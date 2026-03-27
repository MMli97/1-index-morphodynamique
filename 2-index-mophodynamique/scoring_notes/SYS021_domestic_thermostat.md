# Scoring Notes — SYS021 Thermostat domestique

## Identification

- **System ID :** SYS021
- **System name :** Thermostat domestique (boucle capteur–contrôleur–actionneur)
- **Domain :** technological
- **Subdomain :** contrôle thermique résidentiel
- **Scale :** micro
- **Date scored :** 2026-03-10
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Åström, K.J. & Murray, R.M. — *Feedback Systems: An Introduction for Scientists and Engineers*
2. Wiener, N. — *Cybernetics: Or Control and Communication in the Animal and the Machine*
3. Bejan, A. — *Advanced Engineering Thermodynamics*

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                     |
| --------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Deux niveaux clairs : (1) capteur de température / comparateur, (2) actionneur (chaudière/compresseur). Le capteur mesure, le contrôleur décide, l'actionneur exécute.                                                                                                            |
| H2 : ≥ 3 niveaux causaux distincts            | 0.5   | On peut distinguer capteur → contrôleur (logique on/off ou PID) → actionneur, soit trois niveaux. Toutefois le contrôleur reste un étage très mince, souvent un simple comparateur à seuil ; la distinction avec le capteur est parfois intégrée dans un même composant physique. |
| H3 : ≥ 4 niveaux causaux distincts            | 0     | Pas de quatrième niveau identifiable. Il n'y a pas de méta-régulation ni de couche de supervision interne au système.                                                                                                                                                             |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les fonctions sont clairement séparées : mesure (thermistance), décision (comparateur/logique de contrôle), action (relais + chaudière). Chaque niveau a un rôle causal distinct.                                                                                                 |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | La boucle fermée classique : l'actionneur modifie la température ambiante, qui est remesurée par le capteur, qui modifie la commande. C'est le paradigme même du feedback négatif (Åström & Murray, ch. 1).                                                                       |

**Score A1 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** La question principale porte sur H2. Dans un thermostat purement on/off, le « contrôleur » se réduit à un comparateur à hystérésis — fonctionnellement distinct du capteur, mais d'une minceur causale notable. Un thermostat PID offre un contrôleur plus substantiel. Score 0.5 retenu pour couvrir les deux cas.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une perturbation du capteur (dérive, déplacement) se propage directement au contrôleur puis à l'actionneur. Une perturbation de l'actionneur (panne chaudière) modifie la température lue par le capteur.                                                                                                                           |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | La propagation traverse systématiquement les niveaux : capteur → contrôleur → actionneur → environnement → capteur. C'est inhérent à la structure en boucle fermée.                                                                                                                                                                 |
| P3 : Propagation modifie l'état global observable             | 1     | Toute perturbation significative modifie la température ambiante effective, qui est l'unique variable d'état global du système.                                                                                                                                                                                                     |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | Dans un système aussi simple, on *peut* isoler un composant (couper le relais, débrancher le capteur), mais cela revient à ouvrir la boucle, c'est-à-dire à détruire la fonction même du système. L'isolement est donc trivialement possible en matériel, mais fonctionnellement destructif. Score 0.5 pour refléter cette tension. |
| P5 : Couplage fonctionnel non trivial                         | 0     | Le couplage est en réalité très trivial : c'est une boucle linéaire à un seul signal (température). Il n'y a pas de couplages croisés, de modes multiples, ni d'interactions non linéaires complexes entre sous-systèmes. Wiener lui-même utilise le thermostat comme exemple *élémentaire* de feedback.                            |

**Score A2 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** P4 est le point délicat. Le thermostat est un système à couplage sériel strict — l'isolement d'un maillon brise la chaîne, mais la chaîne elle-même est très courte. P5 à 0 : le couplage est canoniquement trivial pour la cybernétique.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                             |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Le signal d'erreur (écart entre consigne et mesure) est le mécanisme explicite de coordination. C'est le cœur du contrôle en boucle fermée (Åström & Murray).                                                             |
| I2 : Réduction de variance observable    | 1     | C'est la fonction première du thermostat : réduire la variance de la température ambiante par rapport à la consigne. Sans thermostat, la température fluctue largement ; avec, elle reste dans une bande étroite.         |
| I3 : Synchronisation multi-niveaux       | 0.5   | Il y a synchronisation entre capteur, contrôleur et actionneur au sens où ils opèrent en temps réel sur le même signal. Mais avec seulement 2–3 niveaux peu profonds, la « synchronisation multi-niveaux » reste modeste. |
| I4 : Boucles de rétroaction globales     | 1     | Le thermostat *est* une boucle de rétroaction globale. C'est sa définition même. La rétroaction négative est le seul mécanisme organisateur du système.                                                                   |
| I5 : Maintien d'un état global cohérent  | 1     | Le système maintient activement la température autour de la consigne. C'est un état global cohérent, stable, et observable.                                                                                               |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** I3 à 0.5 plutôt qu'à 1 : la synchronisation existe, mais le mot « multi-niveaux » implique une richesse hiérarchique que le thermostat ne possède pas vraiment. Dans un système à 2 niveaux effectifs, la synchronisation est quasi-automatique et peu informative.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1     | La température de consigne est un attracteur explicite du système. Le système tend vers cet état et y revient après perturbation.                                                                                                                                                                                                                                                    |
| N2 : Correction active d'écart               | 1     | C'est le mécanisme fondamental : le signal d'erreur déclenche l'action corrective (chauffer si trop froid, couper si trop chaud). Feedback négatif canonique.                                                                                                                                                                                                                        |
| N3 : Hiérarchie de priorités régulatoires    | 0     | Il n'y a qu'une seule variable régulée (température) et une seule consigne. Aucune hiérarchie de priorités, aucun arbitrage entre objectifs concurrents.                                                                                                                                                                                                                             |
| N4 : Mécanisme interne de stabilisation      | 1     | Le feedback négatif est par définition un mécanisme de stabilisation. Dans un thermostat PID, les composantes intégrale et dérivée ajoutent de la robustesse. Même un on/off avec hystérésis stabilise autour de la consigne.                                                                                                                                                        |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le thermostat résiste bien aux perturbations modérées (ouverture de fenêtre, variation de température extérieure) tant que l'actionneur a la capacité thermique suffisante. Mais face à des perturbations prolongées dépassant la capacité du système (grand froid extrême, panne partielle), il n'a aucun mécanisme adaptatif — il sature. Score 0.5 pour cette limite intrinsèque. |

