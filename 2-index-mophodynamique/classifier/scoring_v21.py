"""
Index des Formes Conceptuelles Dynamiques — Scoring Cumulatif V2.1

Chaque axe est décomposé en 5 sous-critères notés 0 / 0.5 / 1.
Score = moyenne des sous-critères → [0, 1].

Les Δ sont dérivés mécaniquement des scores.
"""

# ─────────────────────────────────────────────
# Sous-critères par axe
# ─────────────────────────────────────────────

# A1 — PROFONDEUR HIÉRARCHIQUE
# H1: ≥ 2 niveaux distincts
# H2: ≥ 3 niveaux distincts
# H3: ≥ 4 niveaux distincts
# H4: Fonctions différenciées par niveau
# H5: Causalité bidirectionnelle entre niveaux

# A2 — PROPAGATION DES PERTURBATIONS
# P1: Perturbation locale affecte une part significative du système
# P2: Propagation multi-niveaux
# P3: Propagation rapide (temps court relatif au système)
# P4: Difficulté d'isolement de la perturbation
# P5: Graphe interne à couplage dense

# A3 — INTÉGRATION / COORDINATION
# I1: Mécanisme explicite de coordination
# I2: Réduction observable de variance
# I3: Synchronisation multi-niveaux
# I4: Boucles de feedback globales
# I5: Maintien d'un état cohérent global

# A4 — NORMATIVITÉ
# N1: Existence d'un attracteur dynamique
# N2: Correction active d'écart
# N3: Hiérarchie de priorités régulatoires
# N4: Mécanisme interne de stabilisation
# N5: Résistance aux perturbations prolongées

# A5 — RÉVISION DES RÈGLES
# R1: Ajustement paramétrique
# R2: Modification de règles locales
# R3: Modification de règles globales
# R4: Méta-régulation explicite
# R5: Révision structurelle profonde


def score(criteria: list) -> float:
    """Score = moyenne des sous-critères."""
    return round(sum(criteria) / len(criteria), 2)


# ─────────────────────────────────────────────
# SCORING DES 15 CAS
# ─────────────────────────────────────────────

cases = {}

# ── 01. Cellule eucaryote ──
# H: noyau/RE/Golgi/mito/lyso = 4+ niveaux, fonctions différenciées, signalisation bidirectionnelle
# P: perturbation ATP → cascade, multi-niveaux, rapide, difficile à isoler, réseau métabolique dense
# I: checkpoints coordonnent, réduction variance pH/redox, synchronisation, feedback globaux, cohérence maintenue
# N: attracteur homéostatique, correction active (réparation ADN), priorités (apoptose > survie), stabilisation, résistance modérée
# R: remodelage épigénétique (paramétrique), modification expression locale, pas de modification globale du génome, pas de méta-régulation, pas de révision structurelle profonde
cases["01 Cellule eucaryote"] = {
    "H": [1, 1, 1, 1, 1],        # 4+ niveaux, différenciés, bidirectionnels
    "P": [1, 1, 0.5, 0.5, 1],    # propagation forte mais vitesse variable, isolement partiel possible
    "I": [1, 1, 1, 1, 1],        # coordination excellente
    "N": [1, 1, 0.5, 1, 0.5],    # pas de hiérarchie de priorités complète, résistance limitée dans le temps
    "R": [1, 0.5, 0, 0, 0],      # ajustement épigénétique oui, modification locale partielle, pas de révision globale
}

# ── 02. Thermostat ──
# H: capteur + comparateur = 2 niveaux max, pas de fonctions différenciées au-delà, pas de bidirectionnalité
# P: perturbation locale reste locale, système trop simple pour propager
# I: réduit variance sur 1 variable, pas de synchronisation multi-niveaux
# N: attracteur clair (consigne), correction active, pas de hiérarchie, stabilisation simple, résistance faible
# R: aucune capacité de révision
cases["02 Thermostat"] = {
    "H": [1, 0, 0, 0, 0],
    "P": [0, 0, 0, 0, 0],
    "I": [1, 1, 0, 0, 0.5],      # coordonne 1 variable, réduit variance, maintient état partiel
    "N": [1, 1, 0, 1, 0.5],      # attracteur oui, correction oui, stabilisation oui, résistance limitée
    "R": [0, 0, 0, 0, 0],
}

