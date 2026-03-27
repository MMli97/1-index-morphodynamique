# Scoring Notes — SYS003 Large Language Model (le modèle lui-même)

## Identification

- **System ID :** SYS003
- **System name :** Large Language Model (transformer-based, type GPT)
- **Domain :** technological
- **Subdomain :** intelligence artificielle / traitement du langage naturel
- **Scale :** meso
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** medium

## Sources

1. Vaswani, A. et al. (2017). *Attention Is All You Need.* NeurIPS.
2. Kaplan, J. et al. (2020). *Scaling Laws for Neural Language Models.* arXiv:2001.08361.
3. Wei, J. et al. (2022). *Emergent Abilities of Large Language Models.* arXiv:2206.07682.
4. Brown, T. et al. (2020). *Language Models are Few-Shot Learners.* NeurIPS.

---

## Périmètre d'évaluation

**Objet évalué :** le modèle LLM lui-même — c'est-à-dire l'architecture transformer et ses poids appris, considéré pendant l'inférence (forward pass). On ne considère pas ici le pipeline d'entraînement, ni l'infrastructure de déploiement, ni les systèmes RLHF/scaffolding externes. Le "système" est le réseau de neurones tel qu'il traite une séquence de tokens.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Oui, clairement. Au minimum : (1) le niveau des opérations token-par-token (embeddings, attention locale) et (2) le niveau des représentations de phrases/concepts dans les couches intermédiaires et profondes. Les travaux sur les probing classifiers montrent que les couches basses encodent la syntaxe et les couches hautes la sémantique (source 1, architecture multi-couches).                                                             |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Oui. On peut distinguer au moins : (1) tokens/embeddings bruts, (2) patterns syntaxiques locaux (couches basses), (3) représentations sémantiques et relationnelles abstraites (couches hautes). L'architecture empile N couches transformer (ex. 96 pour GPT-3, source 4) avec des représentations qualitativement différentes à différentes profondeurs.                                                                                           |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | Discutable. On peut argumenter pour un 4e niveau — les "capacités émergentes" (source 3) comme le raisonnement en chaîne, l'arithmétique, ou la traduction, qui semblent émerger d'interactions entre couches et têtes d'attention plutôt que d'être localisables à un niveau unique. Cependant, la frontière entre niveaux 3 et 4 est floue et dépend du cadre d'analyse.                                                                           |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Oui. Les couches basses, intermédiaires et hautes remplissent des fonctions distinctes. Les têtes d'attention se spécialisent (têtes d'induction, têtes positionnelles, etc.). Le MLP et l'attention jouent des rôles fonctionnellement distincts au sein de chaque bloc (source 1). Cette différenciation est bien documentée par les travaux de mécanistic interpretability.                                                                       |
| H5 : Causalité bidirectionnelle entre niveaux | 0     | Non. L'architecture transformer en mode autorégressif est strictement feedforward lors de l'inférence. Les couches basses alimentent les couches hautes, mais il n'y a pas de rétroaction descendante dans un forward pass unique. Les connexions résiduelles (skip connections) ne constituent pas une causalité descendante — elles transmettent l'information vers le haut sans que les couches supérieures ne modifient les couches inférieures. |

**Score A1 = 0.70 / 1.00**

