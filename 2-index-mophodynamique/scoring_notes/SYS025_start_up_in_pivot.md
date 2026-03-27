# Scoring Notes — SYS025 Startup en phase de pivot (pré-Series A)

## Identification

- **System ID :** SYS025
- **System name :** Startup en phase de pivot (pré-Series A)
- **Domain :** economic / institutional
- **Subdomain :** entrepreneuriat organisationnel
- **Scale :** micro
- **Date scored :** 2026-03-17
- **Scorer :** —
- **Confidence globale :** medium

## Sources

1. Ries, E. — *The Lean Startup* (Crown Business, 2011). Sur le pivot comme mécanisme de révision structurelle : abandon du business model, reconfiguration du produit.
2. Blank, S. — *The Four Steps to the Epiphany* (K&S Ranch, 2005). Sur la phase de customer development : la startup cherche son modèle, toutes les règles sont provisoires.
3. Eisenhardt, K. & Martin, J. — "Dynamic capabilities: what are they?" in *Strategic Management Journal* 21, 2000. Sur la reconfiguration organisationnelle comme capacité.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                          |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveau fondateur/stratégie → niveau équipe/exécution clairement distingués. Les décisions stratégiques (pivot, roadmap) causent des changements d'exécution opérationnelle.                                            |
| H2 : ≥ 3 niveaux causaux distincts            | 0.5   | Un troisième niveau (marché/client) existe et influence la stratégie, mais son intégration causale formelle reste faible à ce stade pré-Series A ; les remontées clients ne constituent pas encore un niveau organisé. |
| H3 : ≥ 4 niveaux causaux distincts            | 0     | L'organisation est trop petite et trop fluide pour exhiber 4 niveaux causaux distincts et stables. La hiérarchie formelle est embryonnaire.                                                                            |
| H4 : Niveaux fonctionnellement différenciés   | 0.5   | Différenciation partielle : stratégie vs. produit vs. ops est reconnaissable, mais les rôles se chevauchent largement dans une startup pré-Series A (port de plusieurs casquettes).                                    |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Le feedback client remonte vers la stratégie (Blank : customer development), et la stratégie redesigne l'exécution. La boucle build-measure-learn (Ries) est structurellement bidirectionnelle.                        |

**Score A1 = 0.60 / 1.00**

*(Calcul : (1 + 0.5 + 0 + 0.5 + 1) / 5 = 3.0 / 5 = 0.60)*

**Hésitations / ambiguïtés :** H2 est borderline : le "niveau marché" est réel mais peu structuré comme niveau causal interne. H3 refusé car la structure reste aplatie — une startup de 5–15 personnes n'a pas de middle management distinct.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                            |
| ------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | La perte d'un client clé (module commercial) se propage immédiatement au module produit (repriorisation) et au module finances (runway). Couplage fort typique des petites structures.                                                                   |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Une décision opérationnelle (bug critique, départ d'un dev) remonte nécessairement au fondateur (niveau stratégique), qui doit arbitrer. La traversée de niveaux est quasi automatique.                                                                  |
| P3 : Propagation modifie l'état global observable             | 1     | Un pivot modifie le positionnement public, les métriques suivies, la roadmap et les recrutements en cours — état global observable radicalement changé (Ries : pivot = changement de direction structurelle).                                            |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | L'isolement d'un sous-système (ex. : mettre en pause le commercial) est possible mais coûteux et nécessite une reconfiguration explicite des rôles. Pas totalement impossible dans une petite équipe agile.                                              |
| P5 : Couplage fonctionnel non trivial                         | 0.5   | Le couplage existe mais est davantage dû à la taille (tout le monde dépend de tout le monde) qu'à une architecture fonctionnelle élaborée. Non trivial, mais la cause est la simplicité structurelle et non une interdépendance architecturale profonde. |

**Score A2 = 0.80 / 1.00**

*(Calcul : (1 + 1 + 1 + 0.5 + 0.5) / 5 = 4.0 / 5 = 0.80)*

