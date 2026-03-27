# Scoring Notes — SYS006 Human Gut Microbiome

## Identification

- **System ID :** SYS006
- **System name :** Human Gut Microbiome
- **Domain :** biological
- **Subdomain :** symbiotic microbial ecosystem
- **Scale :** meso
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** medium

## Sources

1. Turnbaugh, P. J., Ley, R. E., Hamady, M., Fraser-Liggett, C., Knight, R., Gordon, J. — *The Human Microbiome Project*, Nature (2007).
2. Sender, R., Fuchs, S., Milo, R. — *Revised Estimates for the Number of Human and Bacterial Cells in the Body*, PLOS Biology (2016).
3. Costello, E. K. et al. — *The Application of Ecological Theory Toward an Understanding of the Human Microbiome*, Science (2012).
4. Coyte, K. Z., Schluter, J., Foster, K. R. — *The Ecology of the Microbiome: Networks, Competition, and Stability*, Science (2015).

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveaux clairement identifiables : (1) souches/espèces individuelles, (2) guildes fonctionnelles (ex. fermenteurs de fibres, producteurs de butyrate). Les dynamiques de compétition intra-espèce causent des effets au niveau des guildes (Coyte et al. 2015).                                                                                               |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Troisième niveau : la communauté microbienne globale (entérotype, profil métagénomique agrégé). Turnbaugh et al. (2007) décrivent un « core microbiome » fonctionnel émergent de l'interaction entre guildes.                                                                                                                                                 |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | Quatrième niveau candidat : l'axe intestin-hôte (métabolisme systémique, immunité muqueuse). Ce niveau est réel mais partiellement exogène au microbiome lui-même — il implique le système immunitaire de l'hôte. On peut argumenter que le microbiome « participe » à ce niveau (production de SCFA, signaux immunitaires) sans le « posséder » entièrement. |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau remplit des fonctions distinctes : les souches se disputent des niches nutritionnelles ; les guildes assurent des fonctions métaboliques spécifiques (protéolyse, fermentation, etc.) ; la communauté globale maintient une homéostasie écologique (Costello et al. 2012).                                                                      |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | La communauté globale contraint les guildes (colonization resistance, compétition pour l'espace) ; les guildes modifient la communauté (production de métabolites qui inhibent ou favorisent d'autres guildes) ; les souches individuelles affectent les guildes et inversement via quorum sensing et cross-feeding (Coyte et al. 2015).                      |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
Le principal point de débat est H3 : le quatrième niveau (axe intestin-hôte) est-il intrinsèque au système « microbiome » ou extrinsèque ? Si l'on définit le système comme le microbiome seul (sans l'hôte), on obtient 3 niveaux nets. Si l'on inclut l'interface hôte-microbiome comme partie intégrante, on atteint 4. Le score de 0.5 reflète cette ambiguïté de délimitation.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Un traitement antibiotique ciblant un groupe bactérien donné entraîne la prolifération opportuniste d'autres modules (ex. expansion de Clostridioides difficile après élimination de compétiteurs). Costello et al. (2012) documentent ces cascades écologiques.                                              |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | La perte d'une souche clé (niveau souche) peut effondrer une guilde fonctionnelle entière (niveau guilde), puis modifier le profil communautaire global (niveau communauté). Exemple classique : perte de producteurs de butyrate → inflammation muqueuse → dysbiose globale.                                 |
| P3 : Propagation modifie l'état global observable             | 1     | Les transitions entre états stables (entérotypes, dysbiose vs. eubiose) sont documentées. Une perturbation suffisante peut faire basculer le système d'un attracteur à un autre, modifiant les profils métagénomiques mesurables (Costello et al. 2012).                                                      |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | Le réseau de cross-feeding et de compétition rend l'isolement partiel difficile (Coyte et al. 2015) mais pas impossible : certains modules sont relativement découplés (ex. méthanogènes archéens relativement indépendants). Le couplage est fort mais pas totalement inextricable.                          |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage repose sur des chaînes métaboliques complexes (cross-feeding en cascade), la compétition pour des substrats partagés, et des interactions signal-dépendantes (quorum sensing). Ce n'est pas un simple couplage linéaire mais un réseau d'interactions hautement non-linéaire (Coyte et al. 2015). |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
P4 à 0.5 plutôt que 1 : certains sous-modules (ex. archées méthanogènes, certains champignons) fonctionnent de manière relativement autonome. L'isolement total est difficile pour les réseaux bactériens centraux, mais les composantes périphériques peuvent être perturbées de manière plus locale. Le microbiome n'est pas un système monolithique — il a une structure modulaire partielle.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 0.5   | Le quorum sensing coordonne le comportement intra-espèce et parfois inter-espèce. Cependant, il n'y a pas de mécanisme centralisé de coordination pour l'ensemble de la communauté — la coordination est distribuée, émergente, et souvent indirecte (via métabolites partagés). Le caractère « explicite » est discutable.                                          |
| I2 : Réduction de variance observable    | 1     | La convergence fonctionnelle est bien documentée : des communautés taxonomiquement très différentes présentent des profils fonctionnels similaires (Turnbaugh et al. 2007 — concept de « core functional microbiome »). La variance taxonomique est forte mais la variance fonctionnelle est réduite.                                                                |
| I3 : Synchronisation multi-niveaux       | 0.5   | Il existe des rythmes circadiens du microbiome corrélés aux cycles alimentaires de l'hôte, mais la synchronisation entre niveaux (souche ↔ guilde ↔ communauté) est davantage une propriété émergente qu'un mécanisme actif de synchronisation. Pas de « chef d'orchestre » identifiable.                                                                            |
| I4 : Boucles de rétroaction globales     | 1     | Colonization resistance : la communauté établie produit des métabolites et occupe des niches qui inhibent l'invasion par des pathogènes (rétroaction communauté → souches). L'axe immunitaire muqueux fournit également une boucle globale (Costello et al. 2012).                                                                                                   |
| I5 : Maintien d'un état global cohérent  | 0.5   | Le microbiome maintient des « attracteurs » (entérotypes) mais avec une variabilité intra-individuelle significative au niveau taxonomique. La cohérence est fonctionnelle plutôt que compositionnelle. De plus, les perturbations majeures (antibiotiques) peuvent rompre cette cohérence durablement, suggérant que le maintien est conditionnel plutôt qu'absolu. |