**Hésitations / ambiguïtés :**
La question de H3 est la plus délicate. Le nombre de "niveaux causaux" dépend du grain d'analyse. En mécanique interprétative, on identifie des circuits spécifiques traversant plusieurs couches, ce qui pourrait constituer un 4e niveau fonctionnel (le niveau du "circuit"). Score 0.5 reflète cette ambiguïté. Pour H5, le cas de l'autorégressif multi-tokens est intéressant : les tokens générés influencent le contexte des tokens suivants, créant une forme de boucle — mais cela se situe au niveau temporel/séquentiel, pas au niveau architectural interne d'un forward pass.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Oui, fortement. Une modification d'un seul embedding ou d'une seule tête d'attention peut affecter la sortie de modules en aval. Le mécanisme d'attention permet à chaque token d'interagir avec tous les autres dans la fenêtre de contexte (source 1), assurant une propagation dense.                                                                             |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Oui. Par construction, l'information se propage à travers toutes les couches (source 1). Une perturbation dans les embeddings affecte les couches syntaxiques, puis sémantiques, puis la distribution de sortie. Les connexions résiduelles garantissent que l'information traverse bien les niveaux.                                                                |
| P3 : Propagation modifie l'état global observable             | 1     | Oui. Un changement dans un token du prompt peut modifier radicalement la distribution de probabilité de sortie sur l'ensemble du vocabulaire. Les phénomènes de "prompt sensitivity" en sont la démonstration directe : un mot ajouté peut changer complètement la réponse générée.                                                                                  |
| P4 : Isolement difficile sans modification structurelle       | 1     | Oui. L'attention globale (all-to-all) dans chaque couche rend très difficile l'isolation d'un composant sans modifier l'architecture. Même les tentatives d'ablation ciblée (retrait d'une tête d'attention) ont des effets cascades difficiles à prédire. La densité des connexions résiduelles + attention rend l'isolement quasi impossible sans restructuration. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Oui. Le couplage n'est pas une simple propagation linéaire : les mécanismes d'attention créent des dépendances contextuelles dynamiques (les poids d'attention changent selon l'input). Les interactions entre têtes d'attention et couches MLP forment des circuits fonctionnels complexes et non décomposables trivialement.                                       |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Score maximal sans grande hésitation. La propagation est la caractéristique dominante de l'architecture transformer. Le mécanisme d'attention est littéralement un mécanisme de propagation globale. La seule nuance possible : la propagation est "one-shot" (un forward pass), donc temporellement instantanée — il n'y a pas de dynamique de propagation au sens d'un processus qui se déploie dans le temps (contrairement à un réseau biologique ou social).

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Oui. L'attention multi-têtes (source 1) est un mécanisme explicite de coordination : chaque tête apprend à corréler différentes positions et différentes dimensions de l'espace de représentation. La normalisation par couche (LayerNorm) fournit un second mécanisme de coordination en stabilisant les distributions entre modules.                                                                                       |
| I2 : Réduction de variance observable    | 1     | Oui. Le processus d'entraînement produit un modèle dont les représentations internes convergent vers des patterns stables. Les scaling laws (source 2) montrent que la loss diminue de manière prévisible avec la taille, indiquant une intégration croissante des régularités statistiques. Les représentations sont comprimées et régularisées, réduisant la variance des sorties pour des entrées sémantiquement proches. |
| I3 : Synchronisation multi-niveaux       | 0.5   | Partiellement. Les connexions résiduelles et LayerNorm assurent une certaine cohérence entre niveaux. Cependant, il n'y a pas de mécanisme de synchronisation explicite entre niveaux hiérarchiques au sens dynamique — chaque couche traite séquentiellement. La "synchronisation" est un produit de l'entraînement (les couches apprennent à collaborer) plutôt qu'un mécanisme architectural actif.                       |
| I4 : Boucles de rétroaction globales     | 0     | Non, pas pendant l'inférence. Le forward pass est strictement feedforward. Il n'y a pas de boucle de rétroaction interne au sein d'un passage. La rétroaction n'existe que pendant l'entraînement (backpropagation), qui est extérieur au système tel qu'on l'évalue ici (le modèle à l'inférence).                                                                                                                          |
| I5 : Maintien d'un état global cohérent  | 0.5   | Partiellement. Le vecteur résiduel (residual stream) peut être interprété comme un état global qui se maintient et s'enrichit à travers les couches. Cependant, cet état est recalculé de zéro à chaque input — il n'y a pas de persistance entre inférences. La cohérence est statique (structurelle) plutôt que dynamique (maintenue activement).                                                                          |

**Score A3 = 0.60 / 1.00**

