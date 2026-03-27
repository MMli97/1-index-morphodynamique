# Scoring Notes — SYS009 Wikipedia

## Identification

- **System ID :** SYS009
- **System name :** Wikipedia (English-language edition, prise comme cas paradigmatique)
- **Domain :** institutional / technological
- **Subdomain :** plateforme collaborative de production de connaissance
- **Scale :** macro
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Reagle, J. — *Good Faith Collaboration: The Culture of Wikipedia* (MIT Press).
2. Jemielniak, D. — *Common Knowledge? An Ethnography of Wikipedia* (Stanford University Press).
3. Halfaker, A., Geiger, R. S., Morgan, J., Riedl, J. — *The Rise and Decline of an Open Collaboration System*, American Behavioral Scientist (2013).
4. Kittur, A., Kraut, R. E. — *Harnessing the Wisdom of Crowds in Wikipedia: Quality Through Coordination*, CSCW (2008).

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au minimum deux niveaux nets : l'édition individuelle d'articles (niveau opérationnel) et la gouvernance communautaire via politiques/guidelines (niveau régulateur). L'action d'un contributeur est contrainte causalement par les règles produites au niveau supérieur. [1][2]                                                 |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Trois niveaux identifiables : (i) micro-éditions sur l'article, (ii) coordination au niveau du projet thématique / WikiProject, (iii) gouvernance globale (ArbCom, Wikimedia Foundation, politiques centrales). Chaque niveau a une causalité propre sur les niveaux adjacents. [2][4]                                           |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | On peut distinguer un quatrième niveau — l'infrastructure technique (MediaWiki, bots, filtres anti-abus) — qui contraint causalement tous les autres. Cependant, ce niveau est partiellement exogène (Wikimedia Foundation / développeurs), donc son statut de niveau « interne » est discutable. [3]                            |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau remplit une fonction distincte : production de contenu, coordination thématique, régulation normative, infrastructure technique. Les rôles ne sont pas interchangeables — un WikiProject ne fait pas le travail de l'ArbCom et vice versa. [2][4]                                                                  |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Bidirectionnalité forte : les politiques (haut) contraignent les éditions (bas), mais les pratiques émergentes des éditeurs remontent pour modifier les politiques (processus de RFC, propositions de guidelines). Halfaker et al. documentent comment les comportements de base modifient les mécanismes de gouvernance. [1][3] |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** Le principal point de friction est H3. L'infrastructure MediaWiki constitue-t-elle un niveau hiérarchique interne au système, ou un substrat exogène ? La Wikimedia Foundation est juridiquement distincte de la communauté éditrice. Score 0.5 reflète cette ambiguïté. On pourrait arguer que les bots, eux, sont endogènes (créés et opérés par des éditeurs), ce qui fractionne le niveau technique en deux sous-composantes.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Un vandalisme sur un article à haute visibilité déclenche des réponses dans le module anti-vandalisme (bots, patrouilleurs), peut entraîner une semi-protection (module administratif), et modifier les flux de la watchlist d'autres éditeurs. [3][4]                                                                           |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un conflit éditorial local peut escalader vers une médiation (WikiProject), puis vers l'ArbCom (gouvernance), puis entraîner un changement de politique. Kittur & Kraut documentent comment les conflits locaux sur la coordination affectent la qualité globale. [4]                                                            |
| P3 : Propagation modifie l'état global observable             | 0.5   | Certaines perturbations modifient l'état global (ex. : le scandale Essjay a provoqué un changement de politique d'identification). Mais la plupart des perturbations locales restent contenues — le système est vaste et la majorité des éditions n'affectent pas l'état global. Score 0.5 pour refléter cette asymétrie. [1][3] |
| P4 : Isolement difficile sans modification structurelle       | 1     | Halfaker et al. montrent que les mesures d'isolement (semi-protection, restrictions d'édition) constituent elles-mêmes des modifications structurelles. On ne peut pas isoler un article problématique sans changer les permissions, ce qui altère la structure d'accès du système. [3]                                          |
| P5 : Couplage fonctionnel non trivial                         | 1     | Les modules sont couplés de manière non triviale : le contenu est lié par hyperliens, catégories, modèles (templates) partagés. Modifier un template affecte potentiellement des milliers d'articles. Les décisions de suppression affectent la structure de navigation globale. [2][4]                                          |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** P3 est le point délicat. Wikipedia est un système massivement distribué où la plupart des perturbations sont absorbées localement. Les cas de propagation globale existent mais sont l'exception. Le score 0.5 capture cette dualité : capacité de propagation globale démontrée, mais non systématique.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Multiples mécanismes explicites : pages de discussion (Talk), WikiProjects, noticeboards (ANI, RSN, NPOV), systèmes de vote (AfD, RfA), templates de coordination. Reagle décrit en détail la culture de coordination délibérative. [1][4]                                                                           |
| I2 : Réduction de variance observable    | 1     | Les Manual of Style, guidelines de sourçage, et processus de featured article review réduisent activement la variance de qualité. Kittur & Kraut montrent empiriquement que la coordination explicite réduit la variance de qualité entre articles. [4]                                                              |
| I3 : Synchronisation multi-niveaux       | 0.5   | Synchronisation partielle : les WikiProjects tentent de synchroniser le travail éditorial de base avec les standards globaux, mais l'efficacité est inégale. Beaucoup de WikiProjects sont dormants. La synchronisation entre la Foundation et la communauté est souvent conflictuelle. [2][3]                       |
| I4 : Boucles de rétroaction globales     | 1     | Plusieurs boucles globales : les watchlists, les Recent Changes, les bots de patrouille, les métriques de qualité des articles (stub → GA → FA) constituent des boucles de rétroaction qui informent l'ensemble du système. La page Main Page amplifie certains signaux vers l'ensemble de la communauté. [3][4]     |
| I5 : Maintien d'un état global cohérent  | 0.5   | Wikipedia maintient une cohérence partielle : les cinq piliers et les politiques fondamentales assurent un cadre, mais la cohérence réelle entre articles est variable. Contradictions entre articles, niveaux de qualité très hétérogènes. Jemielniak documente les tensions entre cohérence locale et globale. [2] |

