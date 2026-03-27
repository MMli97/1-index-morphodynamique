"""
Index des Formes Conceptuelles Dynamiques — Scoring Cumulatif V2.1.2

Sous-critères identiques à V2.1.1:
- A2: invariance d'échelle (sensibilité structurelle relative, pas taille du graphe)
- A5: plasticité structurelle endogène (pas seulement révision institutionnelle explicite)

Classifieur V2.1.2 (seuls changements par rapport à V2.1.1):
- F01: Δ₂₃ ≤ 0.18 (was 0.15)
- F03: Δ₂₃ ≥ 0.23 (was 0.25)
- F06: Δ₂₃ ≤ 0.18 (was 0.15)
- F04, F05, F08, F09: inchangés

Sous-critères 0 / 0.5 / 1 (ternaire).
"""


def score(criteria: list) -> float:
    return round(sum(criteria) / len(criteria), 2)


# ─────────────────────────────────────────────
# GRILLE DE SOUS-CRITÈRES V2.1.1
# ─────────────────────────────────────────────

# A1 — PROFONDEUR HIÉRARCHIQUE (inchangé)
# H1: ≥ 2 niveaux distincts
# H2: ≥ 3 niveaux distincts
# H3: ≥ 4 niveaux distincts
# H4: Fonctions différenciées par niveau
# H5: Causalité bidirectionnelle entre niveaux

# A2 — PROPAGATION (PATCHÉE — invariance d'échelle)
# P1: Perturbation locale affecte au moins un autre module fonctionnel
# P2: Propagation traverse au moins un niveau hiérarchique
# P3: La propagation modifie l'état global observable
# P4: Isolement difficile sans modification structurelle
# P5: Couplage fonctionnel non trivial

# A3 — INTÉGRATION / COORDINATION (inchangé)
# I1: Mécanisme explicite de coordination
# I2: Réduction observable de variance
# I3: Synchronisation multi-niveaux
# I4: Boucles de feedback globales
# I5: Maintien d'un état cohérent global

# A4 — NORMATIVITÉ (inchangé)
# N1: Existence d'un attracteur dynamique
# N2: Correction active d'écart
# N3: Hiérarchie de priorités régulatoires
# N4: Mécanisme interne de stabilisation
# N5: Résistance aux perturbations prolongées

# A5 — RÉVISION (PATCHÉE — plasticité endogène)
# R1: Ajustement paramétrique local
# R2: Modification durable de configuration interne
# R3: Reconfiguration de réseau ou de structure
# R4: Modification des mécanismes de régulation
# R5: Capacité à produire de nouvelles règles de fonctionnement


cases = {}

# ── 01. Cellule eucaryote ──
# A2 patchée: perturbation ATP affecte métabolisme (P1=1), traverse niveaux moléculaire→cellulaire (P2=1),
#   modifie état global (P3=1), isolement difficile (P4=1), couplage fonctionnel dense (P5=1)
# A5 patchée: modulation expression (R1=1), remodelage chromatine durable (R2=1),
#   réorganisation réseau signalisation (R3=1), modification mécanismes régulatoires par épigénétique (R4=0.5),
#   pas de création de règles nouvelles — le génome contraint (R5=0)
cases["01 Cellule eucaryote"] = {
    "H": [1, 1, 1, 1, 1],        # 4+ niveaux, différenciés, bidirectionnels
    "P": [1, 1, 1, 1, 1],        # PATCHÉ: propagation forte à toute échelle
    "I": [1, 1, 1, 1, 1],
    "N": [1, 1, 0.5, 1, 0.5],
    "R": [1, 1, 1, 0.5, 0],      # PATCHÉ: plasticité endogène élevée
}

# ── 02. Thermostat ──
# A2 patchée: capteur → contrôleur = un module affecté (P1=1), traverse capteur→actionneur (P2=1),
#   modifie état global température (P3=1), isolement facile (P4=0), couplage fonctionnel réel (P5=1)
# A5 patchée: pas d'ajustement (R1=0), pas de modification durable (R2=0),
#   pas de reconfiguration (R3=0), pas de modification régulation (R4=0), pas de règles nouvelles (R5=0)
cases["02 Thermostat"] = {
    "H": [1, 0, 0, 0, 0],
    "P": [1, 1, 1, 0, 1],        # PATCHÉ: couplage fonctionnel réel malgré petite taille
    "I": [1, 1, 0, 0, 0.5],
    "N": [1, 1, 0, 1, 0.5],
    "R": [0, 0, 0, 0, 0],        # PATCHÉ: identique — aucune plasticité
}

