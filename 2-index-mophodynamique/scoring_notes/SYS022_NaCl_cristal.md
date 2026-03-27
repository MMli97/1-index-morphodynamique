# Scoring Notes — SYS022 Cristal de sel (NaCl)

## Identification

- **System ID :** SYS022
- **System name :** Cristal de chlorure de sodium (NaCl) — monocristal idéal avec défauts ponctuels
- **Domain :** scientific
- **Subdomain :** physique du solide / chimie des matériaux
- **Scale :** micro (réseau atomique → domaine cristallin)
- **Date scored :** 2026-03-17
- **Scorer :** —
- **Confidence globale :** high

## Sources

1. Kittel, C. — *Introduction to Solid State Physics* (Wiley, 8e éd.). Chapitres 1-3 : structure cristalline, défauts ponctuels, stabilité du réseau.
2. Ashcroft, N. & Mermin, N. — *Solid State Physics* (Holt). Chapitres cohésion, phonons, défauts.
3. Hull, D. & Bacon, D.J. — *Introduction to Dislocations* (Butterworth-Heinemann). Plasticité cristalline, limites de révision structurelle.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Niveau atomique (ions Na⁺/Cl⁻, liaisons ioniques) → niveau mésoscopique (maille cubique, domaine cristallin). Deux niveaux causaux clairement distincts.                                                                                                                                      |
| H2 : ≥ 3 niveaux causaux distincts            | 0.5   | On peut distinguer : électronique (nuage ionique, répulsion de Pauli) → atomique (position d'équilibre, potentiel de Madelung) → réseau (phonons, maille). Le troisième niveau est physiquement réel mais faiblement différencié fonctionnellement du second dans un cristal simple.          |
| H3 : ≥ 4 niveaux causaux distincts            | 0     | Un quatrième niveau causal autonome (ex. domaines, grain boundaries actifs) n'est pas constitutif du monocristal NaCl idéal ; il apparaît seulement dans les polycristaux ou sous contrainte sévère.                                                                                          |
| H4 : Niveaux fonctionnellement différenciés   | 0.5   | Le niveau électronique (cohésion), le niveau atomique (positions d'équilibre, défauts de Schottky/Frenkel) et le niveau réseau (modes normaux, phonons) ont des fonctions causales distinctes, mais le système reste très homogène : pas de spécialisation fonctionnelle forte entre niveaux. |
| H5 : Causalité bidirectionnelle entre niveaux | 0.5   | Les phonons (niveau réseau) modifient les positions moyennes des ions (niveau atomique), qui en retour définissent le spectre phonon. La bidirectionnalité existe mais elle est de nature thermodynamique passive, non régulative.                                                            |

**Score A1 = 0.50 / 1.00**

*(Somme brute : 2.5 pts sur 5 sous-critères → normalisé 0.50)*

**Hésitations / ambiguïtés :** H2 est borderline : le niveau électronique est bien distinct physiquement mais il ne constitue pas un niveau *causal autonome* au sens fort dans les conditions standard (T ambiante, pas d'excitation). Accordé 0.5 plutôt que 1 pour cette raison.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Un défaut ponctuel (lacune, ion interstitiel) perturbe le champ électrique local, modifie les fréquences phonon voisines et déplace les ions adjacents. Propagation immédiate vers au moins un autre « module » (thermique, élastique).                                                                      |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un phonon acoustique généré localement traverse le réseau entier (niveau atomique → niveau mésoscopique). Les ondes élastiques se propagent à longue portée.                                                                                                                                                 |
| P3 : Propagation modifie l'état global observable             | 1     | Une fissure de clivage ou une montée en température due à un choc phonon modifie des propriétés globales mesurables (transmittance optique, conductivité thermique, forme macroscopique).                                                                                                                    |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | On ne peut pas « isoler » un défaut ponctuel sans modifier la structure (recuit, dopage). En revanche, NaCl étant un milieu très ordonné, la propagation d'une perturbation s'atténue rapidement (faible anharmonicité à T ambiante) ; un isolement fonctionnel partiel est donc possible sans intervention. |
| P5 : Couplage fonctionnel non trivial                         | 0.5   | Le couplage phonon-phonon (anharmonicité), le couplage phonon-défaut et l'effet piézoélectrique nul de NaCl (centrosymétrique) indiquent un couplage modéré. Non trivial pour les phonons optiques/acoustiques, mais moins riche que dans les systèmes multicomposants.                                      |

**Score A2 = 0.80 / 1.00**

*(Somme brute : 4.0 / 5 → normalisé 0.80)*

**Hésitations / ambiguïtés :** P4 accordé 0.5 car la propagation s'amortit naturellement dans un cristal peu anharmonique, ce qui constitue une forme d'auto-isolement sans modification structurelle.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 0.5   | Le potentiel de Madelung coordonne implicitement toutes les positions ioniques : chaque ion est contraint par la somme de toutes les interactions coulombiennes. Mécanisme réel mais purement passif/structural, non dynamique au sens d'un coordinateur actif.       |
| I2 : Réduction de variance observable    | 1     | La symétrie cubique face centrée impose une variance quasi nulle sur les positions d'équilibre : à T ≈ 0 K, les ions occupent des sites déterministes. Même à T ambiante, la variance thermique est petite (Debye-Waller). Réduction de variance très forte.          |
| I3 : Synchronisation multi-niveaux       | 0.5   | Les phonons constituent une forme de synchronisation collective des vibrations ioniques sur l'ensemble du réseau. Cependant, cette synchronisation est cohérente seulement à basse T (longueur de cohérence phonon) ; à T ambiante, la synchronisation est partielle. |
| I4 : Boucles de rétroaction globales     | 0     | Il n'existe pas de boucle de rétroaction globale au sens dynamique : NaCl ne possède pas de mécanisme interne qui détecte un écart et envoie un signal correctif à l'ensemble du réseau. Les interactions sont locales et s'additionnent sans boucle globale.         |
| I5 : Maintien d'un état global cohérent  | 1     | Le cristal maintient sa structure cubique Fm3̄m de manière robuste sur de longues durées en conditions normales. L'état global cohérent (réseau périodique) est maintenu par l'énergie de cohésion ionique.                                                           |

**Score A3 = 0.60 / 1.00**

*(Somme brute : 3.0 / 5 → normalisé 0.60)*

**Hésitations / ambiguïtés :** I4 = 0 est la décision la plus tranchée : aucune boucle de rétroaction globale n'opère dans NaCl. I1 est difficile : le potentiel de Madelung « coordonne » mais de façon entièrement passive.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                      |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1     | La configuration Fm3̄m est un minimum d'énergie libre de Gibbs : c'est un attracteur thermodynamique robuste. Toute perturbation modérée ramène le système vers cet état (dans le bassin d'attraction).                                                            |
| N2 : Correction active d'écart               | 0     | Il n'y a pas de correction *active* : NaCl ne « détecte » pas un écart et n'envoie pas de signal correctif. Le retour à l'équilibre est purement passif (forces de rappel élastiques, relaxation thermique).                                                       |
| N3 : Hiérarchie de priorités régulatoires    | 0     | Aucune hiérarchie de priorités n'est implémentée : toutes les interactions ioniques sont de même nature (coulombienne + répulsion). Pas de sous-système qui aurait priorité sur un autre.                                                                          |
| N4 : Mécanisme interne de stabilisation      | 1     | Les forces de rappel élastiques (constantes de force de réseau) constituent un mécanisme interne de stabilisation : tout déplacement ionique génère une force de rappel proportionnelle. Mécanisme clair, documenté par Kittel ch. 3.                              |
| N5 : Résistance aux perturbations prolongées | 0.5   | NaCl résiste bien aux perturbations mécaniques modérées et thermiques jusqu'à ~600°C (transition de phase). Cependant, la dissolution progressive dans l'eau ou la fatigue mécanique (dislocations cumulatives) montrent une résistance limitée sur le long terme. |

**Score A4 = 0.50 / 1.00**

*(Somme brute : 2.5 / 5 → normalisé 0.50)*

**Hésitations / ambiguïtés :** N2 = 0 est central : la distinction entre correction *active* et retour passif vers un attracteur est cruciale ici. NaCl illustre parfaitement la normativité purement endogène-passive.

**Distinction normativité endogène / imposée :** La normativité est entièrement **endogène** (dérive de la structure électronique et du potentiel ionique) ; aucune norme n'est imposée de l'extérieur. C'est un cas-limite pur de normativité physique intrinsèque sans agentivité.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                          |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 0.5   | Les défauts de Schottky (lacunes) et de Frenkel (ions interstitiels) constituent des ajustements locaux spontanés en réponse à T ou à une contrainte chimique. Mais ces ajustements sont statistiques/thermodynamiques, non dirigés.                   |
| R2 : Modification durable de configuration interne | 0.5   | L'introduction de dopants (ex. Ca²⁺ substituant Na⁺) ou d'irradiation crée des modifications durables de la configuration locale. Cependant, dans le cristal pur, ces modifications ne sont pas endogènes ; elles requièrent une intervention externe. |
| R3 : Reconfiguration de réseau ou de structure     | 0     | NaCl ne se reconfigure pas spontanément : aucune reconfiguration topologique du réseau n'est possible sans apport d'énergie externe significatif (fusion, dissolution, haute pression vers la phase B2).                                               |
| R4 : Modification des mécanismes de régulation     | 0     | Les mécanismes de stabilisation (forces de rappel élastiques, potentiel de Madelung) sont invariants : NaCl ne peut pas modifier ses propres constantes de force de manière endogène.                                                                  |
| R5 : Capacité à produire de nouvelles règles       | 0     | Aucune capacité à générer de nouvelles règles structurelles ou fonctionnelles. La stœchiométrie et la symétrie sont fixées par la physique fondamentale des ions Na⁺ et Cl⁻.                                                                           |

**Score A5 = 0.20 / 1.00**

*(Somme brute : 1.0 / 5 → normalisé 0.20)*

**Hésitations / ambiguïtés :** R1 et R2 sont accordés 0.5 en reconnaissant que la thermodynamique des défauts constitue une forme minimale de plasticité endogène, mais sans aucune directionnalité ni finalité. Hull & Bacon (ch. sur la plasticité NaCl) confirment que le glissement de dislocations est possible mais nécessite une contrainte externe.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.50  |
| A2  | 0.80  |
| A3  | 0.60  |
| A4  | 0.50  |
| A5  | 0.20  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | +0.20  |
| Δ₄₅ = A4 − A5 | +0.30  |
| Δ₁₂ = A1 − A2 | −0.30  |
| Δ₃₅ = A3 − A5 | +0.40  |
| Δ₄₃ = A4 − A3 | −0.10  |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Propagation (A2 = 0.80, score le plus élevé)
- **Régime secondaire :** Intégration (A3 = 0.60)
- **Marge :** A2 domine nettement A5 (Δ = 0.60) ; A1 et A4 sont symétriquement moyens (0.50)
- **Surprise par rapport au jugement intuitif :** Légère — on pourrait s'attendre à ce que la normativité (attracteur thermodynamique fort) domine, mais A4 est plafonnée par l'absence de correction active (N2 = 0, N3 = 0). La propagation phonon étant très efficace, A2 s'impose. A5 = 0.20 confirme l'intuition d'un système quasi-rigide.

---

## Notes libres

**Profil général :** NaCl est un système physique à haute intégrité structurelle mais à faible plasticité. Son profil A1=0.50 / A2=0.80 / A3=0.60 / A4=0.50 / A5=0.20 dessine un système propagateur-intégrateur passif, dépourvu de révision endogène.

**Point théoriquement intéressant :** NaCl constitue un cas-test pour la frontière entre *normativité physique* (attracteur d'énergie libre) et *normativité au sens systémique* (correction active). Le score A4 = 0.50 malgré un attracteur robuste (N1 = 1, N4 = 1) illustre bien que la présence d'un bassin d'attraction ne suffit pas à satisfaire les critères N2/N3.

**Limite de la grille sur les cristaux :** Les critères H3, I4, R3-R5 semblent calibrés pour des systèmes biologiques ou techno-institutionnels ; ils atteignent systématiquement 0 pour tout cristal ionique simple. NaCl peut servir d'étalon-bas pour calibrer ces critères sur d'autres systèmes physiques.

**Question ouverte :** Un cristal liquide ou un verre (SiO₂ amorphe) obtiendrait-il des scores significativement différents sur A5 ? La comparaison serait heuristiquement utile.
