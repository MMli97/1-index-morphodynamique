# Scoring Notes — SYS008 Banque centrale européenne (ECB)

## Identification

- **System ID :** SYS008
- **System name :** Banque centrale européenne (European Central Bank)
- **Domain :** institutional
- **Subdomain :** monetary policy / central banking
- **Scale :** macro
- **Date scored :** 2026-03-09
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. ECB Annual Reports (multiple years)
2. Blanchard, O. — *Macroeconomics* (7th ed.)
3. Goodhart, C. — *The Central Bank and the Financial System*
4. Woodford, M. — *Interest and Prices: Foundations of a Theory of Monetary Policy*

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                           |
| --------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Conseil des gouverneurs → banques centrales nationales → banques commerciales : au moins deux niveaux causaux nets.                                                     |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Ajout du niveau marchés financiers / économie réelle qui réagit aux décisions relayées ; trois niveaux identifiables.                                                   |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | On peut distinguer Conseil → Directoire exécutif → BCN → système bancaire → économie réelle, mais la frontière entre certains niveaux (Directoire/Conseil) est poreuse. |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau a une fonction propre : délibération monétaire, exécution opérationnelle, supervision prudentielle (SSM), transmission au secteur bancaire.               |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Les données macro remontées par les BCN et les marchés informent les décisions du Conseil ; la causalité est clairement ascendante et descendante.                      |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** H3 à 0.5 — la distinction entre Conseil des gouverneurs et Directoire exécutif constitue-t-elle un niveau causal séparé ou une différenciation fonctionnelle au sein d'un même niveau ? Le Directoire exécute les décisions du Conseil, mais les deux siègent parfois ensemble. Le 4e niveau (économie réelle) est partiellement externe au système.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                             |
| ------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Un changement de taux directeur affecte simultanément le marché interbancaire, le crédit, le change, et les marchés obligataires.         |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Une décision du Conseil se propage aux BCN, puis aux banques, puis à l'économie réelle — traversant plusieurs niveaux.                    |
| P3 : Propagation modifie l'état global observable             | 1     | Les décisions de taux modifient l'inflation, le PIB, l'emploi à l'échelle de la zone euro : effet macro systémique.                       |
| P4 : Isolement difficile sans modification structurelle       | 1     | Un État membre ne peut s'isoler de la politique monétaire BCE sans quitter l'euro ; le couplage est structurel.                           |
| P5 : Couplage fonctionnel non trivial                         | 1     | Canaux de transmission complexes (taux, anticipations, crédit, change, bilan) avec effets non-linéaires et décalages temporels variables. |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Score maximal atteint. La BCE est un cas d'école de propagation systémique : chaque décision de taux se diffuse à l'ensemble de l'économie de la zone euro via de multiples canaux imbriqués. Aucune ambiguïté majeure.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                 |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Le Conseil des gouverneurs, le système TARGET, les opérations d'open market sont des mécanismes formels de coordination.                                      |
| I2 : Réduction de variance observable    | 1     | L'objectif d'inflation à 2 % réduit effectivement la variance des anticipations d'inflation dans la zone euro (ancrage).                                      |
| I3 : Synchronisation multi-niveaux       | 0.5   | La synchronisation existe (forward guidance, communication) mais reste imparfaite : décalages de transmission entre pays, hétérogénéité des cycles nationaux. |
| I4 : Boucles de rétroaction globales     | 1     | Projections macro → décisions → effets économiques → nouvelles données → révision : boucle rétroactive formalisée.                                            |
| I5 : Maintien d'un état global cohérent  | 0.5   | La cohérence est un objectif constant mais limité par l'hétérogénéité structurelle de la zone (spreads souverains, divergences Nord/Sud).                     |

**Score A3 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** I3 et I5 à 0.5 — la synchronisation multi-niveaux est réelle mais l'hétérogénéité structurelle de la zone euro (20 économies aux cycles désynchronisés) empêche une intégration parfaite. La politique monétaire unique face à des économies hétérogènes crée des tensions structurelles permanentes.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                  |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | La cible d'inflation à 2 % à moyen terme constitue un attracteur explicite, formalisé dans la stratégie monétaire.                             |
| N2 : Correction active d'écart               | 1     | Hausse des taux si inflation > cible, baisse si < cible, programmes d'achat d'actifs : correction active permanente.                           |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Stabilité des prix = objectif primaire (traité) ; stabilité financière et soutien à l'économie = objectifs secondaires : hiérarchie explicite. |
| N4 : Mécanisme interne de stabilisation      | 1     | Facilités permanentes (prêt marginal, dépôt), réserves obligatoires, ELA : stabilisateurs internes opérationnels en continu.                   |
| N5 : Résistance aux perturbations prolongées | 1     | La BCE a maintenu sa fonction à travers la crise de 2008, la crise des dettes souveraines, la pandémie — résilience démontrée.                 |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Score maximal atteint. La normativité est le point fort évident de la BCE : mandat traité, cible d'inflation explicite, instruments de correction permanents, résilience démontrée à travers plusieurs crises majeures.

