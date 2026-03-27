# Scoring Notes — SYS001 Cellule eucaryote animale générique

## Identification

- **System ID :** SYS001
- **System name :** Cellule individuelle animale eucaryote générique (type fibroblaste)
- **Domain :** biological
- **Subdomain :** biologie cellulaire
- **Scale :** micro
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Alberts et al., *Molecular Biology of the Cell*, 7th ed., Garland Science — référence fondamentale structure/fonction cellulaire
2. Lodish et al., *Molecular Cell Biology*, 9th ed. — physiologie cellulaire, transport, cycle cellulaire
3. Nelson & Cox, *Lehninger Principles of Biochemistry*, 8th ed. — métabolisme, régulation enzymatique, signalisation
4. Bray, *Cell Movements*, 2nd ed. — cytosquelette, motilité, signalisation mécanique

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveau moléculaire (enzymes, métabolites) et niveau des organites (mitochondrie, RE, noyau) constituent deux niveaux causaux clairement distincts. Les réactions biochimiques dans la matrice mitochondriale causent un état énergétique au niveau de l'organite entier.                                                                                                                                                                           |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Troisième niveau : la cellule entière comme unité fonctionnelle intégrée (cycle cellulaire, forme, motilité). Le checkpoint G1/S intègre des signaux de multiples voies pour produire une décision cellulaire globale (proliférer ou non).                                                                                                                                                                                                         |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | On peut distinguer : (1) molécules individuelles, (2) complexes macromoléculaires (ribosome, protéasome, spliceosome), (3) organites/compartiments, (4) cellule entière. Le niveau « complexe macromoléculaire » est fonctionnellement réel mais sa distinction causale propre par rapport aux niveaux adjacents est parfois floue — un ribosome est-il un niveau causal distinct de « la machinerie du RE rugueux » ?                             |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau remplit des fonctions qualitativement différentes : catalyse/liaison au niveau moléculaire, biosynthèse/dégradation au niveau des complexes, compartimentation/métabolisme spécialisé au niveau des organites, intégration/décision au niveau cellulaire global. Le noyau (stockage/expression génétique) vs. mitochondrie (énergie) vs. RE (synthèse protéique/lipidique) illustrent une différenciation fonctionnelle nette.       |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Exemple canonique : la signalisation rétrograde mitochondriale — le stress mitochondrial (niveau organite) modifie l'expression génique nucléaire (niveau noyau/cellule), et inversement le noyau régule la biogenèse mitochondriale. Autre exemple : le cytosquelette (niveau cellulaire) régule le trafic vésiculaire (niveau organite) qui régule la composition membranaire locale (niveau moléculaire), avec des rétroactions à chaque étape. |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
La principale hésitation porte sur H3. Le 4ème niveau (complexes macromoléculaires comme unité causale autonome) est biologiquement réel — le spliceosome prend des « décisions » d'épissage, le protéasome sélectionne ses substrats — mais la frontière causale avec les niveaux adjacents est moins tranchée que les trois premiers niveaux. Score 0.5 justifié.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Un dommage à l'ADN (module : génome) active la voie ATM/ATR qui bloque le cycle cellulaire (module : progression du cycle), modifie le métabolisme (module : énergétique), et peut déclencher l'apoptose (module : survie). Une perturbation d'un seul module se propage systématiquement.                                                                                                          |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | La liaison d'un ligand (niveau moléculaire) à un récepteur membranaire déclenche une cascade de signalisation (MAPK, PI3K) qui modifie l'expression génique (niveau noyau) et restructure le cytosquelette (niveau cellulaire entier). Traversée de 3 niveaux hiérarchiques par une seule perturbation.                                                                                             |
| P3 : Propagation modifie l'état global observable             | 1     | L'activation de la voie Rho/Rac par un signal extracellulaire modifie la morphologie cellulaire entière (de fusiforme à étalé), le profil d'expression génique, et le comportement migratoire. L'état global observable de la cellule est transformé.                                                                                                                                               |
| P4 : Isolement difficile sans modification structurelle       | 1     | Les voies de signalisation partagent des composants (cross-talk) : Ras est un nœud commun à MAPK, PI3K/Akt, et Ral-GEF. Isoler une voie de signalisation nécessite des mutations ou des inhibiteurs chimiques — c'est-à-dire une modification structurelle du système. L'architecture même du réseau de signalisation rend l'isolement fonctionnel impossible sans intervention.                    |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage entre métabolisme énergétique et expression génique illustre un couplage non trivial : le ratio NAD⁺/NADH (état métabolique) régule directement les sirtuines (déacétylases) qui modifient l'épigénome, ce qui altère l'expression de gènes métaboliques — boucle de couplage à travers des mécanismes qualitativement différents (redox → épigénétique → transcription → métabolisme). |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation significative. La cellule eucaryote est un cas d'école de propagation inter-modulaire dense. Le seul débat possible porterait sur P4 : certains modules (ex. peroxysomes) sont relativement découplables, mais au niveau du système global, l'isolement reste structurellement impossible pour les modules majeurs.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Les seconds messagers (Ca²⁺, cAMP, IP₃) constituent des mécanismes explicites de coordination : un signal Ca²⁺ cytosolique coordonne simultanément la contraction (cytosquelette), la sécrétion (vésicules), l'expression génique (NFAT), et le métabolisme (mitochondries). Les GTPases Rab coordonnent le trafic vésiculaire entre compartiments.                                               |
| I2 : Réduction de variance observable    | 1     | L'homéostasie du pH cytosolique (maintenu à ~7.2 malgré la production continue d'acides métaboliques) est une réduction de variance mesurable, assurée par des échangeurs Na⁺/H⁺ et des tampons bicarbonate. De même, la concentration de Ca²⁺ cytosolique est maintenue à ~100 nM malgré un gradient de 10⁴ avec le milieu extracellulaire.                                                      |
| I3 : Synchronisation multi-niveaux       | 1     | Le cycle cellulaire synchronise des événements à tous les niveaux : réplication de l'ADN (moléculaire), duplication du centrosome (organite), réorganisation du cytosquelette (cellulaire), le tout coordonné par les oscillations cyclines/CDK. Les checkpoints vérifient l'alignement entre niveaux avant de permettre la progression.                                                          |
| I4 : Boucles de rétroaction globales     | 1     | La voie mTOR intègre l'état nutritionnel (acides aminés, glucose), l'état énergétique (ATP/AMP via AMPK), les signaux de croissance (PI3K/Akt), et le stress (p53) pour réguler globalement la synthèse protéique, l'autophagie, le métabolisme lipidique et la biogenèse ribosomale. C'est une boucle de rétroaction véritablement globale avec des entrées et sorties multi-niveaux.            |
| I5 : Maintien d'un état global cohérent  | 1     | La cellule maintient un « état différencié » stable : un fibroblaste reste un fibroblaste malgré le renouvellement continu de ses composants moléculaires (turnover protéique, renouvellement membranaire). Ce maintien d'identité implique des réseaux de régulation épigénétique et transcriptionnelle qui forment des attracteurs stables, maintenant un état global cohérent au fil du temps. |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Score maximal solidement justifié. La cellule eucaryote est l'un des systèmes biologiques les mieux caractérisés en termes de mécanismes d'intégration. On pourrait débattre de la « perfection » de cette intégration (des erreurs de coordination existent, comme les erreurs de ségrégation chromosomique), mais les mécanismes sont indiscutablement présents et fonctionnels.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | L'état différencié du fibroblaste constitue un attracteur au sens de Kauffman : le réseau de régulation génique converge vers un profil d'expression stable (expression de vimentine, collagène de type I, etc.) qui se maintient même après perturbation transitoire. Les expériences de reprogrammation (Yamanaka) montrent qu'il faut forcer le système hors de cet attracteur.                               |
| N2 : Correction active d'écart               | 1     | La réponse aux protéines mal repliées (UPR) dans le RE est un exemple canonique : l'accumulation de protéines mal repliées (écart) active IRE1/PERK/ATF6 qui augmentent les chaperones, réduisent la traduction, et augmentent la dégradation (ERAD) — correction active ramenant le RE vers son état fonctionnel normal. La réparation de l'ADN (BER, NER, HR, NHEJ) corrige activement les lésions génomiques. |
| N3 : Hiérarchie de priorités régulatoires    | 1     | La cellule possède une hiérarchie claire : survie > intégrité génomique > croissance > prolifération > fonctions spécialisées. Sous stress, p53 bloque la prolifération (CDK) au profit de la réparation ; sous stress extrême, la survie est abandonnée au profit de l'apoptose (protection de l'organisme). AMPK sous stress énergétique inhibe mTOR (croissance) pour préserver l'ATP (survie).               |
| N4 : Mécanisme interne de stabilisation      | 1     | Les protéines chaperones (HSP70, HSP90) stabilisent en permanence le protéome en empêchant l'agrégation et en assistant le repliement. Les antioxydants endogènes (glutathion, thiorédoxine) maintiennent l'état redox. Le cytosquelette assure la stabilité mécanique. Ces mécanismes fonctionnent en continu, pas seulement en réponse au stress.                                                              |
| N5 : Résistance aux perturbations prolongées | 1     | Un fibroblaste en culture peut survivre et maintenir son identité pendant des semaines en conditions suboptimales (sérum réduit, hypoxie modérée). La quiescence (G0) est un état de résistance prolongée où la cellule réduit son métabolisme tout en maintenant son intégrité et sa capacité de réactivation. L'autophagie permet la survie pendant des périodes prolongées de privation nutritive.            |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation majeure. La normativité cellulaire est très bien documentée.

