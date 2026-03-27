# Scoring Notes — SYS017 Pipeline industriel (pétrolier)

## Identification

- **System ID :** SYS017
- **System name :** Pipeline pétrolier industriel (transport longue distance)
- **Domain :** infrastructure
- **Subdomain :** énergie / transport de fluides
- **Scale :** macro
- **Date scored :** 2026-03-10
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Mohitpour, M. — *Pipeline Design and Construction: A Practical Approach* (3rd ed., ASME Press)
2. Oil & Gas Engineering Manuals (API 1160, ASME B31.4, CSA Z662)
3. MIT Energy Initiative — Reports on pipeline infrastructure and energy transport systems

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveau physique (écoulement, pression, température du fluide) et niveau de contrôle (SCADA, vannes automatisées). Deux niveaux clairement distincts.                                                                                                                                       |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Ajout du niveau de supervision opérationnelle : centre de contrôle distant qui intègre les données SCADA et prend des décisions de routage, de maintenance, d'arrêt.                                                                                                                       |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5   | On peut identifier un 4e niveau (planification stratégique : allocation de capacité, scheduling des lots, gestion contractuelle), mais son couplage causal direct avec les niveaux inférieurs est médié par des opérateurs humains, ce qui affaiblit la profondeur strictement systémique. |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Chaque niveau a une fonction propre : physique → transport ; contrôle → régulation en temps réel ; supervision → coordination multi-stations ; planification → optimisation économique. Différenciation nette.                                                                             |
| H5 : Causalité bidirectionnelle entre niveaux | 0.5   | Le niveau physique remonte de l'information (capteurs de pression, débit, température) vers le contrôle, qui agit en retour (vannes, pompes). Mais la boucle entre supervision et planification est largement unidirectionnelle (top-down), avec un feedback lent et indirect.             |

