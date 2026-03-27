# Scoring Notes — SYS007 Internet Routing (BGP)

## Identification

- **System ID :** SYS007
- **System name :** Internet Routing (BGP)
- **Domain :** technological / infrastructure
- **Subdomain :** protocole de routage inter-domaines
- **Scale :** macro
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Huston, G. — BGP: Building Reliable Networks with the Border Gateway Protocol (O'Reilly).
2. Rekhter, Y., Li, T., Hares, S. — A Border Gateway Protocol 4 (BGP-4), RFC 4271 (IETF).
3. Varadhan, K., Govindan, R., Estrin, D. — Persistent Route Oscillations in Inter-Domain Routing, Computer Networks (1997).
4. RIPE NCC — Articles and operational analyses on Internet routing stability (RIPE Labs).

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                              |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au moins 2 niveaux causaux distincts : la couche des routeurs de bordure (peering) et la couche des politiques d'AS (Autonomous Systems) forment deux niveaux clairement séparés.                                                          |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | 3 niveaux : (1) sessions eBGP entre routeurs pairs, (2) décisions de routage intra-AS (iBGP, IGP), (3) politiques inter-domaines (accords de transit/peering). Cf. RFC 4271 et Huston ch. 4-6.                                             |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | Un 4e niveau peut être identifié (organismes de gouvernance : RIR, ICANN pour l'allocation de préfixes), mais son couplage causal direct avec le plan de données BGP est indirect et lent.                                                 |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les niveaux sont fonctionnellement différenciés : le plan de données (forwarding), le plan de contrôle (BGP decision process), et le plan de politique (route-maps, filtrage) ont chacun des mécanismes propres.                           |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Bidirectionnalité claire : les décisions de politique (top-down) modifient les annonces de routes, et les événements de convergence du plan de contrôle (bottom-up) déclenchent des réajustements de politique (route flap damping, etc.). |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
H3 : le 4e niveau (gouvernance) est réel mais faiblement couplé causalement au plan de données en temps réel. Son influence est lente (allocation de préfixes, politiques RPKI) plutôt qu'instantanée. Score 0.5 reflète cette ambiguïté.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une annonce de route erronée par un seul AS affecte immédiatement les tables de routage de multiples AS voisins. Exemples historiques abondants (Pakistan Telecom/YouTube 2008, etc.).                                                  |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | La propagation traverse les niveaux : un événement au niveau session eBGP modifie la table RIB locale, puis se propage via iBGP, puis est réannoncé en eBGP à d'autres AS — traversée de 2+ niveaux hiérarchiques.                      |
| P3 : Propagation modifie l'état global observable             | 1     | Une fuite de route ou un détournement peut modifier l'état global observable du routage Internet (affectant le trafic de millions d'utilisateurs). Varadhan et al. (1997) démontrent les oscillations persistantes à l'échelle globale. |
| P4 : Isolement difficile sans modification structurelle       | 1     | L'isolement d'une perturbation est structurellement difficile : BGP n'a pas de mécanisme natif de confinement. Le filtrage nécessite des modifications manuelles de configuration (prefix-lists, RPKI). Cf. analyses RIPE NCC.          |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage est non trivial : la décision de best-path d'un routeur dépend de multiples attributs (AS-PATH, LOCAL_PREF, MED) dont les interactions créent des effets émergents non linéaires (oscillations de Varadhan et al.).         |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation significative. BGP est un cas d'école de propagation non contenue : le système obtient le score maximal sur tous les sous-critères.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                  |
| ---------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Le protocole BGP lui-même est un mécanisme explicite de coordination : échange de messages UPDATE/KEEPALIVE entre pairs pour synchroniser les tables de routage (RFC 4271, section 4).                                                         |
| I2 : Réduction de variance observable    | 0.5   | BGP converge vers un état stable (réduction de variance), mais la convergence est lente et non garantie dans tous les cas. Les oscillations persistantes (Varadhan et al.) montrent une réduction de variance incomplète.                      |
| I3 : Synchronisation multi-niveaux       | 0.5   | La synchronisation multi-niveaux existe (iBGP synchronisé avec IGP, eBGP avec politiques) mais reste imparfaite : les incohérences transitoires entre niveaux sont fréquentes pendant la convergence.                                          |
| I4 : Boucles de rétroaction globales     | 0.5   | Des boucles de rétroaction globales existent (route flap damping, timer-based withdrawals), mais elles sont paramétriques et non adaptatives. Leur efficacité est limitée et parfois contre-productive (RFC 2439 puis dépréciée par RFC 7196). |
| I5 : Maintien d'un état global cohérent  | 0.5   | L'état global (table de routage Internet) est maintenu de manière cohérente en régime stationnaire, mais la cohérence est fragile : les partitions de routage, les boucles transitoires et les blackholes sont des phénomènes récurrents.      |

**Score A3 = 0.60 / 1.00**

**Hésitations / ambiguïtés :**
I2-I5 : BGP assure une intégration fonctionnelle, mais celle-ci est fragile et souvent incomplète. La convergence lente, les oscillations persistantes (Varadhan et al.) et l'absence de vision globale (chaque AS ne voit que ses voisins) limitent l'intégration. Les scores de 0.5 reflètent cette tension entre mécanismes existants et efficacité limitée.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                 |
| -------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | BGP possède un attracteur dynamique clair : l'état de convergence stable où toutes les tables de routage sont cohérentes et les best-paths sélectionnés selon l'algorithme de décision (RFC 4271, §9.1).                                                                      |
| N2 : Correction active d'écart               | 1     | Correction active d'écart : lorsqu'une route est retirée ou modifiée, BGP recalcule automatiquement le best-path et propage les corrections via UPDATE/WITHDRAW.                                                                                                              |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Une hiérarchie de priorités existe dans le decision process (LOCAL_PREF > AS_PATH length > MED > ...), mais c'est une hiérarchie imposée par la spécification, non émergente. L'opérateur peut la modifier, mais le protocole ne la réordonne pas seul.                       |
| N4 : Mécanisme interne de stabilisation      | 1     | Mécanismes internes de stabilisation : timers de hold-down, MRAI (Minimum Route Advertisement Interval), Graceful Restart (RFC 4724). Ces mécanismes limitent les oscillations et stabilisent le système.                                                                     |
| N5 : Résistance aux perturbations prolongées | 0.5   | Résistance partielle aux perturbations prolongées : BGP résiste aux pannes de liens (reconvergence), mais les attaques soutenues (détournement de préfixes, fuites de routes persistantes) peuvent déstabiliser le système durablement sans mécanisme endogène de résolution. |

**Score A4 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
N3 : la hiérarchie de priorités est spécifiée par la RFC, non émergente. C'est une normativité imposée par design. N5 : le système résiste aux perturbations ponctuelles mais pas aux attaques soutenues ciblant le plan de contrôle.

**Distinction normativité endogène / imposée :**
La normativité de BGP est largement imposée par spécification (RFC). Le decision process, les timers, et les règles de propagation sont définis extérieurement. Toutefois, l'attracteur dynamique (convergence vers un état stable) est une propriété émergente du système distribué, ce qui confère une dimension partiellement endogène à la normativité.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                              |
| -------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Ajustement paramétrique local omniprésent : modification de LOCAL_PREF, MED, weight, timers par les opérateurs sur chaque routeur. Le système intègre ces ajustements en temps réel.                                       |
| R2 : Modification durable de configuration interne | 0.5   | Modification durable possible (ajout de filtres, de communautés, de route-maps), mais ces modifications sont exogènes (faites par les opérateurs humains). BGP ne modifie pas sa propre configuration de manière autonome. |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | La topologie du réseau de sessions BGP peut être reconfigurée (ajout/retrait de peerings, route reflectors), mais encore une fois par intervention humaine. BGP ne restructure pas son réseau de sessions seul.            |
| R4 : Modification des mécanismes de régulation     | 0     | BGP ne modifie pas ses propres mécanismes de régulation. Le decision process, les timers, les règles de propagation sont fixes dans le protocole. Toute modification nécessite une mise à jour du logiciel ou de la RFC.   |
| R5 : Capacité à produire de nouvelles règles       | 0     | Aucune capacité endogène de production de nouvelles règles. L'évolution du protocole (RPKI, BGPsec, etc.) résulte de processus institutionnels externes (IETF), non du système BGP lui-même.                               |

**Score A5 = 0.40 / 1.00**

**Hésitations / ambiguïtés :**
R1 est à 1 car le système intègre les ajustements paramétriques en temps réel, même si ceux-ci sont initiés par l'opérateur. R2-R3 à 0.5 : les modifications sont possibles et effectives, mais toujours initiées de l'extérieur. R4-R5 à 0 : BGP ne peut ni modifier ses propres règles de fonctionnement ni en produire de nouvelles. C'est un protocole figé sans plasticité endogène profonde.

---

## Synthèse

| Axe                          | Score    |
| ---------------------------- | -------- |
| A1 — Profondeur hiérarchique | **0.90** |
| A2 — Capacité de propagation | **1.00** |
| A3 — Intégration             | **0.60** |
| A4 — Normativité             | **0.80** |
| A5 — Capacité de révision    | **0.40** |

### Gradients (calculés)

| Gradient      | Valeur    |
| ------------- | --------- |
| Δ₂₃ = A2 − A3 | **+0.40** |
| Δ₄₅ = A4 − A5 | **+0.40** |
| Δ₁₂ = A1 − A2 | **−0.10** |
| Δ₃₅ = A3 − A5 | **+0.20** |
| Δ₄₃ = A4 − A3 | **+0.20** |

### Classification

- **Régime primaire :** Système réactif-normatif — forte propagation, forte normativité, intégration modérée, faible plasticité.
- **Régime secondaire :** Infrastructure rigide — le Δ₄₅ élevé (+0.40) signale un système qui régule sans pouvoir se transformer.
- **Marge :** Δ₂₃ = +0.40 est le gradient le plus marqué, confirmant que la capacité de propagation dépasse largement l'intégration : le système propage plus qu'il ne coordonne.
- **Surprise par rapport au jugement intuitif :** Le score A2 = 1.00 (maximum) n'est pas surprenant pour BGP. La vraie surprise est le contraste entre A4 (0.80) et A5 (0.40) : BGP est normatif mais rigide, ce qui explique sa vulnérabilité structurelle aux évolutions (adoption lente de RPKI, BGPsec).

---

## Notes libres

BGP est un cas particulièrement intéressant pour le framework : c'est un système distribué sans autorité centrale, où la normativité émerge partiellement de la spécification protocolaire et partiellement de la dynamique collective. Le profil « forte propagation, faible plasticité » est caractéristique des infrastructures protocolaires d'Internet : elles résistent au changement (ossification) tout en étant vulnérables aux perturbations qui se propagent sans contrôle.

Question ouverte : l'adoption progressive de RPKI et l'émergence de propositions comme BGPsec pourraient-elles modifier le score A5 à terme ? Cela dépend de si l'on considère l'écosystème BGP+IETF comme un seul système (auquel cas la plasticité augmente) ou BGP seul comme objet d'étude (auquel cas il reste structurellement rigide).