**Distinction normativité endogène / imposée :**
La normativité de la cellule eucaryote est fondamentalement **endogène** : les mécanismes homéostatiques (UPR, réparation ADN, régulation redox, contrôle du cycle cellulaire) sont encodés dans le génome et opèrent de manière autonome. Cependant, dans un organisme multicellulaire, une composante **imposée** existe : les signaux paracrines et endocrines contraignent le comportement cellulaire (ex. inhibition de contact, signaux apoptotiques extrinsèques). Pour un fibroblaste isolé en culture, la normativité est quasi entièrement endogène. En contexte tissulaire, on estime ~80 % endogène / ~20 % imposée.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | La régulation allostérique des enzymes métaboliques (ex. phosphofructokinase-1 régulée par ATP, citrate, fructose-2,6-bisphosphate) constitue un ajustement paramétrique local continu. La phosphorylation/déphosphorylation modifie les paramètres d'activité de milliers de protéines sans changer leur expression.                                                                                                                                                                                         |
| R2 : Modification durable de configuration interne | 1     | Les modifications épigénétiques (méthylation de l'ADN, modifications d'histones) altèrent durablement le profil d'expression génique sans modifier la séquence d'ADN. Un fibroblaste exposé au TGF-β peut subir une transition vers un phénotype myofibroblaste avec expression d'α-SMA — modification durable qui persiste après retrait du stimulus.                                                                                                                                                        |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Le remodelage du cytosquelette (formation de lamellipodes, filopodes, fibres de stress) reconfigure le réseau structurel de la cellule. La transition épithélio-mésenchymateuse (EMT) est une reconfiguration majeure. Toutefois, pour un fibroblaste générique en conditions normales, la reconfiguration de réseau reste limitée en ampleur par rapport à ce que font des cellules plus plastiques (neurones, cellules souches). Score 0.5 car la capacité existe mais est modérée pour ce type cellulaire. |
| R4 : Modification des mécanismes de régulation     | 0.5   | L'expression de nouveaux microARN en réponse à un stress modifie les circuits de régulation post-transcriptionnelle. L'activation de programmes transcriptionnels alternatifs (ex. réponse au stress via NF-κB) installe temporairement de nouveaux circuits régulatoires. Cependant, ces modifications restent dans le répertoire pré-encodé du génome — la cellule ne « crée » pas de nouveaux mécanismes de régulation de novo, elle active des programmes préexistants.                                   |
| R5 : Capacité à produire de nouvelles règles       | 0     | Le fibroblaste n'a pas de capacité démontrable à produire des règles régulatoires véritablement nouvelles (non pré-encodées dans son génome). La mutation somatique pourrait théoriquement générer de nouvelles règles, mais c'est un processus stochastique non dirigé, et non une capacité fonctionnelle du système. L'évolution opère au niveau de la population, pas de la cellule individuelle.                                                                                                          |