**Score A1 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
La frontière entre niveau de contrôle local (station de pompage) et supervision distante (centre SCADA central) est parfois floue dans les installations plus anciennes où le contrôle est plus centralisé. Le 4e niveau (planification) est clairement présent mais son intégration causale directe est discutable — il opère souvent sur des échelles temporelles très différentes (jours/semaines vs secondes).

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une chute de pression à une station de pompage affecte immédiatement le débit en aval et peut déclencher des alarmes au centre de contrôle. Propagation hydraulique directe.                                                                                                                                     |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un événement physique (fuite, surpression) remonte au niveau contrôle (alarme SCADA) puis au niveau supervision (décision d'arrêt de section). Traversée claire de niveaux.                                                                                                                                      |
| P3 : Propagation modifie l'état global observable             | 1     | Un arrêt de section ou une fuite majeure modifie le débit total du pipeline, affecte les livraisons en bout de ligne, et change l'état opérationnel global (mode dégradé).                                                                                                                                       |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | Les vannes de sectionnement permettent d'isoler des segments, ce qui est précisément une modification structurelle prévue par conception. L'isolement est possible mais requiert une intervention active (fermeture de vannes, bypass). Le système est conçu pour permettre l'isolement, ce qui limite le score. |
| P5 : Couplage fonctionnel non trivial                         | 0.5   | Le couplage est principalement linéaire (série hydraulique). Il existe des non-linéarités (effets de coup de bélier, interactions thermiques fluide-paroi, slug flow), mais la topologie reste essentiellement séquentielle. Le couplage est réel mais moins complexe que dans un réseau maillé.                 |

**Score A2 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
P4 est le point le plus délicat : le pipeline est conçu avec des mécanismes d'isolement (vannes de sectionnement tous les X km), ce qui signifie que l'isolement est structurellement prévu. Cela réduit la "difficulté" d'isolement mais confirme que sans ces dispositifs, la propagation serait totale. P5 : le couplage est fort mais géométriquement simple (linéaire). Un réseau de pipelines interconnectés (grid) scorerait plus haut.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                                          |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Le système SCADA coordonne explicitement toutes les stations de pompage, vannes et instruments. Protocoles de communication standardisés, boucles de contrôle PID distribuées, coordination centralisée.                                                                               |
| I2 : Réduction de variance observable    | 1     | Les régulateurs de pression et de débit réduisent activement la variance : maintien de la pression dans une bande opérationnelle étroite (MOP — Maximum Operating Pressure), lissage des fluctuations de débit.                                                                        |
| I3 : Synchronisation multi-niveaux       | 0.5   | La synchronisation entre niveau physique et contrôle est excellente (temps réel). Mais la synchronisation avec le niveau de planification (batch scheduling, allocation de capacité) est asynchrone et souvent manuelle, avec des délais significatifs.                                |
| I4 : Boucles de rétroaction globales     | 0.5   | Il existe des boucles globales (mesure de débit en sortie comparée à l'injection, bilan matière sur l'ensemble du pipeline pour détection de fuite). Mais ces boucles sont lentes (minutes à heures) et souvent traitées comme des alarmes plutôt que comme des régulations continues. |
| I5 : Maintien d'un état global cohérent  | 1     | Le pipeline maintient un régime d'écoulement stable (steady-state hydraulique) qui constitue un état global cohérent. Les perturbations transitoires sont amorties par la dynamique du fluide et les régulateurs. Le système converge vers un profil de pression/débit stable.         |

**Score A3 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**
I3 et I4 reflètent une tension caractéristique des systèmes d'infrastructure : l'intégration est très forte au niveau physique-contrôle, mais plus faible quand on inclut les niveaux supérieurs (supervision humaine, planification). La question est de savoir si on évalue le pipeline comme système purement technique ou comme système sociotechnique. Ici, on privilégie le système technique avec ses interfaces humaines.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Le régime d'écoulement permanent (steady-state) est un attracteur clair : le système tend vers un profil de pression et débit stable défini par les conditions aux limites (pression d'injection, pression de livraison) et les caractéristiques du pipeline.                                                                |
| N2 : Correction active d'écart               | 1     | Les régulateurs PID corrigent activement les écarts de pression et de débit. Les stations de pompage ajustent leur puissance. Les vannes de contrôle modulent l'ouverture. Correction continue et automatisée.                                                                                                               |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Hiérarchie claire : (1) sécurité (surpression → arrêt d'urgence, ESD), (2) intégrité structurelle (limites de pression MOP), (3) performance opérationnelle (débit nominal), (4) efficacité énergétique. Les systèmes de sécurité préemptent les régulations de performance.                                                 |
| N4 : Mécanisme interne de stabilisation      | 1     | Multiples mécanismes : inertie du fluide (line-pack), compressibilité (pour gaz), régulateurs de pression, vannes de sûreté (PSV), systèmes de détection et arrêt automatique. La physique du fluide elle-même fournit un amortissement naturel.                                                                             |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le pipeline résiste bien aux perturbations courtes (fluctuations de demande, variations de composition). Mais face à des perturbations prolongées (corrosion, déformation du terrain, changement durable de conditions), le système se dégrade sans capacité de réparation autonome. La maintenance est entièrement exogène. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**
N5 est le point critique : le pipeline est très normatif à court terme mais dépend entièrement de la maintenance humaine pour sa normativité à long terme. Sans intervention, la corrosion, la fatigue et les mouvements de terrain dégradent le système de manière irréversible.

**Distinction normativité endogène / imposée :**
Mixte. La normativité physique (attracteur hydraulique, amortissement par inertie) est endogène. La normativité de contrôle (régulateurs, ESD) est conçue et imposée mais fonctionne de manière autonome une fois en place. La normativité de maintenance est entièrement imposée/exogène. Le score élevé reflète principalement les deux premiers types.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                       |
| -------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Les setpoints des régulateurs peuvent être modifiés (pression cible, débit cible, seuils d'alarme). Les stations de pompage peuvent ajuster leur point de fonctionnement. Ajustement paramétrique courant et opérationnel.                                                          |
| R2 : Modification durable de configuration interne | 0.5   | Possible mais lourd : ajout d'un racleur (pig) pour nettoyage, changement de type de produit transporté (batching), modification des séquences de pompage. Ces modifications sont durables mais requièrent une intervention externe et sont contraintes par la conception physique. |
| R3 : Reconfiguration de réseau ou de structure     | 0     | La topologie physique du pipeline est fixe. On ne peut pas re-router le fluide sans construire de nouvelles sections. Les vannes permettent d'isoler mais pas de reconfigurer. Rigidité structurelle inhérente à l'infrastructure enterrée.                                         |
| R4 : Modification des mécanismes de régulation     | 0.5   | Les algorithmes de contrôle SCADA peuvent être reprogrammés, les logiques d'alarme modifiées, de nouveaux capteurs ajoutés. Mais cela requiert une intervention d'ingénierie externe, ce n'est pas une capacité endogène du système.                                                |
| R5 : Capacité à produire de nouvelles règles       | 0     | Le pipeline ne génère pas de nouvelles règles de fonctionnement. Toute innovation régulatoire vient de l'extérieur (ingénieurs, mises à jour logicielles, nouvelles normes). Aucune plasticité endogène à ce niveau.                                                                |

**Score A5 = 0.40 / 1.00**

**Hésitations / ambiguïtés :**
R2 et R4 sont les points de discussion : le système peut être modifié, mais la question est de savoir si ces modifications sont « endogènes ». Un pipeline moderne avec SCADA avancé et capacité de mise à jour à distance est plus plastique qu'un ancien pipeline à contrôle manuel, mais dans les deux cas, la plasticité vient de l'extérieur du système. Le score de 0.5 pour R2 et R4 reflète la possibilité de modification sans reconstruction complète, même si l'initiative est exogène.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.80  |
| A2  | 0.80  |
| A3  | 0.80  |
| A4  | 0.90  |
| A5  | 0.40  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | +0.50  |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | +0.40  |
| Δ₄₃ = A4 − A3 | +0.10  |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Normatif-rigide — forte normativité (A4 = 0.90) avec faible plasticité (A5 = 0.40), gradient Δ₄₅ = +0.50 élevé.
- **Régime secondaire :** Intégré-propagatif — bonne intégration et propagation (A2 = A3 = 0.80), couplage équilibré.
- **Marge :** Le gradient Δ₄₅ = +0.50 est le trait dominant. Le système est fortement canalisé vers son régime nominal sans capacité d'adaptation structurelle.
- **Surprise par rapport au jugement intuitif :** Non. Le profil correspond à l'intuition d'un système d'infrastructure physique : très régulé, bien intégré, hiérarchiquement profond, mais structurellement rigide. Le score A4 élevé est attendu pour un système où la sécurité est critique. La faiblesse en A5 est caractéristique des infrastructures lourdes à topologie fixe.

---

## Notes libres

Le pipeline pétrolier est un cas paradigmatique de système d'infrastructure « normatif-rigide » : excellente régulation en temps réel, hiérarchie de contrôle claire, propagation maîtrisée, mais plasticité quasi nulle au niveau structurel. Le gradient Δ₄₅ = +0.50 capture bien cette asymétrie fondamentale.

Point intéressant : la comparaison avec un réseau de pipelines (grid) plutôt qu'un pipeline unique modifierait significativement A2 (couplage plus complexe, non-linéaire) et A5 (possibilité de re-routage). Le choix de l'unité d'analyse (pipeline unique vs réseau) est déterminant.

Le line-pack (stockage par compression dans le pipeline lui-même) est un phénomène remarquable qui contribue à la fois à A3 (intégration — état global cohérent) et A4 (normativité — stabilisation interne). C'est un cas où la physique du système fournit « gratuitement » des propriétés systémiques.

La dépendance totale à la maintenance exogène pour la normativité à long terme (N5 = 0.5) distingue nettement ce système des systèmes biologiques, qui maintiennent leur intégrité structurelle de manière endogène.