# ── 03. Marché NYSE ──
# A2 patchée: flash crash = module affecté (P1=1), traverse niveaux (P2=1),
#   modifie état global (P3=1), isolement très difficile (P4=1), couplage dense (P5=0.5 — variable)
# A5 patchée: ajustement paramétrique marge (R1=1), modification instruments durable (R2=0.5),
#   reconfiguration partielle structure (R3=0.5), modification mécanismes partiellement (R4=0),
#   pas de production de nouvelles règles endogènes (R5=0)
cases["03 Marché NYSE"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 1, 1, 0.5],      # PATCHÉ: couplage variable
    "I": [1, 0.5, 0.5, 0.5, 0.5],
    "N": [0.5, 0.5, 0, 0.5, 0],
    "R": [1, 0.5, 0.5, 0, 0],    # PATCHÉ: plasticité limitée
}

# ── 04. Immunité adaptative ──
# A2 patchée: cytokine → cascade (P1=1), traverse innée→adaptative (P2=1),
#   modifie état global immunitaire (P3=1), isolement difficile (P4=0.5), couplage dense (P5=1)
# A5 patchée: maturation d'affinité (R1=1), switch isotypique durable (R2=1),
#   reconfiguration répertoire (R3=1), modification mécanismes tolérance (R4=0.5),
#   pas de création de règles — contraint par génome (R5=0)
cases["04 Immunité adaptative"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 1, 0.5, 1],      # PATCHÉ
    "I": [1, 1, 1, 1, 0.5],
    "N": [1, 1, 1, 1, 0.5],
    "R": [1, 1, 1, 0.5, 0],      # PATCHÉ: plasticité adaptative élevée
}

# ── 05. Église ──
# A2 patchée: réforme locale affecte peu (P1=0.5), traverse niveaux lentement (P2=0.5),
#   modifie rarement l'état global (P3=0), isolement facile (P4=0), couplage faible (P5=0.5)
# A5 patchée: ajustement marginal (R1=0.5), modification durable rare (R2=0),
#   pas de reconfiguration (R3=0), pas de modification régulation (R4=0), pas de règles nouvelles (R5=0)
cases["05 Église"] = {
    "H": [1, 1, 1, 1, 0.5],
    "P": [0.5, 0.5, 0, 0, 0.5],  # PATCHÉ: propagation faible
    "I": [1, 0.5, 0.5, 0.5, 0.5],
    "N": [1, 1, 1, 1, 1],
    "R": [0.5, 0, 0, 0, 0],      # PATCHÉ: plasticité quasi nulle
}

# ── 06. Ve République ──
# A2 patchée: crise politique affecte plusieurs institutions (P1=1), traverse niveaux (P2=1),
#   modifie état global parfois (P3=0.5), isolement difficile en crise (P4=0.5), couplage modéré (P5=0.5)
# A5 patchée: ajustement paramétrique oui (R1=1), modification durable institutions (R2=1),
#   reconfiguration partielle (R3=0.5), modification mécanismes constitution (R4=0.5),
#   pas de production de règles entièrement nouvelles — cadre contraint (R5=0)
cases["06 Ve République"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 0.5, 0.5, 0.5],  # PATCHÉ
    "I": [1, 0.5, 0.5, 1, 0.5],
    "N": [1, 1, 0.5, 1, 0.5],
    "R": [1, 1, 0.5, 0.5, 0],    # PATCHÉ: plasticité institutionnelle réelle mais contrainte
}

# ── 07. Organisme multicellulaire ──
# A2 patchée: perturbation hormonale = systémique (P1=1), traverse tous niveaux (P2=1),
#   modifie état global (P3=1), isolement très difficile (P4=1), couplage dense (P5=1)
# A5 patchée: neuroplasticité paramétrique (R1=1), modification durable connexions (R2=1),
#   reconfiguration réseau neural (R3=0.5), modification homéostatique partielle (R4=0.5),
#   pas de création de règles nouvelles — génome fixe (R5=0)
cases["07 Organisme multicel"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 1, 1, 1],        # PATCHÉ
    "I": [1, 1, 1, 1, 1],
    "N": [1, 1, 1, 1, 1],
    "R": [1, 1, 0.5, 0.5, 0],    # PATCHÉ: plasticité réelle mais contrainte par génome
}

