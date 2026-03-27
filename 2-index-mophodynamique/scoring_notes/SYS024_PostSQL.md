# Scoring Notes — SYS024 Base de données relationnelle (PostgreSQL)

## Identification

- **System ID :** SYS001
- **System name :** Base de données relationnelle — PostgreSQL (production)
- **Domain :** technological / infrastructure
- **Subdomain :** systèmes de gestion de données
- **Scale :** meso
- **Date scored :** 2026-03-17
- **Scorer :** —
- **Confidence globale :** high

## Sources

1. Ramakrishnan, R. & Gehrke, J. — *Database Management Systems* (McGraw-Hill, 3rd ed.). Chapitres sur les propriétés ACID, le contrôle de concurrence, la récupération après panne.
2. Hellerstein, J., Stonebraker, M., Hamilton, J. — "Architecture of a Database System" in *Foundations and Trends in Databases* 1(2), 2007. Sur l'architecture multi-couches et les mécanismes de cohérence.
3. PostgreSQL Global Development Group — Documentation officielle, sections sur le WAL (Write-Ahead Logging), MVCC, et le query planner.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au minimum deux niveaux causaux clairement distincts : la couche SQL/requête (logique applicative) et la couche moteur de stockage (pages, tuples). Une requête SQL cause des modifications physiques sur les blocs disque via plusieurs mécanismes intermédiaires.                                                                                                                      |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Trois niveaux identifiables : (1) interface client/SQL parser, (2) query planner/executor, (3) storage manager + buffer pool. L'architecture en couches de Hellerstein et al. (2007) en documente au moins cinq (client, process manager, relational query processor, storage manager, shared components).                                                                               |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Quatre niveaux causaux distincts documentés : parser → planner → executor → storage/WAL. Chaque niveau produit des effets causaux sur le suivant sans que le niveau supérieur contrôle directement les mécanismes du niveau inférieur.                                                                                                                                                   |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Différenciation fonctionnelle forte : le planner optimise sans stocker ; le WAL journalise sans exécuter ; le MVCC gère la visibilité sans planifier. Chaque couche a un rôle non substituable par les autres.                                                                                                                                                                           |
| H5 : Causalité bidirectionnelle entre niveaux | 0.5   | Bidirectionnalité partielle : le query planner consulte les statistiques remontées depuis le storage (pg_statistic), et le buffer pool informe le coût d'exécution. Toutefois, la bidirectionnalité reste asymétrique : le flux descendant (requête → stockage) est dominant ; le flux montant (feedback du stockage vers le planner) est informatif mais non régulateur au sens strict. |

**Score A1 = 0.90 / 1.00**

*(calcul : moyenne des 5 sous-critères = (1 + 1 + 1 + 1 + 0.5) / 5 = 4.5 / 5 → normalisé sur 1.00)*

**Hésitations / ambiguïtés :** H5 : la causalité ascendante (autovacuum → stats → planner) existe mais reste périodique et non temps-réel ; on peut débattre si cela constitue une véritable bidirectionnalité causale ou une simple rétroaction différée. Score 0.5 retenu.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une corruption de page dans le buffer pool affecte immédiatement le query executor (erreur ou résultat erroné) et peut déclencher le WAL recovery. Un verrou posé par une transaction affecte le lock manager et bloque d'autres sessions.                                                                                                                                                                                                                                  |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un deadlock au niveau transaction (niveau logique) force une intervention du lock manager (niveau concurrence) qui annule une transaction et déclenche un rollback impactant le WAL (niveau physique). La propagation traverse au moins deux niveaux hiérarchiques.                                                                                                                                                                                                         |
| P3 : Propagation modifie l'état global observable             | 1     | Une transaction COMMIT modifie l'état global visible par toutes les sessions suivantes (MVCC : le snapshot change). Une panne pendant un CHECKPOINT modifie l'état du WAL et force un replay au redémarrage, état observable via pg_stat_recovery.                                                                                                                                                                                                                          |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | L'isolation est partiellement possible : les tablespaces et schemas permettent une séparation logique ; la réplication logique permet d'isoler des flux. Mais un verrou sur une table système (pg_class) ou une corruption du WAL impacte l'ensemble de l'instance sans possibilité d'isolation partielle sans intervention structurelle (arrêt, restauration). Score 0.5 car l'isolement est possible dans certains cas (partitionnement) mais pas dans les cas critiques. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage MVCC ↔ autovacuum ↔ transaction ID wraparound constitue un exemple de couplage non trivial documenté : un gel insuffisant des XIDs peut rendre la base inaccessible. Le couplage WAL ↔ réplication ↔ point de reprise est également non trivial et source de défaillances en cascade documentées.                                                                                                                                                               |

**Score A2 = 0.90 / 1.00**

*(4.5 / 5)*