**Distinction normativité endogène / imposée :** Mixte. Le mandat fondamental (stabilité des prix) est exogène (traité de Maastricht). Mais la BCE a développé de manière endogène ses normes opérationnelles : cible symétrique de 2 %, stratégie de communication, cadre des piliers. La normativité opérationnelle est largement auto-produite dans le cadre du mandat imposé.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                     |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Ajustements réguliers des taux directeurs, des volumes d'achat, des conditions de refinancement : paramétrage continu.                            |
| R2 : Modification durable de configuration interne | 1     | Passage aux taux négatifs (2014), programmes APP puis PEPP : reconfigurations durables du cadre opérationnel.                                     |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Création du SSM (2014), du SRB : restructurations majeures, mais initiées par le législateur européen plutôt que par la BCE seule.                |
| R4 : Modification des mécanismes de régulation     | 0.5   | La revue stratégique de 2021 a modifié la cible d'inflation (symétrique à 2 %). Mais le cadre traité de Maastricht reste exogène et contraignant. |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | La BCE innove (TLTRO, TPI, euro numérique) mais reste bornée par son mandat légal ; elle ne peut modifier les traités fondateurs.                 |

**Score A5 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** R3, R4, R5 à 0.5 — la BCE fait preuve d'innovation remarquable (taux négatifs, QE, TPI, euro numérique) mais sa plasticité structurelle reste bornée par un cadre juridique exogène (traités européens) qu'elle ne peut modifier. Les restructurations majeures (SSM, union bancaire) ont été co-produites avec le législateur, pas initiées unilatéralement.

---

## Synthèse

| Axe                          | Score |
| ---------------------------- | ----- |
| A1 — Profondeur hiérarchique | 0.90  |
| A2 — Capacité de propagation | 1.00  |
| A3 — Intégration             | 0.80  |
| A4 — Normativité             | 1.00  |
| A5 — Capacité de révision    | 0.70  |

### Gradients (calculés)

| Gradient      | Valeur | Interprétation                                                                        |
| ------------- | ------ | ------------------------------------------------------------------------------------- |
| Δ₂₃ = A2 − A3 | +0.20  | Propagation > Intégration : couplage fort, coordination imparfaite                    |
| Δ₄₅ = A4 − A5 | +0.30  | Normativité > Révision : système très normatif, plasticité contrainte par les traités |
| Δ₁₂ = A1 − A2 | −0.10  | Hiérarchie légèrement inférieure à la propagation                                     |
| Δ₃₅ = A3 − A5 | +0.10  | Intégration > Révision : coordination supérieure à la plasticité                      |
| Δ₄₃ = A4 − A3 | +0.20  | Normativité > Intégration : fort pilotage, cohérence imparfaite                       |

### Classification

- **Régime primaire :** Régulateur normatif à haute propagation — système institutionnel fortement couplé, piloté par des normes explicites, avec une intégration substantielle mais imparfaite.
- **Régime secondaire :** Système adaptatif contraint — plasticité notable mais structurellement limitée par le cadre juridique exogène des traités européens.
- **Marge :** Le gradient Δ₄₅ = +0.30 est le plus significatif : la BCE est bien plus normative que plastique. Ce décalage est cohérent avec une institution fondée sur un mandat juridique rigide.
- **Surprise par rapport au jugement intuitif :** Aucune surprise majeure. Le profil [0.90, 1.00, 0.80, 1.00, 0.70] confirme l'intuition d'un système très normatif et très propagé, avec une plasticité contrainte. L'intégration à 0.80 (et non 1.00) reflète bien la tension structurelle entre politique monétaire unique et hétérogénéité économique de la zone euro.

---

## Notes libres

- La BCE présente un profil caractéristique des institutions régulatrices macro : forte normativité, forte propagation, mais plasticité structurellement inférieure car le cadre constitutionnel est exogène.
- Le contraste avec la Fed américaine serait instructif : la Fed dispose d'un mandat dual (et non hiérarchisé) et opère dans une zone monétaire plus homogène, ce qui pourrait donner un A3 plus élevé et un A4 légèrement différent.
- Le programme TPI (Transmission Protection Instrument, 2022) est un cas fascinant de plasticité à la limite du mandat : la BCE crée un nouvel instrument pour résoudre un problème d'intégration (fragmentation), illustrant la tension entre R5 (innovation bornée) et I5 (cohérence imparfaite).
