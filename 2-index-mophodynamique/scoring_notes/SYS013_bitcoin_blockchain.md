# Scoring Notes — SYS013 Blockchain (Bitcoin)

## Identification

- **System ID :** SYS013
- **System name :** Bitcoin Blockchain
- **Domain :** technological / economic
- **Subdomain :** registre distribué, cryptomonnaie
- **Scale :** macro
- **Date scored :** 2026-03-16
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Nakamoto S. — *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008)
2. Narayanan A. et al. — *Bitcoin and Cryptocurrency Technologies* (Princeton, 2016)
3. MIT Digital Currency Initiative — publications diverses

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveau 1 : transactions individuelles (UTXO, scripts). Niveau 2 : blocs assemblés par les mineurs, qui agrègent et ordonnent les transactions. Causalité claire : les transactions sont la matière première, le bloc les valide collectivement.                                                                                                                                                |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Niveau 3 : la chaîne elle-même comme séquence ordonnée de blocs, porteuse de l'état global (longest chain rule). La chaîne contraint quels blocs sont valides (hauteur, hash précédent), ce qui constitue un niveau causal supplémentaire agissant sur les niveaux inférieurs.                                                                                                                 |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | Niveau 4 candidat : le réseau de nœuds pair-à-pair (couche de propagation/gossip) et le protocole de consensus (règles de difficulté, format). On peut argumenter que le protocole constitue un méta-niveau contraignant la chaîne, mais il est largement statique et codé en dur, ce qui affaiblit sa distinction en tant que niveau causal actif.                                            |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les niveaux identifiés remplissent des fonctions clairement distinctes : création de valeur (transactions), ordonnancement/validation (blocs), mémoire/état global (chaîne), transport (réseau P2P). Pas de redondance fonctionnelle entre niveaux.                                                                                                                                            |
| H5 : Causalité bidirectionnelle entre niveaux | 0.5   | Causalité descendante partielle : la chaîne détermine quelles transactions sont confirmées, l'ajustement de difficulté (chaîne → mineurs) modifie le comportement du niveau bloc. Mais la rétroaction ascendante est limitée — les transactions n'influencent pas structurellement la chaîne au-delà de leur inclusion. L'influence bottom-up est principalement additive, pas transformative. |