# ── 08. Régime autoritaire ──
# A2 patchée: purge = cascade (P1=1), traverse tous niveaux (P2=1),
#   modifie état global (P3=1), isolement quasi impossible (P4=1), couplage dense par peur (P5=1)
# A5 patchée: ajustement par décret (R1=0.5), modification durable par le sommet (R2=0.5),
#   pas de reconfiguration structurelle réelle (R3=0), pas de modification mécanismes (R4=0),
#   pas de production de règles — le leader impose (R5=0)
cases["08 Régime autoritaire"] = {
    "H": [1, 1, 1, 1, 0],
    "P": [1, 1, 1, 1, 1],        # PATCHÉ
    "I": [1, 0.5, 0.5, 0.5, 0],
    "N": [1, 1, 1, 1, 1],
    "R": [0.5, 0.5, 0, 0, 0],    # PATCHÉ: plasticité très faible
}

# ── 09. Supply chain ──
# A2 patchée: pénurie composant = cascade globale (P1=1), traverse niveaux (P2=1),
#   modifie état global (P3=1), isolement très difficile (P4=1), couplage dense (P5=1)
# A5 patchée: ajustement stocks (R1=1), reconfiguration fournisseurs durable (R2=0.5),
#   reconfiguration réseau partielle (R3=0.5), pas de modification mécanismes (R4=0),
#   pas de production de règles nouvelles (R5=0)
cases["09 Supply chain"] = {
    "H": [1, 1, 1, 1, 0.5],
    "P": [1, 1, 1, 1, 1],        # PATCHÉ
    "I": [0.5, 0.5, 0.5, 0.5, 0],
    "N": [0, 0.5, 0, 0.5, 0],
    "R": [1, 0.5, 0.5, 0, 0],    # PATCHÉ
}

# ── 10. Apple ──
# A2 patchée: décision produit → cascade supply+retail (P1=1), traverse niveaux (P2=1),
#   modifie état global (P3=1), isolement difficile (P4=0.5), couplage fonctionnel fort (P5=1)
# A5 patchée: ajustement produit (R1=1), pivot stratégique durable (R2=1),
#   reconfiguration chaîne valeur (R3=1), modification processus décisionnel (R4=0.5),
#   production de nouvelles catégories (R5=0.5)
cases["10 Apple"] = {
    "H": [1, 1, 1, 1, 0.5],
    "P": [1, 1, 1, 0.5, 1],      # PATCHÉ
    "I": [1, 1, 1, 1, 1],
    "N": [1, 1, 1, 1, 0.5],
    "R": [1, 1, 1, 0.5, 0.5],    # PATCHÉ: plasticité stratégique élevée
}

# ── 11. TikTok ──
# A2 patchée: changement algo = cascade sur tout le feed (P1=1), traverse niveaux (P2=1),
#   modifie état global (P3=1), isolement impossible (P4=1), couplage dense via algo (P5=1)
# A5 patchée: ajustement algo constant (R1=1), modification durable modération (R2=1),
#   reconfiguration feed (R3=0.5), modification mécanismes engagement (R4=0.5),
#   pas de production de règles entièrement nouvelles (R5=0)
cases["11 TikTok"] = {
    "H": [1, 1, 0.5, 1, 0.5],
    "P": [1, 1, 1, 1, 1],        # PATCHÉ
    "I": [1, 1, 0.5, 1, 0.5],
    "N": [1, 1, 0.5, 1, 0.5],
    "R": [1, 1, 0.5, 0.5, 0],    # PATCHÉ
}

# ── 12. LLM statique ──
# A2 patchée: perturbation token → cascade attentionnelle (P1=1), traverse couches (P2=1),
#   modifie sortie (P3=1), isolement impossible (forward pass) (P4=1), couplage dense attention (P5=1)
# A5 patchée: aucun ajustement (R1=0), aucune modification (R2=0),
#   aucune reconfiguration (R3=0), aucune modification régulation (R4=0),
#   aucune production de règles (R5=0)
cases["12 LLM statique"] = {
    "H": [1, 1, 1, 1, 0],
    "P": [1, 1, 1, 1, 1],        # PATCHÉ: propagation maximale
    "I": [1, 1, 0.5, 1, 1],
    "N": [0, 0, 0, 0, 0],
    "R": [0, 0, 0, 0, 0],        # PATCHÉ: identique — aucune plasticité
}