# ── 03. Marché NYSE ──
# H: ordre → matching → compensation → indices → dérivés = 5+ niveaux, fonctions très différenciées, causalité bidirectionnelle
# P: flash crash = propagation globale rapide, difficile à isoler, corrélations fortes
# I: mécanisme de prix agrège info, arbitrage réduit écarts, mais variance globale pas fortement comprimée
# N: circuit breakers, margin calls, arbitrage = correction partielle. Mais échoue face aux grandes déviations. Normativité surtout externe.
# R: introduction nouveaux instruments, modification règles marge, mais lent et souvent réactif
cases["03 Marché NYSE"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 1, 1, 0.5],      # propagation massive, rapide, difficile à isoler. Couplage dense variable.
    "I": [1, 0.5, 0.5, 0.5, 0.5], # prix coordonne, réduction variance partielle, synchronisation partielle
    "N": [0.5, 0.5, 0, 0.5, 0],   # attracteur partiel, correction partielle, pas de hiérarchie interne, résistance faible
    "R": [1, 0.5, 0.5, 0, 0],     # ajustement oui, règles locales partiellement, globales partiellement, pas de méta
}

# ── 04. Immunité adaptative ──
# H: cellules innées → adaptatives → mémoire → coordination thymus/moelle = 4+ niveaux
# P: cytokines propagent localement et systémiquement, multi-niveaux, rapide
# I: coordination clonale, réduction variance par sélection, synchronisation innée/adaptative
# N: tolérance au soi = attracteur, correction active (suppression auto-immune), priorités, résistance
# R: maturation d'affinité = modification locale, switch isotypique = modification globale, mais pas de méta-régulation au sens strict
cases["04 Immunité adaptative"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 0.5, 0.5, 0.5],  # propagation forte mais partiellement isolable
    "I": [1, 1, 1, 1, 0.5],      # coordination excellente, cohérence globale partielle (auto-immunité possible)
    "N": [1, 1, 1, 1, 0.5],      # très normatif mais résistance pas absolue
    "R": [1, 1, 0.5, 0.5, 0],    # maturation d'affinité, switch, mais pas de révision structurelle profonde
}

# ── 05. Église (institution) ──
# H: paroisse → diocèse → conférence → curie → pape = 5+ niveaux, fonctions très différenciées, bidirectionnalité limitée (top-down dominant)
# P: réforme locale se propage mal (modularité massive), isolation forte
# I: doctrine = coordination, liturgie = synchronisation, mais pratiques locales varient beaucoup
# N: droit canon = attracteur fort, correction active (censure, excommunication), hiérarchie de priorités, stabilisation forte, résistance élevée
# R: aggiornamento possible mais extrêmement lent, Vatican II = modification globale mais une fois par siècle, pas de méta-régulation
cases["05 Église"] = {
    "H": [1, 1, 1, 1, 0.5],      # bidirectionnalité limitée
    "P": [0.5, 0.5, 0, 0.5, 0.5], # propagation lente, partiellement isolable
    "I": [1, 0.5, 0.5, 0.5, 0.5], # doctrine coordonne mais pratiques varient
    "N": [1, 1, 1, 1, 1],         # très normatif
    "R": [0.5, 0, 0, 0, 0],       # ajustement marginal seulement
}