**Score A4 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** N5 est sensible au dimensionnement. Un thermostat bien dimensionné pour son environnement résiste très bien ; un thermostat sous-dimensionné échoue. Le score reflète le cas générique.

**Distinction normativité endogène / imposée :** La normativité est entièrement **imposée**. La consigne est fixée par l'utilisateur humain, non générée par le système. Le thermostat n'a aucune préférence intrinsèque pour 20°C plutôt que 25°C. L'attracteur est paramétrique et exogène. Ceci est un trait définitoire des systèmes cybernétiques simples par opposition aux systèmes autopoïétiques (Wiener, ch. 4).

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 0.5   | Un thermostat classique ne s'ajuste pas seul. L'utilisateur change la consigne, mais ce n'est pas un ajustement *endogène*. Un thermostat PID avec auto-tuning pourrait scorer 1, mais le cas générique est 0.5 — la composante intégrale d'un PID peut être vue comme un micro-ajustement paramétrique interne. |
| R2 : Modification durable de configuration interne | 0     | Le thermostat classique ne modifie pas sa propre configuration. Pas de mémoire, pas d'apprentissage, pas de recalibration autonome.                                                                                                                                                                              |
| R3 : Reconfiguration de réseau ou de structure     | 0     | Architecture fixe. Le câblage capteur–contrôleur–actionneur est immuable. Aucune reconfiguration topologique possible de l'intérieur.                                                                                                                                                                            |
| R4 : Modification des mécanismes de régulation     | 0     | Le mécanisme de régulation (on/off ou PID) est câblé. Le thermostat ne peut pas passer de on/off à PID, ni modifier ses gains de manière autonome (sauf auto-tuning, cas marginal).                                                                                                                              |
| R5 : Capacité à produire de nouvelles règles       | 0     | Aucune. Le thermostat ne génère jamais de nouvelles règles de contrôle. Il applique indéfiniment la même logique.                                                                                                                                                                                                |

**Score A5 = 0.10 / 1.00**

**Hésitations / ambiguïtés :** R1 à 0.5 est le point le plus discutable. La composante intégrale d'un PID accumule de l'erreur et ajuste la sortie en conséquence — c'est un ajustement paramétrique minimal mais réel. Pour un thermostat purement on/off, R1 serait 0. Le score 0.5 couvre le spectre des implémentations courantes.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.70  |
| A2  | 0.70  |
| A3  | 0.90  |
| A4  | 0.70  |
| A5  | 0.10  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | −0.20  |
| Δ₄₅ = A4 − A5 | +0.60  |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | +0.80  |
| Δ₄₃ = A4 − A3 | −0.20  |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Régulateur rigide — forte intégration et normativité, plasticité quasi nulle
- **Régime secondaire :** Boucle cybernétique élémentaire
- **Marge :** Δ₄₅ = +0.60 et Δ₃₅ = +0.80 confirment un système qui régule bien mais n'apprend pas. Le découplage normativité/révision est le trait dominant.
- **Surprise par rapport au jugement intuitif :** Aucune. Le thermostat est le cas d'école du régulateur sans plasticité. Le score A3 élevé (0.90) confirme que l'intégration est le point fort du système — c'est littéralement une machine à intégrer un signal d'erreur. Le score A5 très bas (0.10) confirme l'absence presque totale de capacité adaptative endogène.

---

## Notes libres

Le thermostat domestique est un cas-test idéal pour calibrer la grille : il doit scorer modérément sur les axes structurels (A1, A2), fortement sur l'intégration (A3) et la normativité (A4), et très faiblement sur la révision (A5). Le profil obtenu — {0.70, 0.70, 0.90, 0.70, 0.10} — correspond exactement à cette attente.

Point théorique notable : la normativité du thermostat est *entièrement imposée* (consigne exogène), ce qui en fait un bon contraste avec des systèmes biologiques où la normativité émerge du fonctionnement même du système. Cette distinction endogène/imposée pourrait mériter un traitement plus fin dans les versions futures de la grille.

Le gradient Δ₃₅ = +0.80 est le plus élevé : c'est la signature d'un système qui coordonne efficacement ses composants mais n'a aucune capacité à se transformer. C'est exactement ce que Wiener décrit comme la limite des systèmes de premier ordre en cybernétique.