**Hésitations / ambiguïtés :** P4 et P5 obtiennent 0.5 car la propagation forte est en partie un artefact de la petite taille, et non d'une architecture couplée sophistiquée. La distinction est analytiquement importante.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                        |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I1 : Mécanisme explicite de coordination | 0.5   | Des rituels de coordination existent (standup, réunion hebdo fondateurs) mais restent informels et non institutionnalisés. Mécanisme reconnaissable, non formalisé.                                                                  |
| I2 : Réduction de variance observable    | 0.5   | Le pivot lui-même est un acte d'intégration qui réduit la variance comportementale (tout le monde réaligne sur la nouvelle direction), mais en dehors des moments de pivot, la variance interne est élevée.                          |
| I3 : Synchronisation multi-niveaux       | 0.5   | La synchronisation fondateur/équipe/marché existe lors des moments clés (sprint reviews, pivot meetings) mais n'est pas continue. Elle est épisodique plutôt que structurelle.                                                       |
| I4 : Boucles de rétroaction globales     | 1     | La boucle build-measure-learn (Ries) est une boucle de rétroaction globale explicite qui relie produit, métriques et décision stratégique. C'est le cœur méthodologique du Lean Startup.                                             |
| I5 : Maintien d'un état global cohérent  | 0     | En phase de pivot, l'état global cohérent est précisément ce qui est remis en cause. La startup est par définition dans un état d'incohérence transitoire cherchant un nouvel attracteur (Blank : "searching for a business model"). |

**Score A3 = 0.50 / 1.00**

*(Calcul : (0.5 + 0.5 + 0.5 + 1 + 0) / 5 = 2.5 / 5 = 0.50)*