# ── 13. Linux ──
# A2 patchée: bug noyau affecte modules (P1=1), traverse niveaux (P2=0.5),
#   modifie état global parfois (P3=0.5), isolement possible grâce à modularité (P4=0), couplage modéré (P5=0.5)
# A5 patchée: ajustement constant (R1=1), refactoring durable (R2=1),
#   reconfiguration architecture possible (R3=1), modification processus contribution (R4=1),
#   production de nouveaux sous-systèmes (R5=0.5)
cases["13 Linux"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 0.5, 0.5, 0, 0.5],  # PATCHÉ: propagation limitée par modularité
    "I": [1, 1, 0.5, 1, 1],
    "N": [1, 1, 0.5, 1, 0.5],
    "R": [1, 1, 1, 1, 0.5],      # PATCHÉ: plasticité élevée
}

# ── 14. Ordre réformé ──
# A2 patchée: crise locale affecte province (P1=0.5), traverse partiellement (P2=0.5),
#   modifie rarement l'état global (P3=0), isolement facile (P4=0), couplage faible (P5=0.5)
# A5 patchée: ajustement marginal (R1=0.5), modification durable rare (R2=0.5),
#   reconfiguration rare (chapitre) (R3=0.5), modification mécanismes rare (R4=0),
#   pas de production de règles nouvelles (R5=0)
cases["14 Ordre réformé"] = {
    "H": [1, 1, 1, 1, 0.5],
    "P": [0.5, 0.5, 0, 0, 0.5],  # PATCHÉ
    "I": [1, 0.5, 0.5, 0.5, 0.5],
    "N": [1, 1, 1, 1, 1],
    "R": [0.5, 0.5, 0.5, 0, 0],  # PATCHÉ: plasticité faible
}

# ── 15. Physique théorique ──
# A2 patchée: résultat majeur affecte sous-champs (P1=1), traverse niveaux (P2=0.5),
#   modifie état global parfois (P3=0.5), isolement partiel (P4=0.5), couplage modéré (P5=0.5)
# A5 patchée: ajustement constant (R1=1), modification durable paradigmes (R2=1),
#   reconfiguration champs (R3=1), modification méthode scientifique (R4=1),
#   production de nouvelles théories (R5=1)
cases["15 Physique théorique"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 0.5, 0.5, 0.5, 0.5], # PATCHÉ
    "I": [1, 0.5, 0.5, 1, 0.5],
    "N": [1, 1, 0, 0.5, 0.5],
    "R": [1, 1, 1, 1, 1],         # PATCHÉ: plasticité maximale
}


# ─────────────────────────────────────────────
# Calcul et classification V2.1.2
# ─────────────────────────────────────────────

v21_scores = {
    "01 Cellule eucaryote":   {"A1":1.00,"A2":0.80,"A3":1.00,"A4":0.80,"A5":0.30},
    "02 Thermostat":          {"A1":0.20,"A2":0.00,"A3":0.50,"A4":0.70,"A5":0.00},
    "03 Marché NYSE":         {"A1":1.00,"A2":0.90,"A3":0.60,"A4":0.30,"A5":0.40},
    "04 Immunité adaptative": {"A1":1.00,"A2":0.70,"A3":0.90,"A4":0.90,"A5":0.60},
    "05 Église":              {"A1":0.90,"A2":0.40,"A3":0.60,"A4":1.00,"A5":0.10},
    "06 Ve République":       {"A1":1.00,"A2":0.60,"A3":0.70,"A4":0.80,"A5":0.60},
    "07 Organisme multicel":  {"A1":1.00,"A2":0.90,"A3":1.00,"A4":1.00,"A5":0.30},
    "08 Régime autoritaire":  {"A1":0.80,"A2":0.90,"A3":0.50,"A4":1.00,"A5":0.10},
    "09 Supply chain":        {"A1":0.90,"A2":1.00,"A3":0.40,"A4":0.20,"A5":0.30},
    "10 Apple":               {"A1":0.90,"A2":0.70,"A3":1.00,"A4":0.90,"A5":0.70},
    "11 TikTok":              {"A1":0.80,"A2":0.90,"A3":0.80,"A4":0.80,"A5":0.50},
    "12 LLM statique":        {"A1":0.80,"A2":0.80,"A3":0.90,"A4":0.00,"A5":0.00},
    "13 Linux":               {"A1":1.00,"A2":0.40,"A3":0.90,"A4":0.80,"A5":0.80},
    "14 Ordre réformé":       {"A1":0.90,"A2":0.40,"A3":0.60,"A4":1.00,"A5":0.30},
    "15 Physique théorique":  {"A1":1.00,"A2":0.40,"A3":0.70,"A4":0.60,"A5":0.90},
}