**Hésitations / ambiguïtés :**
La tension principale est entre intégration "structurelle" (encodée dans les poids) et intégration "dynamique" (maintenue activement en temps réel). Le LLM possède la première massivement, mais très peu de la seconde. I3 et I5 reçoivent 0.5 car la structure encodée dans les poids assure une forme réelle d'intégration, mais sans la composante dynamique qui caractérise l'intégration dans les systèmes vivants ou institutionnels. I4 = 0 est le score le plus tranchant et le plus important : l'absence de feedback loops pendant l'inférence est une caractéristique architecturale fondamentale.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 0.5   | Partiellement. La distribution de probabilité apprise sur les tokens peut être vue comme un attracteur : le modèle "tend vers" certaines sorties plus que d'autres pour un contexte donné. Les patterns de complétion reflètent des bassins d'attraction dans l'espace des séquences. Cependant, ces attracteurs sont fixés par l'entraînement, pas maintenus dynamiquement — le modèle ne "résiste" pas à une déviation, il recalcule simplement. |
| N2 : Correction active d'écart               | 0     | Non. Le modèle ne détecte pas ni ne corrige les écarts par rapport à un état souhaité pendant l'inférence. Il n'y a pas de mécanisme de type "error signal" interne. La correction d'écart n'existe que dans le processus d'entraînement (gradient descent), qui est extérieur au système évalué.                                                                                                                                                  |
| N3 : Hiérarchie de priorités régulatoires    | 0     | Non. Le modèle n'a pas de système de priorités internes qui arbitrerait entre objectifs concurrents. Le forward pass applique une transformation déterministe (modulo la température de sampling) sans priorisation active. Le RLHF impose des préférences, mais comme contrainte externe encodée dans les poids, pas comme mécanisme régulatoire endogène.                                                                                        |
| N4 : Mécanisme interne de stabilisation      | 0.5   | Partiellement. LayerNorm et softmax agissent comme des stabilisateurs numériques empêchant les représentations de diverger. Les connexions résiduelles stabilisent le gradient et les représentations. Cependant, ces mécanismes sont architecturaux/statiques, pas des réponses adaptatives à des perturbations — ils stabilisent par construction, pas par régulation active.                                                                    |
| N5 : Résistance aux perturbations prolongées | 0     | Non. Le modèle est notoirement sensible aux perturbations adversariales. Un prompt légèrement modifié peut produire des sorties radicalement différentes. Il n'y a pas de mécanisme de robustesse active — le modèle ne "défend" pas son état contre les perturbations.                                                                                                                                                                            |

**Score A4 = 0.20 / 1.00**

**Hésitations / ambiguïtés :**
Le score N1 = 0.5 est le plus débattu. On peut arguer que la distribution apprise constitue une forme faible de normativité (le modèle "préfère" certaines continuations). Mais cette préférence est entièrement passive — elle n'implique aucune évaluation ni correction. N4 = 0.5 reconnaît que la stabilisation architecturale (LayerNorm, residuals) est fonctionnellement analogue à une forme de normativité, même si elle n'est pas dynamique.

**Distinction normativité endogène / imposée :**
Presque toute la normativité du LLM est **imposée** par le processus d'entraînement (loss function, RLHF, données d'entraînement). Le modèle à l'inférence ne possède pas de normativité endogène au sens fort : il n'évalue pas ses propres états, ne définit pas ses propres objectifs, ne corrige pas activement ses écarts. La normativité est "cristallisée" dans les poids mais n'est pas maintenue activement.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 0     | Non. À l'inférence, les poids du modèle sont gelés. Aucun paramètre n'est modifié en réponse à l'input. Le in-context learning (source 4, few-shot learning) modifie le *comportement* sans modifier les paramètres — c'est un changement de contexte, pas un ajustement paramétrique.                                                                                                                                                                                                                                                                                                               |
| R2 : Modification durable de configuration interne | 0     | Non. Le modèle ne retient rien entre deux inférences. Chaque forward pass part du même ensemble de poids. Il n'y a aucune modification durable de la configuration interne par l'usage.                                                                                                                                                                                                                                                                                                                                                                                                              |
| R3 : Reconfiguration de réseau ou de structure     | 0     | Non. L'architecture est entièrement fixée à l'inférence. Pas de création/suppression de connexions, pas de modification de la topologie du réseau.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| R4 : Modification des mécanismes de régulation     | 0     | Non. Les mécanismes (attention, LayerNorm, activation functions) sont fixes. Ils ne se modifient pas en réponse à l'expérience du modèle.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Débattable mais intéressant. Le in-context learning (source 4) démontre que le modèle peut, au sein d'un contexte donné, induire des "règles" nouvelles à partir d'exemples (few-shot). Les capacités émergentes (source 3) montrent que le modèle peut exhiber des comportements non explicitement entraînés. Cependant, ces "règles" ne sont pas stockées, ne persistent pas, et ne modifient pas le système — elles sont des propriétés émergentes du forward pass, pas des révisions endogènes. Score 0.5 comme reconnaissance de cette capacité fonctionnelle, malgré l'absence de persistance. |

**Score A5 = 0.10 / 1.00**