**Hésitations / ambiguïtés :** I5 est le critère le plus discriminant ici — la cohérence globale est structurellement absente en phase de pivot, ce qui pénalise A3. I4 compense avec la boucle build-measure-learn, qui est un des rares mécanismes globaux formellement théorisés.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                             |
| -------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 0.5   | Il existe un attracteur téléologique (le product-market fit), mais il n'est pas encore atteint et sa définition reste mouvante. L'attracteur est projeté, non stabilisé.                                  |
| N2 : Correction active d'écart               | 1     | Le pivot est précisément une correction active d'écart entre les métriques observées et la cible attendue. Ries : "validated learning" comme mécanisme de correction.                                     |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Une hiérarchie implicite existe (survie > croissance > optimisation ; runway > tout le reste), mais elle n'est pas formalisée. Elle opère par convention fondateur plutôt que par règle institutionnelle. |
| N4 : Mécanisme interne de stabilisation      | 0.5   | La culture d'équipe et la vision fondateur jouent un rôle stabilisateur partiel, mais ces mécanismes sont fragiles et personnalisés. Pas de processus institutionnel de stabilisation robuste.            |
| N5 : Résistance aux perturbations prolongées | 0     | La startup pré-Series A est notairement fragile aux perturbations prolongées (départ d'un cofondateur, perte de financement, churn client). La résistance est faible par définition du stade.             |

**Score A4 = 0.50 / 1.00**

*(Calcul : (0.5 + 1 + 0.5 + 0.5 + 0) / 5 = 2.5 / 5 = 0.50)*

**Hésitations / ambiguïtés :** N1 est délicat : l'attracteur PMF est réel comme cible normative, mais son instabilité pendant le pivot le rend difficile à scorer 1. N5 est le critère le plus défavorable — empiriquement, la majorité des startups à ce stade ne survivent pas à des perturbations prolongées (statistiques de mortalité startups pré-Series A).

**Distinction normativité endogène / imposée :** La normativité est principalement endogène (vision fondateur, métriques internes, culture lean) avec une composante exogène secondaire (pression investisseurs sur le runway, contraintes réglementaires mineures à ce stade). Le score reflète la normativité endogène, fragile mais présente.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                     |
| -------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Ajustements continus et rapides : pricing, onboarding, feature flags, messaging. La startup pré-Series A est précisément optimisée pour l'ajustement rapide de paramètres locaux (Ries : "tuning the engine").                                                    |
| R2 : Modification durable de configuration interne | 1     | Le pivot implique une modification durable : nouveau segment cible, nouveau stack technologique, nouvelle équipe de vente. Ces reconfigurations perdurent au-delà de l'événement déclencheur.                                                                     |
| R3 : Reconfiguration de réseau ou de structure     | 1     | La reconfiguration structurelle est le propre du pivot (Ries : pivot = changement de direction fondamentale). Peut inclure changement de canal de distribution, de partenaires, de modèle de revenus — toute la structure est susceptible d'être reconfigurée.    |
| R4 : Modification des mécanismes de régulation     | 1     | Après un pivot, les métriques suivies changent (ex. : de DAU à NPS, ou de croissance à rétention), ce qui constitue une modification des mécanismes de régulation eux-mêmes (Blank : les règles du customer development sont délibérément provisoires).           |
| R5 : Capacité à produire de nouvelles règles       | 1     | La startup en phase de pivot est explicitement dans un mode de production de nouvelles règles : nouvelles hypothèses, nouveau ICP, nouveau go-to-market. Eisenhardt & Martin : les dynamic capabilities permettent précisément de produire de nouvelles routines. |

**Score A5 = 1.00 / 1.00**

*(Calcul : (1 + 1 + 1 + 1 + 1) / 5 = 5.0 / 5 = 1.00)*

**Hésitations / ambiguïtés :** A5 = 1.00 est le score le plus robuste de l'évaluation — la plasticité endogène est la caractéristique définitoire du stade pivot. Aucun des 5 sous-critères ne fait débat. La seule nuance possible sur R2 serait que certaines reconfigurations durent moins longtemps qu'attendu (pivot sur pivot), mais le critère porte sur la capacité, non la stabilité de l'output.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.60  |
| A2  | 0.80  |
| A3  | 0.50  |
| A4  | 0.50  |
| A5  | 1.00  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | +0.30  |
| Δ₄₅ = A4 − A5 | −0.50  |
| Δ₁₂ = A1 − A2 | −0.20  |
| Δ₃₅ = A3 − A5 | −0.50  |
| Δ₄₃ = A4 − A3 | 0.00   |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Plasticité élevée / intégration faible (A5 >> A3)
- **Régime secondaire :** Propagation forte / normativité modérée (A2 > A4)
- **Marge :** Δ₄₅ = −0.50 et Δ₃₅ = −0.50 sont les gradients les plus saillants — écart maximal entre capacité de révision et stabilité (normative + intégrative)
- **Surprise par rapport au jugement intuitif :** A5 = 1.00 confirme l'intuition. La surprise est A4 = 0.50 (plus élevé qu'attendu pour un système "chaotique") : même en phase de pivot, la normativité opère via la cible PMF et la boucle de correction. A3 = 0.50 est la valeur la plus discriminante : l'intégration est structurellement limitée par le fait que la cohérence globale est en cours de reconstruction.

---

## Notes libres

**Profil général :** Le profil de la startup en pivot est asymétrique de façon caractéristique — très haute plasticité, propagation forte, mais intégration et normativité modérées, hiérarchie peu profonde. Ce profil est cohérent avec la littérature (Ries, Blank) qui présente la startup comme un système délibérément incomplet cherchant sa forme stable.

**Tension structurelle centrale :** Δ₄₅ = −0.50 exprime la tension fondamentale du stade pivot : le système est capable de se réviser bien plus vite qu'il n'est capable de se stabiliser. C'est fonctionnellement adaptatif à court terme, mais potentiellement pathologique si le gradient persiste au-delà du stade de recherche (scale-up prématuré, absence de process).

**Question ouverte :** Dans quelle mesure A5 = 1.00 est-il une compétence distincte de l'organisation ou un simple artefact de l'absence de rigidité structurelle ? La plasticité d'une startup pré-Series A pourrait être moins une "capacité" (au sens d'Eisenhardt & Martin) qu'une absence de contrainte. Cette distinction aurait des implications pour le scoring de systèmes comparables mais plus institués.

**Comparaison utile :** Ce profil (A5 >> A3, A4 modéré) devrait être mis en contraste avec une startup post-Series B ou une PME établie, où A3 et A4 augmentent significativement tandis que A5 tend à diminuer — phénomène de "ossification organisationnelle".