# ── 06. Ve République ──
# H: commune → département → région → État → UE = 5 niveaux, fonctions différenciées, bidirectionnalité (élections)
# P: crise politique se propage (cohabitation, gilets jaunes), multi-niveaux, vitesse variable
# I: constitution coordonne, réduction variance par cadre juridique, synchronisation partielle
# N: Conseil constitutionnel = attracteur, correction active (censure, dissolution), hiérarchie claire, résistance modérée
# R: révision constitutionnelle possible, modification des règles du jeu, mais méta-régulation limitée
cases["06 Ve République"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [0.5, 1, 0.5, 0.5, 0.5], # propagation variable
    "I": [1, 0.5, 0.5, 1, 0.5],   # cadre juridique coordonne, feedback institutionnel
    "N": [1, 1, 0.5, 1, 0.5],     # normatif mais pas absolument résistant
    "R": [1, 1, 0.5, 0.5, 0],     # révision constitutionnelle oui, méta-régulation partielle
}

# ── 07. Organisme multicellulaire ──
# H: molécule → organelle → cellule → tissu → organe → système → organisme = 6+ niveaux
# P: perturbation hormonale = systémique, rapide, multi-niveaux, difficile à isoler
# I: coordination endocrine + nerveuse, réduction variance homéostatique, synchronisation multi-systèmes
# N: homéostasie = attracteur fort, correction multi-niveaux, priorités (cerveau > périphérie), résistance élevée
# R: neuroplasticité = modification locale, adaptation immunitaire = modification locale, mais génome fixe
cases["07 Organisme multicel"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [1, 1, 1, 0.5, 1],      # propagation forte, difficile à isoler mais pas impossible
    "I": [1, 1, 1, 1, 1],
    "N": [1, 1, 1, 1, 1],
    "R": [1, 0.5, 0, 0, 0],      # ajustement paramétrique oui, modification locale partielle, pas de révision globale
}

# ── 08. Régime autoritaire ──
# H: population → administration → parti → cercle intérieur → leader = 4-5 niveaux, fonctions différenciées, bidirectionnalité très faible
# P: purge ou ordre = propagation rapide et massive, multi-niveaux, difficile à résister
# I: coordination par coercition, variance réduite par peur, synchronisation forcée, pas de cohérence organique
# N: attracteur imposé, correction agressive (police politique), hiérarchie de priorités, stabilisation forte, résistance élevée
# R: le leader peut changer les règles, mais le système ne peut pas changer de leader = révision unidirectionnelle
cases["08 Régime autoritaire"] = {
    "H": [1, 1, 1, 1, 0],        # pas de bidirectionnalité
    "P": [1, 1, 1, 1, 0.5],      # propagation massive
    "I": [1, 0.5, 0.5, 0.5, 0],  # coordination par coercition, pas de cohérence organique
    "N": [1, 1, 1, 1, 1],
    "R": [0.5, 0, 0, 0, 0],      # ajustement marginal par le sommet seulement
}

# ── 09. Supply chain globale ──
# H: fournisseur → fabricant → logistique → distributeur = 4 niveaux, fonctions différenciées, bidirectionnalité via commandes
# P: pénurie composant = cascade globale (cf. semi-conducteurs 2021), rapide, très difficile à isoler
# I: coordination par contrats et planification, mais variance élevée, synchronisation partielle
# N: pas d'attracteur global clair, correction par ajustement de stocks, pas de hiérarchie de priorités globale
# R: reconfiguration possible (relocalisation), mais lente et réactive
cases["09 Supply chain"] = {
    "H": [1, 1, 1, 1, 0.5],      # bidirectionnalité partielle
    "P": [1, 1, 1, 1, 1],        # propagation maximale
    "I": [0.5, 0.5, 0.5, 0.5, 0], # coordination contractuelle, pas de cohérence globale
    "N": [0, 0.5, 0, 0.5, 0],    # pas d'attracteur clair, correction partielle
    "R": [1, 0.5, 0, 0, 0],      # ajustement paramétrique, modification locale partielle
}