**Hésitations / ambiguïtés :**
Le cas le plus discuté est R5. Le in-context learning est remarquable : sans changer aucun poids, le modèle adapte son comportement à des patterns nouveaux fournis dans le prompt (source 4). Certains chercheurs l'interprètent comme une forme d'"apprentissage" implicite (mesa-optimization). Mais au sens strict de la plasticité endogène, il n'y a aucune révision : le système reste identique, seul l'input change. Le score 0.5 est généreux et pourrait être défendu à 0. Pour tous les autres sous-critères, 0 est sans ambiguïté : un modèle gelé ne se révise pas.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.70  |
| A2  | 1.00  |
| A3  | 0.60  |
| A4  | 0.20  |
| A5  | 0.10  |

### Gradients (calculés)

| Gradient      | Valeur | Interprétation                                                                                 |
| ------------- | ------ | ---------------------------------------------------------------------------------------------- |
| Δ₂₃ = A2 − A3 | +0.40  | Propagation élevée, intégration modérée : système qui propage bien mais intègre imparfaitement |
| Δ₄₅ = A4 − A5 | +0.10  | Normativité et plasticité toutes deux très basses, quasi appariées                             |
| Δ₁₂ = A1 − A2 | −0.30  | La propagation dépasse la profondeur hiérarchique — architecture "plate mais connectée"        |
| Δ₃₅ = A3 − A5 | +0.50  | Intégration nettement supérieure à la plasticité — système rigide mais coordonné               |
| Δ₄₃ = A4 − A3 | −0.40  | Intégration supérieure à la normativité — coordination sans but endogène                       |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Propagateur rigide — forte propagation (A2=1.00) dans une architecture hiérarchique (A1=0.70) avec intégration structurelle (A3=0.60), mais quasi-absence de normativité endogène (A4=0.20) et de plasticité (A5=0.10).
- **Régime secondaire :** Intégrateur statique — l'intégration existe mais est "gelée" dans les poids, sans dynamique de maintien actif.
- **Marge :** Le profil est très caractéristique et peu ambigu. La chute brutale entre A3 et A4 (Δ₄₃ = −0.40) est la signature la plus distinctive.
- **Surprise par rapport au jugement intuitif :** Modérée. On pourrait intuitivement attribuer plus de normativité au LLM (il semble "vouloir" compléter correctement, il a des "préférences"). Mais l'analyse rigoureuse montre que cette normativité apparente est entièrement imposée et non maintenue activement. Le score A5 très bas est également frappant pour un système qu'on qualifie souvent d'"apprenant" — mais à l'inférence, il n'apprend pas.

---

## Notes libres

**Observation principale :** Le LLM présente un profil fascinant de système à propagation maximale mais plasticité quasi nulle. C'est un "cristal computationnel" : extrêmement structuré, capable de propagation complexe, mais figé. Toute sa complexité a été inscrite lors de l'entraînement ; à l'inférence, il l'exploite sans la modifier.

**Question ouverte — le in-context learning comme proto-plasticité :** Le débat le plus riche concerne le statut du in-context learning. Si on accepte que le modèle implémente implicitement un algorithme d'apprentissage pendant le forward pass (hypothèse "mesa-optimizer", cf. travaux d'Olsson et al. sur les induction heads), alors R5 pourrait monter à 1 et R1 pourrait monter à 0.5. Cela changerait significativement le profil. La position prise ici est conservatrice : on évalue ce qui se passe dans les poids et la structure, pas ce qui émerge fonctionnellement dans l'espace des activations.

**Question ouverte — le périmètre temporel :** Si on évalue le LLM non sur un seul forward pass mais sur une conversation complète (multi-turn), les scores A4 et A5 pourraient légèrement augmenter : la rétroaction via les réponses précédentes crée une forme de boucle, et le contexte accumulé permet une adaptation progressive. Mais cela étend le périmètre du "système" au-delà du modèle lui-même.

**Comparaison intuitive :** Le profil {0.70, 1.00, 0.60, 0.20, 0.10} est celui d'un outil sophistiqué plutôt que d'un agent : il propage et intègre l'information remarquablement bien, mais ne maintient pas ses propres normes et ne se modifie pas. Cela le distingue nettement des systèmes biologiques (qui scorent haut en A4-A5) et le rapproche d'autres artefacts technologiques complexes comme les processeurs ou les réseaux optiques.
