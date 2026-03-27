# Scoring Notes — SYS014 Réseau neuronal biologique

## Identification

- **System ID :** SYS014
- **System name :** Réseau neuronal biologique (cortex cérébral)
- **Domain :** biological
- **Subdomain :** neurosciences
- **Scale :** meso (circuits corticaux → régions → cerveau entier)
- **Date scored :** 2026-03-16
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Sporns O. — *Networks of the Brain* (2011), MIT Press
2. Friston K. — Free energy principle & predictive processing (2010+)
3. Kandel E. et al. — *Principles of Neural Science*, 6th ed. (2021)

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Synapse → neurone → circuit local : au minimum deux niveaux causaux clairement établis (Kandel ch. 2-4). Les potentiels post-synaptiques causent l'activité neuronale, qui cause l'activité du circuit.                                                                                                                         |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Synapse → neurone → colonne corticale → aire fonctionnelle. La hiérarchie corticale (V1→V2→V4→IT dans le flux ventral) constitue au moins trois niveaux causaux distincts (Sporns ch. 4).                                                                                                                                       |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Molécule (neurotransmetteur) → synapse → neurone → microcircuit (colonne) → aire corticale → réseau large échelle (default mode network, etc.). Au moins 5-6 niveaux identifiables (Sporns ch. 2-6).                                                                                                                            |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau remplit une fonction distincte : la synapse opère le filtrage/pondération du signal, le neurone intègre et décide (seuil de décharge), la colonne extrait un trait local, l'aire traite une modalité, le réseau large échelle coordonne des fonctions cognitives (Kandel ch. 17-21).                              |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Connections feedforward ET feedback omniprésentes dans le cortex. Les projections top-down (prédictions, modulation attentionnelle) sont aussi denses que les projections bottom-up (Friston — predictive processing). La plasticité synaptique (niveau bas) est modulée par des signaux globaux (niveau haut), et inversement. |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation majeure. Le cortex est l'un des systèmes biologiques les plus clairement hiérarchisés et multi-échelles. La seule subtilité est que la hiérarchie n'est pas strictement sérielle mais partiellement parallèle — ce qui ne réduit pas la profondeur mais complexifie sa description.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une lésion focale (ex. : aire de Broca) affecte des fonctions distribuées (production du langage, planification motrice associée). Les crises épileptiques focales se propagent à des régions distantes (Kandel ch. 50).                                                                        |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un changement synaptique (LTP) dans l'hippocampe modifie le comportement de réseaux entiers ; une lésion corticale modifie l'activité synaptique en aval par dégénérescence wallérienne. La propagation inter-niveaux est la règle, pas l'exception (Sporns ch. 7).                             |
| P3 : Propagation modifie l'état global observable             | 1     | Une perturbation locale peut modifier l'état de conscience global (ex. : stimulation du claustrum, lésion thalamique). Les états globaux (sommeil, éveil, anesthésie) sont sensibles à des perturbations relativement localisées (Kandel ch. 51).                                               |
| P4 : Isolement difficile sans modification structurelle       | 1     | L'architecture small-world du connectome rend l'isolement fonctionnel d'une région quasiment impossible sans lésion physique ou déconnexion chirurgicale (callosotomie, etc.). La connectivité dense et les hubs (Sporns ch. 6) empêchent tout cloisonnement spontané.                          |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage n'est pas une simple chaîne linéaire : il implique des boucles réentrantes, des oscillations couplées entre bandes de fréquence (cross-frequency coupling), et des interactions non-linéaires (Friston). La relation entre perturbation et effet est hautement contexte-dépendante. |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
On pourrait discuter P3 en notant que certaines perturbations locales restent effectivement locales (redondance, dégénérescence fonctionnelle). Mais le critère demande si la propagation *peut* modifier l'état global — ce qui est indiscutablement le cas. Score 1 maintenu.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                             |
| ---------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Synchronisation oscillatoire (gamma, theta, alpha) comme mécanisme de binding fonctionnel entre régions (Sporns ch. 8). Modulation neuromodulatoire globale (dopamine, sérotonine, noradrénaline) coordonne les états fonctionnels (Kandel ch. 40-43).                                                    |
| I2 : Réduction de variance observable    | 1     | L'attention réduit la variabilité de la réponse neuronale (réduction du bruit). L'apprentissage réduit la variance des patterns d'activation pour un stimulus donné. Le cortex supprime activement les signaux non pertinents (inhibition latérale, suppression surround) (Kandel ch. 25).                |
| I3 : Synchronisation multi-niveaux       | 1     | Couplage phase-amplitude entre oscillations lentes (delta/theta, réseau large) et oscillations rapides (gamma, circuits locaux). Les rythmes thalamocorticaux coordonnent l'activité à travers tous les niveaux de la hiérarchie (Sporns ch. 8 ; Friston).                                                |
| I4 : Boucles de rétroaction globales     | 1     | Boucles cortico-thalamo-corticales, boucles cortico-basales-ganglionnaires, boucle cortico-cérébelleuse. Le predictive processing de Friston modélise le cerveau entier comme une hiérarchie de boucles prédiction/erreur opérant à toutes les échelles.                                                  |
| I5 : Maintien d'un état global cohérent  | 1     | La conscience elle-même est un état global cohérent maintenu activement. Les états de vigilance (éveil/sommeil) sont des états globaux stables. La théorie de l'information intégrée (Tononi) formalise cette cohérence. Le connectome maintient une intégration fonctionnelle mesurable (Sporns ch. 10). |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
I5 pourrait être discuté : certains états pathologiques (split-brain, dissociation) montrent une fragmentation de la cohérence globale, ce qui suggère que le maintien de l'état cohérent est actif mais pas garanti. Cela ne diminue pas le score — au contraire, la *possibilité* de fragmentation confirme que la cohérence n'est pas triviale mais activement maintenue.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1     | États attracteurs bien documentés : états de vigilance (éveil, sommeil NREM, REM), états par défaut (default mode network au repos). Les dynamiques corticales convergent vers des attracteurs mesurables en EEG/fMRI (Sporns ch. 9).                                                                                    |
| N2 : Correction active d'écart               | 1     | L'homéostasie synaptique (synaptic scaling) corrige les dérives d'activité. Le predictive processing (Friston) est fondamentalement un mécanisme de minimisation de l'erreur de prédiction — correction continue d'écart entre prédiction et signal entrant.                                                             |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Le tronc cérébral priorise les fonctions vitales (respiration, rythme cardiaque) sur toute activité corticale. L'amygdale peut court-circuiter le traitement cortical pour prioriser la survie. La modulation attentionnelle impose des priorités entre flux informationnels (Kandel ch. 51, 21).                        |
| N4 : Mécanisme interne de stabilisation      | 1     | Inhibition GABAergique comme stabilisateur fondamental (sans elle : épilepsie). Homéostasie synaptique (Turrigiano). Régulation de l'excitabilité intrinsèque. Plasticité homéostatique à toutes les échelles (Kandel ch. 66).                                                                                           |
| N5 : Résistance aux perturbations prolongées | 1     | Récupération fonctionnelle après AVC (neuroplasticité compensatoire). Adaptation à la privation sensorielle chronique (réorganisation corticale). Résistance à la neurodégénérescence progressive grâce à la réserve cognitive (Sporns ch. 11). Le système maintient sa fonction malgré la perte neuronale liée à l'âge. |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
N5 : la résistance a des limites (maladies neurodégénératives avancées, lésions massives). Mais le critère évalue la *capacité* de résistance, pas son caractère absolu. Le cortex montre une résilience remarquable face aux perturbations prolongées. Score 1 maintenu.