**Score A1 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
Le statut du protocole comme niveau causal distinct est discutable. Il est codé dans le logiciel et ne se modifie que par fork (événement exogène au fonctionnement courant). On pourrait aussi considérer le mempool comme un sous-niveau intermédiaire entre transactions et blocs, mais il est davantage un buffer qu'un niveau causal propre.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une transaction double-spend ou un bloc invalide déclenche un rejet qui se propage aux nœuds voisins. Une variation du hashrate d'un mineur affecte la compétition globale pour le bloc suivant. La perturbation locale ne reste jamais confinée.                                                                      |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un fork temporaire (niveau bloc) modifie l'état de la chaîne (niveau supérieur) et invalide des transactions précédemment considérées confirmées (niveau inférieur). La propagation traverse bien les niveaux.                                                                                                         |
| P3 : Propagation modifie l'état global observable             | 1     | Un fork, une attaque 51 %, ou même un pic de volume de transactions modifie l'état global : UTXO set, hauteur de chaîne, difficulté, temps de confirmation moyen. L'état global est directement affecté par des perturbations locales.                                                                                 |
| P4 : Isolement difficile sans modification structurelle       | 1     | Par conception (réseau P2P, consensus distribué), il est impossible d'isoler un sous-ensemble du réseau sans partitionner physiquement le réseau ou modifier le protocole. Le couplage est constitutif de l'architecture.                                                                                              |
| P5 : Couplage fonctionnel non trivial                         | 0.5   | Le couplage est fort mais relativement mécanique : propagation par gossip protocol, validation par règles déterministes. Il y a peu de non-linéarité endogène — les effets sont largement proportionnels et prévisibles sauf en cas de fork ou d'attaque. Le couplage est robuste mais pas complexe au sens dynamique. |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
P5 est le point délicat. Le protocole Bitcoin est intentionnellement simple et déterministe. Les non-linéarités émergent principalement de la couche économique (incitations des mineurs, spéculation) qui est partiellement exogène au système technique stricto sensu. Si on inclut la couche économique, P5 monte à 1.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Le consensus Proof-of-Work est un mécanisme explicite de coordination : tous les nœuds suivent la même règle (longest valid chain) pour converger vers un état unique. C'est le cœur même du design de Nakamoto.                                                                                                                                        |
| I2 : Réduction de variance observable    | 1     | L'ajustement de difficulté toutes les 2016 blocs réduit activement la variance du temps inter-blocs autour de la cible de 10 minutes. Le consensus élimine les forks temporaires, réduisant la variance de l'état global.                                                                                                                               |
| I3 : Synchronisation multi-niveaux       | 0.5   | Les nœuds se synchronisent sur la chaîne (état global) et propagent les transactions (état local) de manière coordonnée. Cependant, la synchronisation est principalement unidirectionnelle (top-down : la chaîne impose l'état) et il n'y a pas de synchronisation fine entre sous-systèmes — c'est plutôt une convergence vers un référentiel unique. |
| I4 : Boucles de rétroaction globales     | 1     | L'ajustement de difficulté est une boucle de rétroaction négative globale classique : hashrate ↑ → difficulté ↑ → temps de bloc se stabilise. Le halving du reward est une boucle programmée qui modifie les incitations globales. Ces mécanismes opèrent sur l'ensemble du système.                                                                    |
| I5 : Maintien d'un état global cohérent  | 1     | C'est la raison d'être du système : maintenir un registre global cohérent (UTXO set) sans autorité centrale. Le consensus de Nakamoto garantit qu'en régime normal, tous les nœuds convergent vers le même état. La cohérence est la propriété fondamentale du système.                                                                                 |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
I3 reçoit 0.5 car la « synchronisation » dans Bitcoin est essentiellement une convergence passive vers un état unique plutôt qu'une coordination active entre sous-systèmes de nature différente. Il n'y a pas de négociation ou d'ajustement mutuel entre niveaux — le niveau supérieur (chaîne) dicte, les niveaux inférieurs se conforment.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Le système possède un attracteur clair : la chaîne la plus longue valide. Toute déviation (fork, bloc orphelin) est résorbée par convergence vers cet attracteur. Le temps inter-blocs de 10 min est un attracteur paramétrique maintenu par l'ajustement de difficulté.                                                                                                                 |
| N2 : Correction active d'écart               | 1     | L'ajustement de difficulté corrige activement l'écart entre temps de bloc observé et cible. Les nœuds rejettent activement les blocs et transactions invalides (correction par exclusion). Ces mécanismes opèrent sans intervention externe.                                                                                                                                             |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Il existe un ordonnancement implicite : validité cryptographique > règles de consensus > règles de relais (mempool policy). Cependant, cette hiérarchie est codée en dur et n'est pas dynamiquement arbitrée — il n'y a pas de mécanisme interne qui priorise entre objectifs concurrents en temps réel.                                                                                 |
| N4 : Mécanisme interne de stabilisation      | 1     | L'ajustement de difficulté est un stabilisateur endogène par excellence. Le mécanisme de frais (fee market) stabilise l'accès au bloc en situation de congestion. Le Proof-of-Work lui-même stabilise le système contre les attaques en rendant la manipulation coûteuse.                                                                                                                |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le système résiste bien aux perturbations techniques (panne de nœuds, variation de hashrate) grâce à l'ajustement de difficulté. Cependant, face à une perte prolongée de hashrate (>50 %), le système se dégrade significativement (temps de bloc très longs avant ajustement). Le halving crée aussi des chocs périodiques auxquels le système s'adapte mais pas toujours sans stress. |

**Score A4 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
N3 est le point le plus discutable. On peut argumenter que la hiérarchie de validation constitue une vraie hiérarchie normative, mais elle est entièrement statique et prédéterminée, ce qui limite son score.

**Distinction normativité endogène / imposée :**
Mixte. La normativité de Bitcoin est *conçue* (imposée par le protocole initial de Nakamoto) mais *maintenue endogènement* par les mécanismes de consensus sans autorité centrale. L'ajustement de difficulté et la validation par les nœuds sont pleinement endogènes dans leur fonctionnement, même si les règles qu'ils appliquent ont été fixées exogènement à la conception. C'est un cas intéressant de normativité imposée-puis-internalisée.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | L'ajustement de difficulté modifie un paramètre clé du système toutes les 2016 blocs de manière entièrement endogène. Les frais de transaction s'ajustent par le marché. Les nœuds individuels peuvent ajuster leurs politiques de relais (minrelaytxfee, etc.).                                                                                                                    |
| R2 : Modification durable de configuration interne | 0.5   | Les soft forks (SegWit, Taproot) modifient durablement la configuration, mais ils nécessitent un consensus social exogène au protocole. L'ajustement de difficulté modifie durablement la configuration, mais c'est un mécanisme pré-programmé, pas une adaptation émergente. Score intermédiaire : le résultat est durable, mais le mécanisme est soit pré-programmé soit exogène. |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | La topologie du réseau P2P se reconfigure dynamiquement (nœuds entrent/sortent, connexions changent). Cependant, la structure fondamentale du système (chaîne linéaire de blocs, PoW, règles de consensus) ne se reconfigure pas de manière endogène. Les changements structurels majeurs (hard forks) sont des événements exogènes impliquant coordination humaine.                |
| R4 : Modification des mécanismes de régulation     | 0     | Le mécanisme de régulation central (ajustement de difficulté, règles de validation, schedule de halving) ne se modifie pas lui-même. Il n'y a pas de méta-régulation endogène. Toute modification des règles nécessite un fork décidé par la communauté humaine. Le système n'a aucune capacité endogène à modifier ses propres mécanismes de régulation.                           |
| R5 : Capacité à produire de nouvelles règles       | 0     | Bitcoin ne produit pas de nouvelles règles de manière endogène. Toute nouvelle règle (nouveau type de transaction, nouvel opcode) nécessite une proposition humaine (BIP) et un déploiement par fork. Le système est, par conception, conservateur et résistant au changement — c'est une feature, pas un bug.                                                                      |

**Score A5 = 0.40 / 1.00**

**Hésitations / ambiguïtés :**
Le scoring de A5 dépend fortement de la frontière du système. Si on inclut la communauté de développeurs et le processus BIP comme partie du système, R4 et R5 montent significativement. Si on se limite au protocole et au réseau technique, le système est remarquablement rigide par conception. Nous avons retenu la frontière technique, car la communauté humaine n'est pas un composant endogène du système algorithmique.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.80  |
| A2  | 0.90  |
| A3  | 0.90  |
| A4  | 0.80  |
| A5  | 0.40  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | +0.40  |
| Δ₁₂ = A1 − A2 | −0.10  |
| Δ₃₅ = A3 − A5 | +0.50  |
| Δ₄₃ = A4 − A3 | −0.10  |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système normatif rigide — forte intégration et normativité, faible plasticité
- **Régime secondaire :** Système propagatif couplé — haute capacité de propagation avec intégration forte
- **Marge :** Le gradient Δ₄₅ = +0.40 est le signal dominant : le système régule fortement mais ne se révise presque pas. Δ₃₅ = +0.50 confirme : très intégré mais peu plastique.
- **Surprise par rapport au jugement intuitif :** Faible. Le profil correspond à l'intuition d'un système volontairement conservateur et rigide. La seule légère surprise est le score élevé en propagation (A2 = 0.90), qui reflète le couplage fort du réseau P2P souvent sous-estimé.

---

## Notes libres

Le profil de Bitcoin est cohérent avec son design philosophique : un système conçu pour être un « protocole ossifié » (terme utilisé par les développeurs Core). La rigidité en A5 n'est pas une faiblesse mais un choix architectural délibéré — la résistance au changement est la source de confiance du système.

Le gradient Δ₄₅ = +0.40 est caractéristique des systèmes technologiques à protocole fixe : ils régulent efficacement *dans* leurs règles mais ne peuvent pas modifier *les* règles elles-mêmes. Ce profil les distingue nettement des systèmes biologiques ou institutionnels adaptatifs.

Question ouverte : le processus de fork (soft et hard) constitue-t-il une forme de plasticité « au méta-niveau » ? Si oui, la frontière du système devrait être élargie pour inclure la gouvernance communautaire, ce qui modifierait significativement le scoring de A5 (probablement 0.60–0.70) mais aussi de A1 (ajout d'un niveau causal social/politique).