**Hésitations / ambiguïtés :** P4 : le partitionnement natif et les extensions comme pg_partman améliorent l'isolement, ce qui tempère le score ; mais les ressources partagées (shared_buffers, WAL) restent un point de couplage irréductible.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I1 : Mécanisme explicite de coordination | 1     | Mécanismes multiples et explicitement documentés : le lock manager coordonne l'accès concurrent ; le WAL coordonne la persistance et la réplication ; le process manager (postmaster) coordonne les processus backend.                                                                                                                                                         |
| I2 : Réduction de variance observable    | 1     | Le MVCC réduit la variance des lectures (chaque transaction voit un snapshot cohérent, indépendamment des écritures concurrentes). Les contraintes d'intégrité (PK, FK, CHECK) réduisent la variance des états stockés. Le query planner réduit la variance des temps d'exécution via la sélection du plan optimal.                                                            |
| I3 : Synchronisation multi-niveaux       | 1     | Synchronisation documentée à plusieurs niveaux : (a) synchronisation des écritures via WAL flush avant commit ; (b) synchronisation des lectures via snapshot MVCC ; (c) synchronisation des processus via le postmaster et les signaux inter-processus ; (d) synchronisation avec les réplicas via les LSN (Log Sequence Numbers).                                            |
| I4 : Boucles de rétroaction globales     | 0.5   | Boucles de rétroaction présentes mais partielles. L'autovacuum constitue une boucle : accumulation de tuples morts → déclenchement autovacuum → mise à jour des statistiques → amélioration des plans. Mais ces boucles sont périodiques et non continues ; il n'existe pas de régulation globale en temps réel de l'état de la base (contrairement à un système de contrôle). |
| I5 : Maintien d'un état global cohérent  | 1     | C'est la propriété centrale de PostgreSQL : les propriétés ACID (Atomicité, Cohérence, Isolation, Durabilité) garantissent le maintien d'un état global cohérent après chaque transaction, y compris après crash (grâce au WAL et au crash recovery).                                                                                                                          |

**Score A3 = 0.90 / 1.00**

*(4.5 / 5)*

**Hésitations / ambiguïtés :** I4 : la distinction entre boucle de rétroaction au sens cybernétique (continue, corrective) et mécanisme réactif différé (autovacuum, analyze) est non triviale. Score 0.5 retenu car les boucles existent mais ne sont pas globales ni continues.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | L'état cohérent de la base (toutes contraintes satisfaites, WAL à jour, transactions commitées visibles) constitue un attracteur fort : toute perturbation (crash, rollback) ramène le système vers cet état via les mécanismes de recovery. La cohérence transactionnelle est l'attracteur central.                                                                                                                                          |
| N2 : Correction active d'écart               | 1     | Correction active documentée : (a) crash recovery via replay du WAL pour corriger l'écart entre état disque et état committé ; (b) autovacuum pour corriger l'écart entre visibilité des tuples et état réel ; (c) contraintes d'intégrité qui rejettent activement toute écriture créant un écart par rapport aux règles définies.                                                                                                           |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Hiérarchie explicite : durabilité (WAL fsync) > cohérence (contraintes) > isolation (niveaux READ COMMITTED, REPEATABLE READ, SERIALIZABLE) > disponibilité. En cas de conflit, PostgreSQL sacrifie la disponibilité (blocage, rejet) plutôt que la cohérence. Le théorème CAP s'applique : PostgreSQL choisit CP.                                                                                                                            |
| N4 : Mécanisme interne de stabilisation      | 1     | Mécanismes multiples : (a) WAL + checkpoint pour stabiliser l'état persisté ; (b) lock manager pour stabiliser l'accès concurrent ; (c) MVCC pour stabiliser la vue transactionnelle ; (d) autovacuum pour stabiliser l'espace physique et les statistiques. Ces mécanismes opèrent en continu ou à intervalles réguliers.                                                                                                                    |
| N5 : Résistance aux perturbations prolongées | 0.5   | Résistance partielle : PostgreSQL résiste bien aux perturbations courtes (crash serveur, transaction longue, pic de charge). Mais sous perturbations prolongées (transaction ouverte très longue → bloat ; wraparound XID → maintenance forcée ; réplication en retard → wal_keep_size saturé), le système peut atteindre des états dégradés nécessitant une intervention externe. Score 0.5 car la résistance est réelle mais non illimitée. |

**Score A4 = 0.90 / 1.00**

*(4.5 / 5)*

**Hésitations / ambiguïtés :** N5 : la limite XID wraparound est un cas documenté de défaillance normative sous perturbation prolongée (bases très actives sans maintenance). La résistance est robuste dans les conditions nominales mais pas sans borne.

