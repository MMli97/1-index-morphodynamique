# Scoring Notes — SYS002 Global Supply Chain

## Identification

- **System ID :** SYS002
- **System name :** Global Supply Chain (réseau mondial d'approvisionnement)
- **Domain :** economic / infrastructure
- **Subdomain :** logistique, commerce international
- **Scale :** macro
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** medium

## Sources

1. Christopher, M. — *Logistics & Supply Chain Management* (Pearson).
2. Simchi-Levi, D., Kaminsky, P., Simchi-Levi, E. — *Designing and Managing the Supply Chain* (McGraw-Hill).
3. Helbing, D. — *Globally Networked Risks and How to Respond*, Nature (2013).
4. Ivanov, D., Dolgui, A. — *Viability of Intertwined Supply Networks*, Annals of Operations Research (2020).

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                          |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au minimum : fournisseur de matières premières → fabricant → distributeur. Deux niveaux causaux clairement distincts (extraction/transformation, transformation/distribution). [1][2]                                                                                  |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Tier-2 suppliers → Tier-1 suppliers → OEM → distributeurs → détaillants. Au moins trois strates causales indépendantes avec des dynamiques propres. [2]                                                                                                                |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | En ajoutant les couches régulatoires (douanes, normes, accords commerciaux) et les marchés financiers (couverture de change, lettres de crédit), on dépasse quatre niveaux. L'infrastructure logistique (ports, fret) forme un niveau supplémentaire. [1][3]           |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque strate remplit une fonction distincte : extraction, transformation, assemblage, logistique, distribution, finance, régulation. Les compétences et mécanismes causaux diffèrent radicalement d'un niveau à l'autre. [1][2]                                       |
| H5 : Causalité bidirectionnelle entre niveaux | 0.5   | La demande finale remonte vers les fournisseurs (effet bullwhip), et les contraintes amont (pénuries) se propagent vers l'aval. Toutefois, la bidirectionnalité est souvent retardée, déformée et incomplète — les signaux remontants sont notoirement bruités. [2][3] |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
H5 est le point délicat. L'effet bullwhip (Simchi-Levi) montre que la causalité remontante existe mais est amplifiée et distordue, ce qui questionne la qualité de la bidirectionnalité. Score 0.5 plutôt que 1 car la remontée d'information est systématiquement dégradée par rapport à la propagation descendante.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                       |
| ------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Cas d'école : une inondation dans une usine de semi-conducteurs en Thaïlande (2011) a perturbé l'automobile, l'électronique grand public et l'industrie informatique mondialement. [3][4]                                                           |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Les perturbations au niveau Tier-2 se propagent au Tier-1, puis à l'OEM, puis au marché final. La pandémie de 2020 a illustré une propagation traversant tous les niveaux simultanément. [3][4]                                                     |
| P3 : Propagation modifie l'état global observable             | 1     | Les disruptions majeures modifient les prix mondiaux, les délais de livraison agrégés, les indices PMI et les volumes de commerce international — tous des indicateurs d'état global. [3]                                                           |
| P4 : Isolement difficile sans modification structurelle       | 1     | Le découplage d'un fournisseur critique (ex. semi-conducteurs taïwanais) nécessite une restructuration massive : relocalisation, investissements en capacité, renégociation contractuelle. Le « decoupling » géopolitique en cours le démontre. [4] |
| P5 : Couplage fonctionnel non trivial                         | 1     | Les interdépendances sont non linéaires : flux physiques, flux financiers, flux informationnels, contraintes réglementaires et logistiques interagissent de manière complexe. Helbing décrit des « cascades de défaillances systémiques ». [3][4]   |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation majeure. La supply chain mondiale est un cas paradigmatique de propagation forte. Le seul débat possible concerne P3 : certaines perturbations restent contenues (disruptions mineures). Mais le critère demande si la propagation *peut* modifier l'état global, pas si elle le fait systématiquement — et les exemples empiriques sont abondants.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 0.5   | Il existe des mécanismes de coordination (EDI, contrats, plateformes de planification collaborative type S&OP), mais ils sont fragmentés. Aucun mécanisme unifié ne coordonne la supply chain *globale* — seulement des sous-réseaux. [1][2]                         |
| I2 : Réduction de variance observable    | 0.5   | Le JIT, le VMI et les systèmes de prévision partagée réduisent la variance localement. Mais l'effet bullwhip montre que la variance *augmente* en remontant la chaîne — échec partiel d'intégration. [2]                                                             |
| I3 : Synchronisation multi-niveaux       | 0.5   | Des synchronisations existent au sein de chaînes intégrées (ex. Toyota, Apple). Mais entre chaînes concurrentes et entre secteurs, la synchronisation est faible voire inexistante. Hétérogénéité forte. [1][2]                                                      |
| I4 : Boucles de rétroaction globales     | 0.5   | Les prix de marché et les indicateurs macroéconomiques agissent comme rétroaction globale, mais de manière indirecte et retardée. Pas de boucle de feedback architecturée au niveau du système entier. [3]                                                           |
| I5 : Maintien d'un état global cohérent  | 0     | La supply chain mondiale ne maintient pas d'état global cohérent. Elle oscille entre pénuries et surproduction, avec des déséquilibres structurels persistants (stocks régionaux, goulots d'étranglement). Ivanov parle de « viabilité » plutôt que d'équilibre. [4] |

**Score A3 = 0.40 / 1.00**

**Hésitations / ambiguïtés :**
I1 et I4 hésitation entre 0 et 0.5. On a retenu 0.5 car les mécanismes existent partiellement — mais ils ne couvrent pas le système dans sa globalité. I5 à 0 car le concept même d'« état global cohérent » est discutable pour ce système : il n'y a pas de variable d'état unique que le système chercherait à stabiliser collectivement.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                          |
| -------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 0.5   | Le système tend vers un équilibre offre-demande (attracteur économique), mais cet attracteur est instable, multi-modal et perturbé par les chocs exogènes. Ce n'est pas un attracteur robuste au sens dynamique fort. [2][3]           |
| N2 : Correction active d'écart               | 1     | Les mécanismes de prix, les ajustements de production, les réallocations logistiques corrigent activement les écarts entre offre et demande. Les acteurs individuels optimisent en permanence. [1][2]                                  |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Chaque acteur a sa propre hiérarchie (coût > délai > qualité, ou l'inverse). Il n'y a pas de hiérarchie partagée au niveau global, mais les régulations (douanes, sanctions, normes sanitaires) imposent des priorités partielles. [1] |
| N4 : Mécanisme interne de stabilisation      | 0.5   | Les stocks-tampons, les contrats long-terme, les assurances et la diversification des fournisseurs stabilisent partiellement. Mais ces mécanismes sont décentralisés et parfois contradictoires (JIT réduit les buffers). [2][4]       |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le système absorbe des chocs importants (pandémie, blocage du canal de Suez) et se réorganise, mais avec des délais longs et des dommages collatéraux significatifs. La résilience est réelle mais coûteuse et imparfaite. [3][4]      |

**Score A4 = 0.60 / 1.00**

**Hésitations / ambiguïtés :**
N2 est le critère le plus solide : la correction par les prix est un mécanisme bien documenté. N1 hésitation entre 0.5 et 1 — l'attracteur existe (équilibre de marché) mais il est si instable et sensible aux conditions initiales qu'on ne peut pas lui donner 1. N5 hésitation : le système a survécu à de nombreux chocs, mais « résistance » implique un maintien de fonctionnement que la supply chain ne garantit pas toujours (pénuries prolongées).

**Distinction normativité endogène / imposée :**
Mixte. La normativité endogène provient des dynamiques de marché (prix, concurrence, optimisation décentralisée). La normativité imposée provient des régulations étatiques (tarifs douaniers, sanctions, normes), des accords commerciaux (OMC, accords bilatéraux) et des standards industriels. Les deux couches interagissent et parfois se contredisent (ex. optimisation coût vs contraintes réglementaires environnementales).

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                            |
| -------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Les acteurs ajustent en continu leurs paramètres : prix, volumes de commande, niveaux de stock, choix de transporteurs. Réactivité paramétrique très élevée. [1][2]                                                                                      |
| R2 : Modification durable de configuration interne | 1     | Les entreprises changent de fournisseurs, relocalisent, réorganisent leurs entrepôts, adoptent de nouvelles technologies (automatisation, IoT). Ces changements sont durables et fréquents. [2][4]                                                       |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Des reconfigurations majeures ont lieu (nearshoring, friendshoring, diversification post-COVID), mais elles sont lentes, coûteuses et souvent incomplètes. La structure globale évolue, mais avec une forte inertie. [4]                                 |
| R4 : Modification des mécanismes de régulation     | 0.5   | Les régulations commerciales évoluent (nouveaux accords, sanctions, normes ESG), et les pratiques managériales changent (passage du JIT au JIC — Just in Case). Mais ces modifications sont exogènes (politiques) ou très graduelles (pratiques). [1][3] |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Le système génère de nouvelles normes (standards de traçabilité blockchain, certifications ESG, protocoles de résilience). Mais cette production est lente, fragmentée et souvent réactive plutôt que proactive. [4]                                     |

**Score A5 = 0.70 / 1.00**

**Hésitations / ambiguïtés :**
R3 hésitation entre 0.5 et 1. La reconfiguration post-COVID est réelle et significative, mais elle est encore en cours et sa profondeur reste incertaine. R5 hésitation : la supply chain « produit » des règles (standards, best practices), mais il est discutable que ce soit une propriété émergente du système plutôt que des décisions d'acteurs individuels ou d'institutions externes.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.90  |
| A2  | 1.00  |
| A3  | 0.40  |
| A4  | 0.60  |
| A5  | 0.70  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | +0.60  |
| Δ₄₅ = A4 − A5 | −0.10  |
| Δ₁₂ = A1 − A2 | −0.10  |
| Δ₃₅ = A3 − A5 | −0.30  |
| Δ₄₃ = A4 − A3 | +0.20  |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Propagatif-découplé — Le système propage massivement les perturbations (A2 = 1.00) mais sans intégration suffisante pour les contenir ou les coordonner (A3 = 0.40). Le gradient Δ₂₃ = +0.60 est le trait dominant du profil.
- **Régime secondaire :** Adaptatif-décentralisé — Bonne plasticité (A5 = 0.70) portée par les acteurs individuels plutôt que par le système comme tout. La normativité (A4 = 0.60) est suffisante pour maintenir un fonctionnement mais pas pour garantir la stabilité.
- **Marge :** Le déséquilibre A2 >> A3 constitue la vulnérabilité structurelle majeure : le système propage mieux qu'il n'intègre, ce qui explique les crises en cascade documentées par Helbing.
- **Surprise par rapport au jugement intuitif :** Modérée. Le score A3 est plus bas qu'attendu — on pense intuitivement la supply chain comme « intégrée » à cause du vocabulaire managérial (integrated supply chain), mais l'intégration réelle au niveau global est faible. Le score A1 élevé (0.90) est attendu. Le Δ₂₃ très élevé formalise bien l'intuition que la supply chain est « fragile par conception ».

---

## Notes libres

- Le système « Global Supply Chain » est un cas intéressant de complexité émergente sans architecte : personne ne l'a conçu comme un tout, et pourtant il exhibe des propriétés systémiques fortes (propagation, hiérarchie). C'est précisément l'absence de conception globale qui explique le déficit d'intégration (A3).
- La tension entre JIT (optimisation locale, réduction de buffers) et résilience (buffers, redondance) est un conflit normatif structurel qui apparaît dans le score A4 modéré.
- Le gradient Δ₃₅ = −0.30 est notable : le système est plus plastique qu'intégré, ce qui signifie que les reconfigurations se font de manière fragmentée, sans vision d'ensemble.
- La confiance est « medium » principalement à cause de la difficulté à délimiter le système. « Global Supply Chain » est une abstraction couvrant des réalités très hétérogènes (chaîne automobile vs chaîne alimentaire vs chaîne pharmaceutique). Les scores pourraient varier significativement selon le sous-secteur retenu.