**Score A5 = 0.60 / 1.00**

**Hésitations / ambiguïtés :**
R3 pourrait être scoré à 1 si l'on considère l'EMT comme une reconfiguration de réseau complète, mais pour un fibroblaste « générique en conditions normales », 0.5 semble plus juste. R4 est le sous-critère le plus ambigu : la frontière entre « activer un programme régulatoire préexistant » et « modifier un mécanisme de régulation » est subtile. R5 à 0 pourrait être contesté si l'on considère la diversité des réponses épigénétiques comme « nouvelles règles », mais cela étire la définition au-delà du raisonnable.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.90  |
| A2  | 1.00  |
| A3  | 1.00  |
| A4  | 1.00  |
| A5  | 0.60  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | +0.40  |
| Δ₁₂ = A1 − A2 | −0.10  |
| Δ₃₅ = A3 − A5 | +0.40  |
| Δ₄₃ = A4 − A3 | 0.00   |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système hautement intégré et normatif — la cellule eucaryote score au maximum ou quasi-maximum sur les axes de propagation, d'intégration et de normativité, indiquant un système biologique mature et robuste.
- **Régime secondaire :** Plasticité contrainte — le décrochage sur A5 (0.60) révèle un système dont la capacité de révision est limitée par le répertoire génomique pré-encodé. La cellule est un exécutant sophistiqué mais pas un innovateur.
- **Marge :** Le gradient Δ₄₅ = +0.40 est le plus informatif : forte normativité avec plasticité modérée. Ce profil est typique des systèmes biologiques différenciés (par opposition aux cellules souches qui auraient un Δ₄₅ plus faible).
- **Surprise par rapport au jugement intuitif :** Pas de surprise majeure. Le score très élevé sur A2-A3-A4 confirme l'intuition que la cellule eucaryote est un système biologique d'une sophistication remarquable. Le score légèrement réduit sur A1 (0.90 vs 1.00) reflète correctement l'ambiguïté du 4ème niveau hiérarchique. Le 0.60 sur A5 est peut-être le résultat le plus intéressant : il quantifie l'intuition que la cellule est « programmée » plutôt que « créative ».