**Distinction normativité endogène / imposée :**
Entièrement endogène. La normativité du cortex émerge de ses propres dynamiques : homéostasie synaptique, oscillations intrinsèques, minimisation de l'énergie libre. Aucun agent externe n'impose les états attracteurs ou les mécanismes de correction — ils sont des propriétés émergentes de l'architecture neuronale elle-même.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Plasticité synaptique (LTP/LTD) : modification des poids synaptiques individuels en fonction de l'activité. C'est le mécanisme le plus fondamental et le mieux documenté de l'apprentissage (Kandel ch. 64-66).                                                                                                                                                                                                                                          |
| R2 : Modification durable de configuration interne | 1     | Consolidation mnésique : les patterns d'activation transitoires deviennent des configurations stables (mémoire à long terme). Remodelage dendritique (synaptogenèse, élagage) modifie durablement la connectivité locale (Kandel ch. 66).                                                                                                                                                                                                                |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Réorganisation corticale après lésion (remapping somatotopique). Neurogenèse adulte (hippocampe). Plasticité inter-modale (cortex visuel recruté pour le braille chez les aveugles). Ces reconfigurations modifient la topologie du réseau, pas seulement ses paramètres (Sporns ch. 11).                                                                                                                                                                |
| R4 : Modification des mécanismes de régulation     | 1     | Métaplasticité : la plasticité elle-même est plastique (le seuil de LTP/LTD se déplace en fonction de l'histoire d'activation — BCM theory). Les règles de modulation neuromodulatoire changent avec l'expérience (sensibilisation/désensibilisation des récepteurs). La régulation de la régulation est un phénomène bien établi (Kandel ch. 66 ; Friston).                                                                                             |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Le cortex peut développer de nouvelles stratégies cognitives (apprentissage de règles abstraites, transfert). Cependant, les *mécanismes fondamentaux* de plasticité (LTP/LTD, modulation, homéostasie) restent les mêmes — ce sont les configurations qui changent, pas les principes biophysiques sous-jacents. Le cortex produit de nouvelles « règles comportementales » mais pas de nouveaux « mécanismes de production de règles » au sens strict. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
R5 est le point de tension principal. On pourrait argumenter un score de 1 si l'on considère que les nouvelles stratégies cognitives (développement du langage, invention mathématique) constituent de véritables nouvelles règles. Le score de 0.5 reflète le fait que les mécanismes biophysiques de base restent fixes — la créativité opère *dans* le cadre existant, elle ne le remplace pas. C'est une limite constitutive du substrat biologique.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 1.00  |
| A4  | 1.00  |
| A5  | 0.90  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | +0.10  |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | +0.10  |
| Δ₄₃ = A4 − A3 | 0.00   |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système autonome intégré — scores maximaux ou quasi-maximaux sur tous les axes ; profil caractéristique d'un système biologique mature hautement organisé.
- **Régime secondaire :** Système adaptatif complexe — la plasticité multi-échelle et la normativité endogène placent le cortex dans la catégorie des systèmes capables d'auto-réorganisation.
- **Marge :** Très faible. Seul R5 (0.5) introduit un écart, et il est argumentable dans les deux sens.
- **Surprise par rapport au jugement intuitif :** Aucune. Le cortex cérébral est le système de référence implicite pour la plupart de ces critères — il serait surprenant qu'il ne score pas au plafond ou presque.

---

## Notes libres

Le cortex neuronal biologique constitue un cas canonique — presque un étalon — pour cette grille d'évaluation. Les cinq axes y sont saturés ou quasi-saturés, ce qui en fait un point de comparaison naturel pour tous les autres systèmes.

Le seul point de discussion substantiel est R5 (production de nouvelles règles). L'argument pour 0.5 repose sur la distinction entre *recombinaison créative dans un cadre fixe* (ce que fait le cortex) et *modification du cadre lui-même* (ce que ferait un système capable de réécrire ses propres mécanismes de plasticité). Cette distinction est philosophiquement chargée : le développement du langage, par exemple, a-t-il modifié les « règles du jeu » cortical, ou simplement exploité des capacités préexistantes ? La réponse dépend du grain d'analyse.

Le profil plat (gradients proches de zéro) est typique des systèmes biologiques ayant subi une longue pression de sélection : chaque axe a été co-optimisé avec les autres, éliminant les déséquilibres.