def compute_all():
    print("=" * 135)
    print("SCORING V2.1.2 — Matrice corrigée (A2 invariant d'échelle, A5 plasticité endogène)")
    print("=" * 135)
    print(f"{'Système':28s} | {'A1':>5s} {'A2':>5s} {'A3':>5s} {'A4':>5s} {'A5':>5s} | {'Δ23':>6s} {'Δ45':>6s} {'Δ12':>6s} {'Δ35':>6s} {'Δ43':>6s}")
    print("-" * 135)

    results = {}
    all_scores = {"A1": [], "A2": [], "A3": [], "A4": [], "A5": []}

    for name, c in cases.items():
        A1 = score(c["H"])
        A2 = score(c["P"])
        A3 = score(c["I"])
        A4 = score(c["N"])
        A5 = score(c["R"])

        D23 = round(A2 - A3, 2)
        D45 = round(A4 - A5, 2)
        D12 = round(A1 - A2, 2)
        D35 = round(A3 - A5, 2)
        D43 = round(A4 - A3, 2)

        results[name] = {"A1":A1,"A2":A2,"A3":A3,"A4":A4,"A5":A5,
                         "D23":D23,"D45":D45,"D12":D12,"D35":D35,"D43":D43}

        for k in ["A1","A2","A3","A4","A5"]:
            all_scores[k].append(results[name][k])

        print(f"{name:28s} | {A1:5.2f} {A2:5.2f} {A3:5.2f} {A4:5.2f} {A5:5.2f} | "
              f"{D23:+6.2f} {D45:+6.2f} {D12:+6.2f} {D35:+6.2f} {D43:+6.2f}")

    # Dispersion
    print("\n" + "=" * 80)
    print("DISPERSION V2.1.2")
    print("=" * 80)
    for k in ["A1","A2","A3","A4","A5"]:
        vals = all_scores[k]
        mn, mx = min(vals), max(vals)
        avg = sum(vals)/len(vals)
        std = (sum((v-avg)**2 for v in vals)/len(vals))**0.5
        print(f"  {k}: min={mn:.2f} max={mx:.2f} mean={avg:.2f} std={std:.2f} range={mx-mn:.2f}")

    # Comparaison V2.1 → V2.1.1
    print("\n" + "=" * 135)
    print("COMPARAISON V2.1 → V2.1.2")
    print("=" * 135)
    print(f"{'Système':28s} | {'δA2':>5s} {'δA5':>5s} | {'Δ23 old':>7s} {'Δ23 new':>7s} {'δΔ23':>6s} | {'Δ45 old':>7s} {'Δ45 new':>7s} {'δΔ45':>6s} | Note")
    print("-" * 135)

    for name in results:
        r = results[name]
        v = v21_scores[name]
        dA2 = round(r["A2"] - v["A2"], 2)
        dA5 = round(r["A5"] - v["A5"], 2)

        old_D23 = round(v["A2"] - v["A3"], 2)
        old_D45 = round(v["A4"] - v["A5"], 2)
        dD23 = round(r["D23"] - old_D23, 2)
        dD45 = round(r["D45"] - old_D45, 2)

        note = ""
        if abs(dA2) >= 0.30:
            note += f"A2 {'↑' if dA2>0 else '↓'}{abs(dA2):.1f} "
        if abs(dA5) >= 0.30:
            note += f"A5 {'↑' if dA5>0 else '↓'}{abs(dA5):.1f} "
        if abs(dD45) >= 0.20:
            note += f"Δ45 shift! "

        print(f"{name:28s} | {dA2:+5.2f} {dA5:+5.2f} | {old_D23:+7.2f} {r['D23']:+7.2f} {dD23:+6.2f} | "
              f"{old_D45:+7.2f} {r['D45']:+7.2f} {dD45:+6.2f} | {note}")

    return results


if __name__ == "__main__":
    compute_all()