**Score A3 = 0.70 / 1.00**

**Hésitations / ambiguïtés :**
L'intégration du microbiome est un point complexe. Le système montre une forte intégration fonctionnelle (convergence, colonization resistance) mais une intégration mécanistique plus faible (pas de coordinateur central, pas de signal global unique). I1 et I3 à 0.5 reflètent cette tension entre intégration émergente forte et coordination explicite limitée.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Les entérotypes (Arumugam et al., cité dans Costello et al. 2012) constituent des bassins d'attraction. Après perturbation, le microbiome tend à revenir vers une configuration stable (même si pas toujours identique à l'état initial).                                                                                     |
| N2 : Correction active d'écart               | 1     | Colonization resistance : prolifération compensatoire de commensaux face à un envahisseur ; compétition pour les niches qui ramène la communauté vers un profil fonctionnel « normal ». L'immunité muqueuse de l'hôte participe aussi à cette correction (IgA sécrétoires).                                                   |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Il existe une priorité implicite : la survie des espèces dominantes prime (par compétition), et la stabilité fonctionnelle globale émerge en second. Cependant, cette hiérarchie n'est pas « programmée » mais résulte de dynamiques écologiques. Le caractère hiérarchique est émergent, pas structurel.                     |
| N4 : Mécanisme interne de stabilisation      | 1     | La compétition et la coopération forment un réseau de stabilisation interne. Coyte et al. (2015) démontrent que la prédominance de compétition sur la coopération est paradoxalement stabilisatrice pour l'écosystème. Le cross-feeding crée des interdépendances stabilisantes.                                              |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le microbiome résiste à des perturbations modérées (changement alimentaire temporaire, infection aiguë) mais des perturbations prolongées (antibiotiques répétés, maladie chronique) peuvent le faire basculer durablement vers un état dysbiotique difficilement réversible. La résilience est réelle mais limitée en durée. |

**Score A4 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
N3 est délicat : y a-t-il réellement une hiérarchie de priorités, ou simplement une dynamique compétitive dont l'issue dépend des conditions ? La distinction entre « priorité régulatoire » et « résultat d'un rapport de forces » est subtile ici. N5 pose la question du seuil : le microbiome résiste bien aux perturbations courtes/modérées mais mal aux perturbations prolongées/sévères — le 0.5 reflète cette dualité.

**Distinction normativité endogène / imposée :**
Largement endogène. Les dynamiques de compétition, coopération et colonization resistance sont intrinsèques à l'écosystème microbien. Cependant, une composante significative de la normativité est imposée par l'hôte (immunité muqueuse, apport nutritionnel, pH gastrique, péristaltisme). Le microbiome ne « choisit » pas ses normes — elles émergent de la combinaison de ses dynamiques internes et des contraintes de l'hôte.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Les populations bactériennes ajustent leur expression génique en réponse aux conditions locales (disponibilité de substrats, pH, O₂). Régulation transcriptionnelle rapide et réversible documentée à grande échelle (métatranscriptomique).                                                                                                                                          |
| R2 : Modification durable de configuration interne | 1     | Changement alimentaire prolongé modifie durablement la composition du microbiome (abondances relatives). Un régime riche en fibres vs. riche en protéines animales produit des profils communautaires distincts et stables dans le temps (Turnbaugh et al. 2007).                                                                                                                     |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Le transfert horizontal de gènes (HGT) permet une reconfiguration structurelle du réseau métabolique communautaire. De nouvelles capacités métaboliques peuvent apparaître sans changement de composition taxonomique. La colonisation par de nouvelles espèces peut aussi reconfigurer le réseau d'interactions (Costello et al. 2012).                                              |
| R4 : Modification des mécanismes de régulation     | 0.5   | Le transfert horizontal peut introduire de nouveaux systèmes de quorum sensing ou de résistance, modifiant les mécanismes de régulation intercellulaire. Cependant, les mécanismes régulatoires fondamentaux (compétition, cross-feeding) restent qualitativement stables — ce qui change, ce sont les paramètres, pas les principes. Score de 0.5 car la modification est partielle. |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Le HGT et la mutation/sélection permettent l'émergence de nouvelles fonctions (ex. dégradation d'un xénobiotique nouveau). Cependant, le microbiome ne « conçoit » pas de nouvelles règles — il explore un espace de possibilités par variation et sélection. La capacité est réelle mais non dirigée, ce qui justifie un score partiel.                                              |