**Score A3 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** I3 et I5 sont les points faibles. La synchronisation multi-niveaux est un idéal rarement atteint — la taille du système rend la coordination parfaite impossible. L'état global « cohérent » est plutôt un état statistiquement stable qu'une cohérence stricte. Le score reflète cette distinction entre cohérence locale (forte) et globale (partielle).

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | L'encyclopédie « idéale » conforme aux cinq piliers (neutralité, vérifiabilité, pas de travail inédit, civilité, souplesse des règles) constitue un attracteur clair. Le système tend à revenir vers cet état après perturbation. [1]                                                                                        |
| N2 : Correction active d'écart               | 1     | Correction rapide et multi-modale : revert de vandalisme (secondes via bots), discussions de neutralité, processus AfD pour contenu hors-critères, blocage d'utilisateurs perturbateurs. Halfaker et al. documentent l'intensification des mécanismes de correction. [3]                                                     |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Hiérarchie explicite : les cinq piliers > les politiques > les guidelines > les essais. BLP (biographies de personnes vivantes) a priorité sur la plupart des autres considérations. La politique de vérifiabilité prime sur le consensus local. [1][2]                                                                      |
| N4 : Mécanisme interne de stabilisation      | 1     | Mécanismes robustes : semi-protection de pages, système de permissions graduelles (autoconfirmed → admin → bureaucrate → steward), bots automatisés, ArbCom comme instance de dernier recours. [2][3]                                                                                                                        |
| N5 : Résistance aux perturbations prolongées | 0.5   | Résistance démontrée à des perturbations ponctuelles (vandalisme massif, controverses médiatiques). Mais Halfaker et al. montrent une vulnérabilité systémique aux perturbations prolongées : le déclin de rétention des nouveaux contributeurs constitue une perturbation structurelle que le système peine à corriger. [3] |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** N5 est le point critique. Le système résiste bien aux perturbations exogènes, mais les perturbations endogènes lentes (bureaucratisation, hostilité envers les nouveaux) montrent les limites de la normativité. Le système corrige les écarts à ses normes mais a du mal à corriger les normes elles-mêmes quand elles deviennent dysfonctionnelles.

