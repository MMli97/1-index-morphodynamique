# Scoring Notes — SYS005 Colonie de fourmis

## Identification

- **System ID :** SYS005
- **System name :** Colonie de fourmis (espèces génériques : *Pogonomyrmex barbatus*, *Linepithema humile*, modèles généraux)
- **Domain :** biological
- **Subdomain :** entomologie sociale / systèmes auto-organisés
- **Scale :** meso
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Gordon, D. M. (2010). *Ant Encounters: Interaction Networks and Colony Behavior*. Princeton University Press.
2. Bonabeau, E., Dorigo, M. & Theraulaz, G. (1999). *Swarm Intelligence: From Natural to Artificial Systems*. Oxford University Press.
3. Theraulaz, G. & Bonabeau, E. (1999). A brief history of stigmergy. *Artificial Life*, 5(2), 97–116.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Deux niveaux clairement identifiables : l'individu (fourmi) et la colonie. Le comportement collectif (allocation de tâches, pistes de fourragement) émerge des interactions locales entre individus (Gordon, chap. 2-3).                                                                                                                                                                                            |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Trois niveaux : (i) physiologie individuelle (seuils de réponse, âge), (ii) interactions locales (contacts antennaires, phéromones), (iii) patterns coloniaux globaux (répartition des tâches, architecture du nid). Bonabeau et al. distinguent explicitement ces niveaux dans leur modèle de seuils de réponse.                                                                                                   |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | Un quatrième niveau peut être identifié : les structures environnementales modifiées (nid, pistes phéromonales) qui constituent un médium stigmergique opérant causalement de façon distincte (Theraulaz & Bonabeau). Cependant, le statut de ce niveau comme "niveau causal" à part entière (vs. médium de couplage) reste discutable.                                                                             |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les niveaux ont des logiques causales différentes : l'individu fonctionne par seuils et règles locales simples, le réseau d'interactions fonctionne par fréquences de contact et feedback, la colonie fonctionne par allocation proportionnelle et régulation homéostatique. Gordon montre que les taux d'interaction déterminent les transitions de tâches selon une logique distincte du comportement individuel. |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Claire bidirectionnalité : les individus produisent les patterns coloniaux (bottom-up), et les patterns coloniaux (concentration phéromonale, taux de contacts) modulent le comportement individuel (top-down). Gordon documente comment le taux de retour des fourrageuses régule la sortie de nouvelles fourrageuses.                                                                                             |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
La principale hésitation concerne H3. Le milieu stigmergique (phéromones déposées, architecture du nid) constitue-t-il un niveau causal autonome ou simplement un canal de communication ? Theraulaz & Bonabeau plaident pour un rôle causal propre de l'environnement modifié (la structure guide l'action indépendamment de l'agent qui l'a produite), ce qui justifie 0.5 plutôt que 0. Cependant, l'absence de dynamique interne propre à ce niveau empêche d'attribuer 1.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Gordon montre qu'une perturbation sur le fourragement (ex. blocage d'un sentier) entraîne un recrutement d'ouvrières depuis d'autres groupes de tâches (maintenance du nid, patrouille). La perturbation d'un module fonctionnel se propage aux autres.                                                                                                       |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Une perturbation au niveau individuel (ex. retrait d'un groupe de fourrageuses) modifie les taux d'interaction locaux, ce qui altère l'allocation globale de la colonie. Inversement, un stress au niveau colonial (pénurie alimentaire) modifie les seuils individuels. Traversée de niveaux documentée dans les deux sens (Gordon, chap. 5).                |
| P3 : Propagation modifie l'état global observable             | 1     | Les expériences de Gordon montrent que des perturbations localisées (ajout de billes de verre sur un sentier, présentation de proies) modifient le ratio global d'allocation des tâches de la colonie entière en quelques minutes. L'état global est mesurablément modifié.                                                                                   |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | Le couplage phéromonal et par contacts rend l'isolement d'un module fonctionnel difficile sans intervention physique (barrières, séparation spatiale). Cependant, la nature locale des interactions signifie qu'un certain degré de modularité spatiale existe naturellement : des fourrageuses éloignées sont partiellement découplées. Score intermédiaire. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage entre modules passe par des mécanismes indirects (phéromones, taux de contacts, stigmergie) et non par des connexions directes point-à-point. Bonabeau et al. montrent que ce couplage produit des propriétés non linéaires (bifurcations, hystérésis dans le choix de chemin). Le couplage est clairement non trivial.                           |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
P4 est délicat. Les fourmis n'ont pas de communication globale instantanée ; la propagation dépend de la proximité physique et de la diffusion phéromonale, ce qui introduit une modularité spatiale de fait. L'isolement n'est pas impossible (certaines parties du nid peuvent fonctionner de manière semi-autonome), mais il n'est pas non plus simple à réaliser sans modifier la géographie du nid.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Plusieurs mécanismes de coordination bien documentés : phéromones de piste (coordination du fourragement), contacts antennaires (régulation des taux d'interaction selon Gordon), signaux d'alarme, trophallaxie. Ce sont des mécanismes explicites, bien que décentralisés.                                                                                                                                                |
| I2 : Réduction de variance observable    | 1     | La colonie maintient des ratios d'allocation de tâches relativement stables malgré la variabilité individuelle. Gordon montre que les colonies matures ont des profils d'allocation reproductibles d'un jour à l'autre. Le fourragement collectif converge vers des solutions efficaces (exploitation du chemin le plus court), réduisant la variance par rapport à l'exploration individuelle aléatoire (Bonabeau et al.). |
| I3 : Synchronisation multi-niveaux       | 0.5   | Il existe une synchronisation partielle : les rythmes circadiens individuels sont alignés avec l'activité coloniale, et les transitions de tâches sont coordonnées temporellement. Cependant, il n'y a pas de mécanisme centralisé de synchronisation — elle émerge des interactions locales avec un certain degré de bruit. La synchronisation est réelle mais imparfaite et indirecte.                                    |
| I4 : Boucles de rétroaction globales     | 1     | Boucles de rétroaction positive (recrutement phéromonal amplifiant l'exploitation d'une source) et négative (saturation de la piste, retour de fourrageuses à vide inhibant les sorties selon Gordon). Ces boucles opèrent au niveau global de la colonie et sont largement documentées dans les trois sources.                                                                                                             |
| I5 : Maintien d'un état global cohérent  | 0.5   | La colonie maintient une cohérence fonctionnelle (allocation des tâches, intégrité du nid) mais cette cohérence est statistique et approximative, pas exacte. Gordon note que les colonies montrent une personnalité stable (agressivité, profil de fourragement) mais avec des fluctuations significatives. L'état global est cohérent au sens tendanciel, non au sens d'un état précisément défini et maintenu.           |

**Score A3 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
I3 et I5 reflètent une tension fondamentale des systèmes auto-organisés : l'intégration est réelle mais intrinsèquement approximative. La colonie n'a pas de représentation interne de son propre état ; elle converge vers des régimes fonctionnels sans les "viser" explicitement. La synchronisation multi-niveaux (I3) est émergente et imparfaite. Le maintien de cohérence (I5) est robuste en moyenne mais bruyant instantanément.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Les ratios d'allocation de tâches constituent des attracteurs bien documentés : après perturbation, la colonie revient à un profil typique. Bonabeau et al. modélisent ces attracteurs formellement via les modèles de seuils de réponse. Le choix collectif de chemin (convergence vers le chemin le plus court) est un autre attracteur classique.                                              |
| N2 : Correction active d'écart               | 1     | Gordon montre que lorsque des fourrageuses sont retirées, la colonie réalloue des ouvrières d'autres tâches pour compenser. Lorsqu'une brèche apparaît dans le nid, des ouvrières sont recrutées pour la réparer. La correction est active : elle implique des changements comportementaux individuels en réponse au déséquilibre global.                                                         |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Il existe une priorisation implicite : la défense du nid prime sur le fourragement en cas de menace, et le soin au couvain prime sur la maintenance. Cependant, cette hiérarchie n'est pas explicitement encodée — elle émerge des différences de seuils individuels et d'intensité de stimuli. Elle est fonctionnelle mais pas structurellement formalisée.                                      |
| N4 : Mécanisme interne de stabilisation      | 1     | Les boucles de rétroaction négative (évaporation des phéromones, saturation des signaux de recrutement, contacts inhibiteurs documentés par Gordon) constituent des mécanismes internes de stabilisation qui empêchent l'emballement des boucles positives. L'évaporation phéromonale est un mécanisme élégant de stabilisation temporelle.                                                       |
| N5 : Résistance aux perturbations prolongées | 0.5   | Les colonies sont remarquablement robustes aux perturbations ponctuelles, mais les perturbations prolongées (perte durable de fourrageuses, stress environnemental chronique) finissent par dégrader la performance et peuvent mener à l'effondrement. Gordon note que les colonies jeunes sont plus vulnérables et que la résilience dépend de la taille. Robustesse significative mais limitée. |

**Score A4 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
N3 est délicat. La hiérarchie de priorités existe fonctionnellement (les fourmis ne vont pas fourrager pendant une attaque), mais elle résulte de la dynamique des seuils plutôt que d'une architecture de contrôle hiérarchique. Le score de 0.5 reflète cette ambiguïté : la hiérarchie est réelle dans ses effets mais émergente dans son mécanisme.

**Distinction normativité endogène / imposée :**
La normativité est très largement endogène. Les attracteurs et les mécanismes de correction dérivent de l'auto-organisation interne de la colonie, pas d'une contrainte externe. Les normes sont inscrites dans l'architecture des interactions (seuils, phéromones, contacts) et non imposées par un contrôleur ou un environnement coercitif. La sélection naturelle a façonné ces mécanismes, mais la régulation elle-même est intrinsèque au fonctionnement du système.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1     | Les fourmis individuelles ajustent leurs seuils de réponse en fonction de l'expérience locale (fréquence de contacts, succès du fourragement). Gordon documente que les fourrageuses modifient leur taux de sortie en fonction du taux de retour. Ce sont des ajustements paramétriques continus au sein d'une structure fixe.                                                                                                                   |
| R2 : Modification durable de configuration interne | 1     | La polyéthisme d'âge (progression temporelle des tâches) et l'apprentissage individuel (familiarisation avec des routes, reconnaissance de compagnes de nid) constituent des modifications durables de la configuration individuelle. Au niveau colonial, la maturation de la colonie (décrite par Gordon) modifie durablement les profils comportementaux collectifs.                                                                           |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | La colonie peut reconfigurer partiellement ses réseaux d'interaction (redéploiement spatial, modification des pistes phéromonales, réarchitecturation partielle du nid). Cependant, cette reconfiguration est contrainte : la structure du nid ne change pas radicalement, et les patterns d'interaction restent dans un espace limité. La stigmergie permet une certaine flexibilité structurelle (Theraulaz & Bonabeau) mais dans des limites. |
| R4 : Modification des mécanismes de régulation     | 0     | La colonie ne modifie pas ses propres mécanismes de régulation au cours de sa vie. Les règles de réponse aux phéromones, les mécanismes de contact antennaire, les principes de stigmergie restent les mêmes. La régulation peut changer quantitativement (seuils) mais pas qualitativement (mécanismes). Il n'y a pas de méta-régulation au sein d'une génération coloniale.                                                                    |
| R5 : Capacité à produire de nouvelles règles       | 0     | La colonie ne génère pas de nouvelles règles comportementales. Les fourmis opèrent avec un répertoire comportemental fixe, génétiquement déterminé. L'innovation comportementale intra-coloniale n'est pas documentée dans les sources. L'évolution peut produire de nouvelles règles, mais à l'échelle transgénérationnelle, non au niveau du système individuel (une colonie).                                                                 |

**Score A5 = 0.50 / 1.00**

**Hésitations / ambiguïtés :**
R3 est le point d'hésitation principal. La stigmergie permet une forme de reconfiguration structurelle (les pistes changent, le nid est remodelé), mais ces changements opèrent dans un espace de possibilités prédéfini. La colonie ne peut pas inventer un nouveau type de structure, seulement réarranger les éléments existants. Le 0.5 reconnaît cette plasticité limitée.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.90  |
| A2  | 0.90  |
| A3  | 0.80  |
| A4  | 0.80  |
| A5  | 0.50  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | +0.10  |
| Δ₄₅ = A4 − A5 | +0.30  |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | +0.30  |
| Δ₄₃ = A4 − A3 | 0.00   |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système auto-organisé à haute propagation et normativité endogène, avec plasticité limitée.
- **Régime secondaire :** Système stigmergique à intégration émergente.
- **Marge :** Le gradient Δ₄₅ = +0.30 est le plus marqué : la colonie régule bien mieux qu'elle n'innove. Le gradient Δ₃₅ = +0.30 confirme que l'intégration est forte par rapport à la capacité de révision. Profil typique d'un système robuste mais conservateur.
- **Surprise par rapport au jugement intuitif :** Peu de surprise. Le profil confirme l'intuition d'un système remarquablement bien organisé mais rigide dans ses mécanismes. La seule légère surprise est le score élevé de A1 (0.90) — on pourrait intuitivement sous-estimer la profondeur hiérarchique d'un système "décentralisé", mais la littérature montre clairement une stratification causale multi-niveaux.

---

## Notes libres

**Observation clé :** La colonie de fourmis constitue un cas paradigmatique de système où l'intégration et la normativité sont élevées *sans* contrôle centralisé. Cela en fait un test intéressant pour tout framework d'évaluation systémique : si le framework exigeait un contrôle centralisé pour scorer haut en intégration ou normativité, il échouerait sur ce cas.

**Profil caractéristique :** Le découplage entre A4 (normativité forte) et A5 (révision faible) est caractéristique des systèmes biologiques sociaux insectes : la sélection naturelle a optimisé les mécanismes de régulation, mais la capacité de modification de ces mécanismes est réservée au niveau évolutif, pas au niveau du système individuel.

**Question ouverte :** La maturation coloniale (décrite par Gordon — les colonies deviennent plus stables et prévisibles avec l'âge) constitue-t-elle une forme de R4 (modification des mécanismes de régulation) ? L'argument serait que les seuils collectifs changent qualitativement avec l'âge. Contre-argument : ce sont les mêmes mécanismes qui s'expriment différemment en raison de changements démographiques (ratio d'ouvrières âgées/jeunes), pas une véritable modification du mécanisme lui-même. Le score de 0 pour R4 reflète le contre-argument.

**Comparaison utile :** Comparer avec un organisme multicellulaire (intégration plus forte, normativité comparable, révision potentiellement plus élevée via plasticité développementale) et avec un essaim temporaire (intégration plus faible, normativité plus faible).