**Distinction normativité endogène / imposée :**
La normativité de PostgreSQL est majoritairement **endogène** : les mécanismes ACID, le WAL, le MVCC et le lock manager sont intégrés à l'architecture et opèrent sans intervention externe. La normativité **imposée** concerne les contraintes définies par l'administrateur (schémas, FK, CHECK) et les paramètres de configuration (fsync, wal_level) — ces normes sont extérieures au moteur mais intégrées à son exécution une fois définies.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | PostgreSQL offre un ajustement paramétrique extensif : `work_mem`, `shared_buffers`, `checkpoint_completion_target`, `autovacuum_vacuum_cost_delay`, etc. — modifiables à chaud (ALTER SYSTEM, SET LOCAL) sans redémarrage pour la plupart. Le query planner ajuste ses estimations via les statistiques (ANALYZE).                                                                                                                                        |
| R2 : Modification durable de configuration interne | 1 :   | Les modifications via ALTER SYSTEM persistent dans `postgresql.auto.conf` et survivent aux redémarrages. Les migrations de schéma (ALTER TABLE, CREATE INDEX CONCURRENTLY) modifient durablement la structure interne. La mise à jour des statistiques (autovacuum analyze) modifie durablement les tables pg_statistic.                                                                                                                                   |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Reconfiguration structurelle possible mais limitée : partitionnement, création/suppression d'index, ajout de colonnes. Toutefois, certaines reconfigurations majeures (changement de type de colonne avec réécriture, passage à un schéma de partitionnement différent) nécessitent des opérations lourdes ou un downtime. Pas de reconfiguration topologique dynamique à chaud comparable à un système distribué natif.                                   |
| R4 : Modification des mécanismes de régulation     | 0.5   | Possible mais encadrée : les règles autovacuum peuvent être ajustées par table (`ALTER TABLE ... SET autovacuum_vacuum_scale_factor`) ; le niveau d'isolation peut être modifié par session ; les extensions (pg_hint_plan) permettent de modifier le comportement du planner. Mais les mécanismes fondamentaux (MVCC, WAL, lock manager) ne sont pas reconfigurables — ils sont fixes par conception.                                                     |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | PostgreSQL permet la création de nouvelles règles via : triggers, règles (RULE), fonctions PL/pgSQL, politiques de sécurité au niveau lignes (RLS). Ces mécanismes permettent d'étendre la normativité du système. Mais la production de nouvelles règles reste dans un espace prédéfini (le langage de règles de PostgreSQL) et ne constitue pas une plasticité endogène au sens fort — le système ne génère pas de nouvelles règles de manière autonome. |

**Score A5 = 0.70 / 1.00**

*(3.5 / 5)*

**Hésitations / ambiguïtés :** R3 et R4 : la frontière entre "reconfiguration structurelle" et "modification opérationnelle" est floue dans le contexte d'une base de données. Score 0.5 retenu pour marquer que la plasticité existe mais reste dans des limites architecturales prédéfinies. R5 : les triggers et RLS sont des règles "produites" mais dans un cadre fixe — plasticité de second ordre, pas de troisième ordre.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.90  |
| A2  | 0.90  |
| A3  | 0.90  |
| A4  | 0.90  |
| A5  | 0.70  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | +0.20  |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | +0.20  |
| Δ₄₃ = A4 − A3 | 0.00   |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système fortement intégré et normatif (A3 = A4 = 0.90)
- **Régime secondaire :** Propagation et hiérarchie élevées, plasticité modérée
- **Marge :** A5 est le seul axe sous 0.80 (Δ₄₅ = +0.20) — écart normativité/révision significatif
- **Surprise par rapport au jugement intuitif :** Légère surprise sur A5 : intuitivement PostgreSQL semble très configurable, mais la plasticité *endogène* (modification autonome des mécanismes de régulation, production de nouvelles règles par le système lui-même) est faible. La configurabilité est externe (DBA), pas auto-générée. A1 légèrement plus élevé qu'attendu grâce à la richesse de l'architecture en couches documentée par Hellerstein et al.

---

## Notes libres

**Profil général :** PostgreSQL présente un profil très régulier sur A1–A4 (0.90 uniforme), avec une chute nette sur A5. Ce profil caractérise un système conçu pour la **robustesse et la cohérence** plutôt que pour l'**auto-adaptation**. C'est cohérent avec la philosophie de conception des SGBD relationnels : garantir des propriétés invariantes (ACID) plutôt qu'évoluer dynamiquement.

**Point de tension conceptuel :** La normativité (A4 = 0.90) sans plasticité endogène forte (A5 = 0.70) crée un système stable mais rigide. Les mécanismes de révision existent (autovacuum, statistiques adaptatives, ajustement paramétrique) mais restent dans un cadre prédéfini et ne constituent pas une révision des règles fondamentales — le système ne peut pas "apprendre" à gérer un nouveau type de charge sans intervention humaine.

**Question ouverte :** La frontière entre PostgreSQL seul et PostgreSQL + Citus (sharding) ou PostgreSQL + pgBouncer (pooling) déplace significativement A3 et A5. Le scoring ici porte sur l'instance PostgreSQL standalone en production standard.

**XID wraparound comme cas limite normatif :** Ce phénomène illustre parfaitement la limite de N5 : le système maintient sa normativité jusqu'à un seuil (2^31 transactions) au-delà duquel il entre en mode de protection d'urgence (base en lecture seule). C'est une normativité à horizon fini, non illimitée.