**Distinction normativité endogène / imposée :** Largement endogène. Les normes sont produites par la communauté via des processus délibératifs (RFC, votes, discussions). La Wikimedia Foundation impose très rarement des normes top-down (quelques exceptions : Terms of Use, politique sur les images de personnes vivantes). Reagle insiste sur le caractère auto-organisé de la normativité wikipédienne. La composante imposée est minoritaire mais existe.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1     | Ajustements constants : modification des seuils de semi-protection, paramétrage des bots, ajustement des critères d'admissibilité par domaine. Chaque WikiProject ajuste ses propres critères dans le cadre global. [2][4]                                                                                                                 |
| R2 : Modification durable de configuration interne | 1     | Le système a produit des modifications durables : création de nouveaux espaces de noms, introduction du système de patrouille, flagged revisions (sur certaines versions linguistiques), création de nouveaux rôles (reviewer, rollbacker). [2][3]                                                                                         |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Reconfigurations partielles : fusion/scission de WikiProjects, réorganisation des catégories, création de projets sœurs (Wiktionary, Commons). Mais la structure fondamentale (article + talk page + historique) n'a quasiment pas changé depuis le début. L'architecture de base est très rigide. [2]                                     |
| R4 : Modification des mécanismes de régulation     | 0.5   | Le système peut modifier ses propres mécanismes (création de l'ArbCom, modification des critères de RfA, introduction de bots de régulation). Mais Halfaker et al. documentent une trajectoire de rigidification : les mécanismes de régulation deviennent plus stricts mais rarement plus souples. La révision est unidirectionnelle. [3] |
| R5 : Capacité à produire de nouvelles règles       | 1     | Capacité démontrée et continue : Wikipedia produit régulièrement de nouvelles politiques et guidelines via des processus communautaires. Le corpus normatif a considérablement grossi depuis 2001. Reagle documente cette capacité d'auto-législation comme trait fondamental. [1][2]                                                      |

**Score A5 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** R3 et R4 révèlent une tension fondamentale. Wikipedia peut ajouter des règles et des mécanismes mais peine à modifier ses structures profondes ou à assouplir ses régulations. La plasticité est réelle mais asymétrique : forte en mode additif (créer de nouvelles normes, ajouter des couches), faible en mode soustractif (simplifier, défaire, restructurer). C'est le constat central de Halfaker et al.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.90  |
| A2  | 0.90  |
| A3  | 0.80  |
| A4  | 0.90  |
| A5  | 0.80  |

### Gradients (calculés)

| Gradient      | Valeur | Interprétation                                                                                                                                                |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Δ₂₃ = A2 − A3 | +0.10  | Propagation légèrement supérieure à l'intégration : le système propage bien les perturbations mais n'intègre pas parfaitement les réponses.                   |
| Δ₄₅ = A4 − A5 | +0.10  | Normativité légèrement supérieure à la plasticité : le système maintient mieux ses normes qu'il ne les révise — signature d'une tendance à la rigidification. |
| Δ₁₂ = A1 − A2 | 0.00   | Équilibre entre profondeur hiérarchique et propagation.                                                                                                       |
| Δ₃₅ = A3 − A5 | 0.00   | Équilibre entre intégration et plasticité.                                                                                                                    |
| Δ₄₃ = A4 − A3 | +0.10  | Normativité supérieure à l'intégration : le système est plus normatif qu'intégré — il sait ce qu'il veut être, mais n'y arrive pas uniformément.              |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système auto-organisé à normativité endogène forte
- **Régime secondaire :** Système en rigidification progressive (Δ₄₅ > 0, plasticité asymétrique)
- **Marge :** Scores serrés (0.80–0.90), profil remarquablement homogène pour un système de cette taille. Les axes faibles (A3, A5) ne descendent pas sous 0.80.
- **Surprise par rapport au jugement intuitif :** Modérée. L'intuition place souvent Wikipedia comme un système « chaotique » ou « anarchique ». Le scoring révèle au contraire un système fortement normé (A4 = 0.90) avec une hiérarchie profonde (A1 = 0.90). La surprise principale est la relative faiblesse de l'intégration (A3 = 0.80) — on pourrait s'attendre à plus de cohérence pour un projet aussi mature. C'est la taille qui explique ce plafond.

---

## Notes libres

**Observation principale :** Wikipedia est un cas remarquable de système institutionnel auto-organisé atteignant des scores élevés et homogènes sur les cinq axes. Le profil est celui d'un organisme social mature : fort en structure et en norme, légèrement plus faible en intégration globale et en plasticité.

**Tension fondamentale identifiée :** Le diagnostic de Halfaker et al. (2013) se lit directement dans le gradient Δ₄₅ = +0.10 : le système est meilleur pour maintenir ses normes que pour les réviser. Cette rigidification asymétrique est le principal risque systémique. Le système sait corriger les écarts aux normes (N2 = 1) mais peine à corriger les normes elles-mêmes quand elles deviennent contre-productives (R4 = 0.5).

**Question ouverte :** Comment interpréter la quasi-stagnation structurelle (R3 = 0.5) d'un système pourtant technologiquement capable de se transformer ? L'hypothèse est que la normativité forte (A4) agit comme frein à la plasticité structurelle (R3) — le coût social de la reconfiguration est rendu prohibitif par la densité normative accumulée. Ce serait un cas d'auto-limitation par excès de normativité.

**Comparaison heuristique :** Profil attendu très différent d'un système biologique (où A5 > A4 typiquement) et d'un système purement technologique (où A3 > A4). Wikipedia occupe une position intermédiaire caractéristique des systèmes institutionnels communautaires.