# ── 10. Apple ──
# H: équipe → division → SVP → Tim Cook = 4+ niveaux, fonctions très différenciées, bidirectionnalité contrôlée
# P: décision produit se propage à toute la chaîne, multi-niveaux, rapide en interne
# I: intégration verticale forte, design → hardware → software coordonnés, cohérence de marque
# N: culture de design = attracteur, correction active (standards qualité), hiérarchie claire, résistance forte
# R: pivot vers services, changement architecture puces = modification globale, Tim Cook ≠ Jobs = adaptation
cases["10 Apple"] = {
    "H": [1, 1, 1, 1, 0.5],      # bidirectionnalité contrôlée mais pas totale
    "P": [1, 1, 0.5, 0.5, 0.5],  # propagation forte mais partiellement gérable
    "I": [1, 1, 1, 1, 1],        # intégration verticale excellente
    "N": [1, 1, 1, 1, 0.5],      # très normatif mais pas absolument résistant
    "R": [1, 1, 1, 0.5, 0],      # pivot oui, modification globale oui, méta-régulation partielle
}

# ── 11. TikTok (plateforme) ──
# H: utilisateur → algo recommandation → modération → stratégie produit = 3-4 niveaux
# P: trend virale = propagation instantanée, changement algo affecte tout le monde
# I: algo coordonne l'attention, réduit variance de ce qui est vu, synchronisation par feed
# N: modération + algo = attracteur (maximiser engagement), correction active, priorités
# R: ajustement algo constant, modification règles modération, mais pas de révision structurelle profonde
cases["11 TikTok"] = {
    "H": [1, 1, 0.5, 1, 0.5],    # 3-4 niveaux, pas sûr des 4+
    "P": [1, 1, 1, 1, 0.5],      # propagation virale massive
    "I": [1, 1, 0.5, 1, 0.5],    # algo coordonne fortement
    "N": [1, 1, 0.5, 1, 0.5],    # normatif via algo
    "R": [1, 1, 0.5, 0, 0],      # ajustement constant, modification locale, pas de méta
}

# ── 12. LLM statique (inférence) ──
# H: token → attention → couches → représentation latente → sortie = 5+ niveaux, fonctions différenciées, pas de bidirectionnalité (forward only)
# P: perturbation token → cascade attentionnelle, multi-couches, instantanée, non isolable
# I: attention = coordination, représentations latentes = cohérence, synchronisation par architecture
# N: aucun attracteur dynamique, aucune correction, aucune hiérarchie normative, aucune stabilisation, aucune résistance
# R: aucune capacité de révision
cases["12 LLM statique"] = {
    "H": [1, 1, 1, 1, 0],        # pas de bidirectionnalité (forward pass)
    "P": [1, 1, 1, 0.5, 0.5],    # propagation forte mais architecture contrôle le flux
    "I": [1, 1, 0.5, 1, 1],      # attention coordonne, cohérence forte
    "N": [0, 0, 0, 0, 0],
    "R": [0, 0, 0, 0, 0],
}

# ── 13. Linux (écosystème) ──
# H: contributeur → mainteneur → sous-système → Linus = 4 niveaux, fonctions différenciées, bidirectionnalité (patches remontent)
# P: bug noyau peut casser tout, mais architecture modulaire isole bien
# I: code review = coordination, tests = réduction variance, releases = synchronisation
# N: coding standards = attracteur, review = correction, hiérarchie de mainteneurs, résistance aux mauvais patches
# R: refactoring régulier, changement architecture possible, méta-régulation (changement process de contribution)
cases["13 Linux"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [0.5, 0.5, 0.5, 0, 0.5], # propagation limitée par modularité
    "I": [1, 1, 0.5, 1, 1],       # coordination forte
    "N": [1, 1, 0.5, 1, 0.5],     # normatif mais flexible
    "R": [1, 1, 1, 0.5, 0.5],     # révision active, méta-régulation partielle
}