---

## Notes libres

**Profil global :** La cellule eucaryote animale présente un profil [0.90, 1.00, 1.00, 1.00, 0.60] caractéristique d'un système biologique hautement organisé mais opérant dans un espace de possibilités contraint par son génome. Ce profil est remarquablement « plat » sur les axes A1-A4 (entre 0.90 et 1.00) avec un décrochage net sur A5.

**Comparaison anticipée :** On s'attendrait à ce qu'une cellule souche embryonnaire score plus haut sur A5 (R3 et R4 à 1, voire R5 à 0.5) et qu'un procaryote (E. coli) score plus bas sur A1 et A3 mais potentiellement comparable sur A5 (transfert horizontal de gènes comme forme de R5).

**Limites de l'évaluation :** Le choix d'un « fibroblaste générique » comme représentant de la cellule eucaryote animale est une simplification. Les neurones (A1 plus élevé en raison de la complexité synaptique ?), les cellules immunitaires (A5 plus élevé en raison de la recombinaison V(D)J ?) ou les cellules souches (A5 nettement plus élevé) donneraient des profils différents.

**Question ouverte :** R5 = 0 est-il définitif ? Les phénomènes de « régulation émergente » dans des réseaux de signalisation très interconnectés pourraient constituer des formes de « nouvelles règles » non explicitement encodées mais émergeant de la combinatoire des interactions. Cela dépend de la définition précise de « nouvelle règle » dans le cadre théorique.
