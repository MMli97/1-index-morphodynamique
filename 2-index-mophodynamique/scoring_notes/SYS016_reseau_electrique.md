# Scoring Notes — SYS016 Réseau électrique (grid)

## Identification

- **System ID :** SYS016
- **System name :** Réseau électrique interconnecté (power grid)
- **Domain :** infrastructure
- **Subdomain :** énergie / ingénierie électrique
- **Scale :** macro
- **Date scored :** 2026-03-16
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Kundur, P. — *Power System Stability and Control*, McGraw-Hill, 1994
2. U.S. DOE — *Electric Grid Modernization*, Department of Energy reports
3. IEEE — Grid engineering papers (protection, SCADA, frequency control)

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                        |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveau physique (générateurs, lignes, charges) et niveau contrôle (dispatching, SCADA) forment deux strates causales clairement distinctes.                                                                                                                          |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Trois niveaux au minimum : (1) physique électrique (flux de puissance, fréquence), (2) contrôle primaire/secondaire automatisé (governors, AGC), (3) contrôle tertiaire / dispatch économique (opérateur humain + marché).                                           |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | On ajoute (4) la planification et régulation institutionnelle (normes NERC/ENTSO-E, planification d'expansion, règles de marché) qui contraint les trois premiers niveaux.                                                                                           |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau opère avec des constantes de temps, des variables d'état et des logiques différentes : millisecondes (protection), secondes (contrôle primaire), minutes (AGC), heures (dispatch), années (planification).                                             |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | La fréquence (physique) remonte comme signal vers le contrôle ; le contrôle modifie la consigne des générateurs (physique). Les pannes physiques déclenchent des révisions régulatoires (bottom-up), et les normes contraignent les choix d'exploitation (top-down). |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation majeure. Le grid est un cas d'école de hiérarchie multi-niveaux en ingénierie des systèmes. La seule question porte sur le comptage exact des niveaux (4, 5 ou plus selon la granularité choisie), mais même le comptage conservateur dépasse le seuil H3.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Le déclenchement d'un générateur modifie instantanément les flux de puissance sur tout le réseau voisin et surcharge d'autres lignes. La perte d'une ligne redistribue les flux sur les lignes parallèles.                                                                                         |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Une perte de production (niveau physique) déclenche la réponse du contrôle primaire (governors), puis secondaire (AGC), puis potentiellement tertiaire (dispatch). Propagation ascendante systématique.                                                                                            |
| P3 : Propagation modifie l'état global observable             | 1     | Un défaut majeur provoque une déviation de fréquence mesurable sur l'ensemble de la zone synchrone (ex. : la fréquence 50 Hz de l'Europe continentale dévie de façon uniforme lors d'un événement). Les cascading failures (blackout 2003 nord-est USA) démontrent la modification globale d'état. |
| P4 : Isolement difficile sans modification structurelle       | 1     | Les flux de puissance obéissent aux lois de Kirchhoff : on ne peut pas « router » l'électricité comme des paquets de données. Isoler un défaut nécessite l'ouverture de disjoncteurs (modification structurelle topologique). Sans action, la propagation est physiquement inévitable.             |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage est régi par les équations non linéaires de swing (dynamique rotor) et les équations de flux de puissance (load flow). Des effets non linéaires comme l'effondrement de tension ou les oscillations inter-zones illustrent la complexité du couplage.                                  |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune. Le grid est le système technique archétypique pour la propagation de perturbations. Les cascading failures sont un phénomène emblématique étudié massivement dans la littérature (Kundur ch. 12–13, rapports DOE post-2003).

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | SCADA/EMS (Energy Management System) coordonne en temps réel les générateurs, les flux, les protections. Les opérateurs de réseau (TSO/ISO) assurent la coordination explicite entre zones. Protocoles ICCP pour l'échange inter-opérateurs.                                                                                                                                  |
| I2 : Réduction de variance observable    | 1     | La fréquence est maintenue dans une bande étroite (±0.05 Hz en Europe continentale autour de 50 Hz), ce qui représente une réduction de variance remarquable par rapport au régime libre (chaque générateur tournerait à sa propre vitesse sans synchronisation). La tension est également régulée dans des bandes strictes (±5 %).                                           |
| I3 : Synchronisation multi-niveaux       | 1     | Le synchronisme des rotors (niveau physique) est maintenu par le contrôle primaire (niveau automatique) sous la supervision du dispatch (niveau opérationnel). Les trois niveaux doivent être synchronisés pour que le réseau fonctionne. La phase des rotors sur des milliers de km reste cohérente.                                                                         |
| I4 : Boucles de rétroaction globales     | 1     | L'AGC (Automatic Generation Control) est une boucle de rétroaction globale : elle mesure l'écart de fréquence et l'erreur de contrôle de zone (ACE), puis répartit les corrections sur l'ensemble des générateurs participants. Le contrôle tension/réactif opère de façon similaire à l'échelle régionale.                                                                   |
| I5 : Maintien d'un état global cohérent  | 0.5   | Le grid maintient un état cohérent (fréquence, tension, synchronisme) dans des conditions normales et modérément perturbées. Cependant, lors de perturbations extrêmes, le système peut perdre sa cohérence globale (îlotage, blackout partiel, perte de synchronisme). La cohérence est maintenue mais avec des limites connues et des modes de défaillance catastrophiques. |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
I5 est le point de discussion principal. Le grid maintient bien un état cohérent en régime normal, mais les blackouts montrent que cette cohérence peut se fracturer. Le score 0.5 reflète le fait que la cohérence globale est conditionnelle et non absolue. On pourrait argumenter 1 si on considère que l'îlotage contrôlé est lui-même un mécanisme de maintien de cohérence locale.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | L'état synchrone à fréquence nominale (50 ou 60 Hz) est un attracteur au sens dynamique : les équations de swing montrent que le système revient au synchronisme après petite perturbation (stabilité en petit signal, Kundur ch. 12).                                                                                                                                                                     |
| N2 : Correction active d'écart               | 1     | Le contrôle primaire (droop des governors) corrige automatiquement les écarts de fréquence. Le contrôle secondaire (AGC) ramène la fréquence à la valeur nominale exacte. Les régulateurs de tension (AVR) corrigent les écarts de tension. Triple couche de correction active.                                                                                                                            |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Priorités clairement hiérarchisées : (1) protection des équipements et personnes (relais, disjoncteurs — ms), (2) stabilité du réseau (contrôle fréquence/tension — s à min), (3) optimisation économique (dispatch — min à h), (4) adéquation long terme (planification — années). Le délestage de charge illustre cette hiérarchie : on sacrifie la desserte pour sauver le réseau.                      |
| N4 : Mécanisme interne de stabilisation      | 1     | L'inertie des rotors synchrones est un mécanisme physique intrinsèque de stabilisation (résistance aux variations brusques de fréquence). Les impédances de ligne limitent naturellement les courants de court-circuit. Ce sont des mécanismes passifs, internes à la physique du système.                                                                                                                 |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le grid résiste bien aux perturbations modérées et prolongées (variations de charge jour/nuit, perte d'un générateur unique — critère N-1). Cependant, des perturbations prolongées extrêmes (vague de froid prolongée + pertes multiples, comme ERCOT 2021) peuvent dépasser la capacité de résistance et mener à des délestages massifs ou blackouts. La robustesse est dimensionnée mais pas illimitée. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
N5 : la question est de savoir si on évalue la résistance en conditions de design ou en conditions extrêmes. Le grid est conçu pour le critère N-1 (perte d'un élément quelconque) mais pas toujours N-2 ou au-delà. Score 0.5 car la résistance, bien que remarquable, a des limites structurelles démontrées par les blackouts historiques.

**Distinction normativité endogène / imposée :**
Mixte. La normativité physique (inertie rotors, lois de Kirchhoff, attracteur synchrone) est pleinement endogène. La normativité de contrôle (consignes AGC, seuils de protection, critères N-1) est imposée par conception humaine. La normativité institutionnelle (normes NERC, codes réseau) est exogène. Le grid est un cas hybride où la physique fournit une normativité de base que l'ingénierie augmente et structure.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1     | Les consignes des governors, AVR, transformateurs à prises réglables sont ajustées en continu. Le dispatch modifie les points de fonctionnement des générateurs toutes les 5–15 minutes. Les protections adaptatives modifient leurs seuils selon l'état du réseau.                                                                                                |
| R2 : Modification durable de configuration interne | 1     | Le réseau reconfigure sa topologie via l'ouverture/fermeture de disjoncteurs et sectionneurs. Les schémas d'exploitation saisonniers modifient durablement les configurations. L'intégration de nouvelles sources (éolien, solaire) modifie les flux de puissance de façon permanente.                                                                             |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | La reconfiguration structurelle (nouvelles lignes, nouveaux postes, changement de niveau de tension) est possible mais lourde, coûteuse et lente (années de planification et construction). Le réseau ne se reconfigure pas spontanément à grande échelle ; cela nécessite une intervention d'ingénierie et d'investissement majeure.                              |
| R4 : Modification des mécanismes de régulation     | 0.5   | Les mécanismes de régulation évoluent (passage du contrôle analogique au numérique, introduction de FACTS, smart grid, contrôle distribué) mais ces changements sont exogènes — décidés par les ingénieurs et régulateurs, non générés endogènement par le système. Le grid ne modifie pas ses propres règles de contrôle ; ce sont les humains qui les modifient. |
| R5 : Capacité à produire de nouvelles règles       | 0     | Le grid ne génère pas de nouvelles règles de fonctionnement de façon endogène. Toute nouvelle règle (nouveau protocole de protection, nouvelle structure de marché, nouveau code réseau) est le produit d'une décision humaine externe au système technique lui-même. Même les systèmes « smart grid » avec IA appliquent des règles pré-programmées.              |

**Score A5 = 0.60 / 1.00**

**Hésitations / ambiguïtés :**
R3 : on pourrait argumenter 1 si on inclut les reconfigurations topologiques automatiques (self-healing grids, restauration automatique). Cependant, ces capacités restent limitées et pré-programmées. Score 0.5 reflète la capacité réelle mais contrainte.
R4 : les smart grids et le contrôle adaptatif brouillent la frontière. Certains systèmes modernes ajustent leurs paramètres de régulation automatiquement (adaptive relaying), ce qui pourrait justifier un score plus élevé. Mais la modification du mécanisme lui-même (pas juste ses paramètres) reste exogène.
R5 : c'est le point le plus net. Même avec l'IA, le grid n'invente pas ses propres règles. Score 0 sans ambiguïté.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 0.90  |
| A4  | 0.90  |
| A5  | 0.60  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | +0.10  |
| Δ₄₅ = A4 − A5 | +0.30  |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | +0.30  |
| Δ₄₃ = A4 − A3 | 0.00   |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système intégré fortement normatif — haute structure, haute propagation, haute intégration, forte régulation, plasticité limitée.
- **Régime secondaire :** Système rigide-robuste — l'écart Δ₄₅ = +0.30 signale un système qui régule beaucoup mieux qu'il ne se transforme. Le grid corrige les perturbations mais évolue lentement.
- **Marge :** Profil très homogène sur A1–A4 (0.90–1.00) avec décrochage net sur A5 (0.60). Ce profil est typique d'un artefact d'ingénierie mature : haute performance opérationnelle, faible auto-transformation.
- **Surprise par rapport au jugement intuitif :** Aucune surprise majeure. Le score confirme l'intuition d'un système complexe, fortement couplé, bien régulé, mais fondamentalement rigide. Le Δ₄₅ positif élevé est la signature attendue d'un système technique conçu pour la stabilité plutôt que pour l'adaptation.

---

## Notes libres

Le réseau électrique est un cas d'étude exemplaire pour ce cadre d'analyse. Quelques observations :

**Tension fondamentale stabilité/adaptabilité** — Le grid illustre parfaitement le compromis entre robustesse opérationnelle et capacité d'évolution. Sa physique (synchronisme, lois de Kirchhoff) lui confère une normativité endogène puissante mais crée aussi une rigidité structurelle. La transition énergétique (intégration massive d'éolien/solaire, stockage, véhicules électriques) teste précisément cette limite : le système doit se transformer profondément tout en maintenant sa stabilité seconde par seconde.

**Hybridité de la normativité** — Le grid est un cas intéressant de normativité hybride. La physique impose des contraintes dures (synchronisme, limites thermiques) que l'ingénierie ne peut que respecter ou contourner, jamais supprimer. Cette couche de normativité endogène distingue le grid de systèmes purement institutionnels où les normes sont entièrement conventionnelles.

**Propagation comme propriété et comme risque** — La haute propagation (A2 = 1.00) est à la fois une propriété fonctionnelle (le réseau transporte l'énergie précisément parce qu'il est couplé) et un risque systémique (les cascading failures existent parce que ce couplage ne peut pas être désactivé sélectivement). Ce double visage du couplage est caractéristique des infrastructures critiques.

**Comparaison intéressante avec Internet** — Un réseau de données aurait probablement un A5 plus élevé (routage adaptatif, protocoles évolutifs, architecture modulaire) mais potentiellement un A4 plus bas (moins de normativité physique endogène). La comparaison des profils serait instructive.