# ── 14. Ordre religieux réformé ──
# H: communauté → province → chapitre → gouvernement général = 4 niveaux, différenciés, bidirectionnalité par chapitres
# P: crise communauté locale se propage peu (autonomie), sauf crise de gouvernance
# I: règle commune = coordination, liturgie = synchronisation, mais autonomie locale
# N: règle = attracteur fort, correction par visite canonique, hiérarchie claire, résistance forte
# R: chapitre peut modifier la règle (= révision globale), mais processus très lent et conservateur
cases["14 Ordre réformé"] = {
    "H": [1, 1, 1, 1, 0.5],      # bidirectionnalité par chapitres mais limitée
    "P": [0.5, 0.5, 0, 0.5, 0.5], # propagation faible
    "I": [1, 0.5, 0.5, 0.5, 0.5], # coordination par règle, variance locale
    "N": [1, 1, 1, 1, 1],
    "R": [0.5, 0.5, 0.5, 0, 0],   # chapitre peut réviser mais rarement et marginalement
}

# ── 15. Physique théorique (discipline) ──
# H: doctorant → chercheur → groupe → sous-champ → discipline = 4+ niveaux, fonctions différenciées, bidirectionnalité forte
# P: résultat majeur se propage à tout le champ, mais lentement (peer review), partiellement isolable
# I: peer review = coordination, consensus = réduction variance, conférences = synchronisation
# N: reproductibilité = attracteur, peer review = correction, mais pas de hiérarchie rigide
# R: changement de paradigme possible, méta-réflexion sur la méthode, épistémologie intégrée
cases["15 Physique théorique"] = {
    "H": [1, 1, 1, 1, 1],
    "P": [0.5, 0.5, 0, 0.5, 0.5], # propagation lente, partiellement isolable
    "I": [1, 0.5, 0.5, 1, 0.5],   # coordination par consensus, cohérence partielle
    "N": [1, 1, 0, 0.5, 0.5],     # pas de hiérarchie rigide, résistance modérée
    "R": [1, 1, 1, 1, 0.5],       # révision de paradigme, méta-régulation épistémologique
}


# ─────────────────────────────────────────────
# Calcul et affichage
# ─────────────────────────────────────────────

def compute_all():
    print("=" * 130)
    print("SCORING CUMULATIF V2.1 — 15 cas")
    print("=" * 130)
    print(f"{'Système':28s} | {'A1':>5s} {'A2':>5s} {'A3':>5s} {'A4':>5s} {'A5':>5s} | {'Δ23':>6s} {'Δ45':>6s} {'Δ12':>6s} {'Δ35':>6s} {'Δ43':>6s}")
    print("-" * 130)

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

        results[name] = {
            "A1": A1, "A2": A2, "A3": A3, "A4": A4, "A5": A5,
            "D23": D23, "D45": D45, "D12": D12, "D35": D35, "D43": D43
        }

        for k in ["A1", "A2", "A3", "A4", "A5"]:
            all_scores[k].append(results[name][k])

        print(f"{name:28s} | {A1:5.2f} {A2:5.2f} {A3:5.2f} {A4:5.2f} {A5:5.2f} | "
              f"{D23:+6.2f} {D45:+6.2f} {D12:+6.2f} {D35:+6.2f} {D43:+6.2f}")

    # Statistiques de dispersion
    print("\n" + "=" * 80)
    print("DISPERSION (vérification compression)")
    print("=" * 80)
    for k in ["A1", "A2", "A3", "A4", "A5"]:
        vals = all_scores[k]
        mn, mx = min(vals), max(vals)
        avg = sum(vals) / len(vals)
        var = sum((v - avg) ** 2 for v in vals) / len(vals)
        std = var ** 0.5
        print(f"  {k}: min={mn:.2f} max={mx:.2f} mean={avg:.2f} std={std:.2f} range={mx-mn:.2f}")

    return results