**Score A5 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
R4 et R5 posent la question de ce qui compte comme « modification de mécanisme de régulation » vs. « modification de paramètre dans un mécanisme existant ». Le HGT est un puissant levier de révision, mais il opère par variation aléatoire et sélection, pas par « décision » du système. Le microbiome est hautement plastique mais sa plasticité est non dirigée — ce qui le distingue d'un système à révision intentionnelle.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.90  |
| A2  | 0.90  |
| A3  | 0.70  |
| A4  | 0.80  |
| A5  | 0.80  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | +0.20  |
| Δ₄₅ = A4 − A5 | 0.00   |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | −0.10  |
| Δ₄₃ = A4 − A3 | +0.10  |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système biologique auto-organisé à intégration émergente
- **Régime secondaire :** Écosystème adaptatif à normativité partiellement exogène
- **Marge :** Le profil est remarquablement équilibré (scores 0.70–0.90), avec un « creux » relatif en intégration (A3), cohérent avec un système sans coordinateur central.
- **Surprise par rapport au jugement intuitif :** Le score A5 (plasticité) est peut-être plus élevé qu'attendu intuitivement — on pense au microbiome comme « stable » mais le HGT et la recomposition communautaire lui confèrent une plasticité remarquable. Le Δ₂₃ positif (+0.20) confirme l'intuition que la propagation est plus forte que l'intégration : le système propage bien les perturbations mais coordonne de manière émergente plutôt qu'explicite.

---

## Notes libres

Le microbiome intestinal humain est un cas d'étude fascinant pour ce cadre d'évaluation car il se situe à la frontière entre un « vrai » système autonome et un sous-système d'un système plus large (l'holobionte humain). Plusieurs scores (H3, N2, N5) sont sensibles à cette question de délimitation : inclut-on l'interface avec l'hôte ou non ?

Le Δ₄₅ nul est intéressant : la normativité et la plasticité sont parfaitement équilibrées, ce qui correspond à un système qui maintient des états stables tout en étant capable de se reconfigurer profondément — une propriété caractéristique des écosystèmes résilients.

Question ouverte : comment scorer un microbiome dysbiotique ? Les scores changeraient-ils significativement (probablement A3 et A4 diminueraient, A2 resterait élevé → augmentation de Δ₂₃) ?