def compare_v2(results):
    """Compare V2.1 scores with V2 scores."""
    v2_scores = {
        "01 Cellule eucaryote":   {"A1":0.70,"A2":0.60,"A3":0.75,"A4":0.65,"A5":0.35},
        "02 Thermostat":          {"A1":0.20,"A2":0.40,"A3":0.45,"A4":0.50,"A5":0.00},
        "03 Marché NYSE":         {"A1":0.60,"A2":0.75,"A3":0.50,"A4":0.30,"A5":0.20},
        "04 Immunité adaptative": {"A1":0.75,"A2":0.65,"A3":0.70,"A4":0.65,"A5":0.55},
        "05 Église":              {"A1":0.80,"A2":0.55,"A3":0.60,"A4":0.75,"A5":0.10},
        "06 Ve République":       {"A1":0.65,"A2":0.60,"A3":0.55,"A4":0.60,"A5":0.40},
        "07 Organisme multicel":  {"A1":0.85,"A2":0.70,"A3":0.80,"A4":0.75,"A5":0.30},
        "08 Régime autoritaire":  {"A1":0.70,"A2":0.65,"A3":0.45,"A4":0.80,"A5":0.05},
        "09 Supply chain":        {"A1":0.55,"A2":0.80,"A3":0.45,"A4":0.35,"A5":0.15},
        "10 Apple":               {"A1":0.75,"A2":0.65,"A3":0.70,"A4":0.70,"A5":0.50},
        "11 TikTok":              {"A1":0.60,"A2":0.75,"A3":0.65,"A4":0.55,"A5":0.45},
        "12 LLM statique":        {"A1":0.90,"A2":0.55,"A3":0.75,"A4":0.05,"A5":0.00},
        "13 Linux":               {"A1":0.70,"A2":0.55,"A3":0.70,"A4":0.60,"A5":0.55},
        "14 Ordre réformé":       {"A1":0.75,"A2":0.50,"A3":0.65,"A4":0.70,"A5":0.25},
        "15 Physique théorique":  {"A1":0.70,"A2":0.55,"A3":0.65,"A4":0.55,"A5":0.60},
    }

    print("\n" + "=" * 130)
    print("COMPARAISON V2 → V2.1 (écarts)")
    print("=" * 130)
    print(f"{'Système':28s} | {'δA1':>5s} {'δA2':>5s} {'δA3':>5s} {'δA4':>5s} {'δA5':>5s} | {'δΔ23':>6s} {'δΔ45':>6s} | Stable?")
    print("-" * 130)

    for name in results:
        r = results[name]
        v = v2_scores[name]
        diffs = {k: round(r[k] - v[k], 2) for k in ["A1", "A2", "A3", "A4", "A5"]}

        v_D23 = round(v["A2"] - v["A3"], 2)
        v_D45 = round(v["A4"] - v["A5"], 2)
        dD23 = round(r["D23"] - v_D23, 2)
        dD45 = round(r["D45"] - v_D45, 2)

        # Check if regime is stable (same sign for key deltas)
        same_D23_sign = (r["D23"] >= 0) == (v_D23 >= 0) or abs(r["D23"]) < 0.10 or abs(v_D23) < 0.10
        same_D45_regime = True
        if v_D45 >= 0.40 and r["D45"] < 0.30:
            same_D45_regime = False
        if v_D45 <= 0.05 and r["D45"] > 0.20:
            same_D45_regime = False

        stable = "✓" if same_D23_sign and same_D45_regime else "⚠"

        print(f"{name:28s} | {diffs['A1']:+5.2f} {diffs['A2']:+5.2f} {diffs['A3']:+5.2f} "
              f"{diffs['A4']:+5.2f} {diffs['A5']:+5.2f} | {dD23:+6.2f} {dD45:+6.2f} | {stable}")


if __name__ == "__main__":
    results = compute_all()
    compare_v2(results)
