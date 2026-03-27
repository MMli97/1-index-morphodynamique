"""
Index des Formes Conceptuelles Dynamiques — Classifieur V0

Classifieur projectif explicable basé sur des polytopes dans [0,1]^5.
Chaque forme est définie par des contraintes linéaires + invariants de signature.
La classification est traçable : on sait quelles contraintes sont violées et de combien.

Axes :
  A1 - Complexité organisationnelle
  A2 - Couplage structurel interne
  A3 - Intégration informationnelle
  A4 - Normativité régulatoire
  A5 - Capacité de révision interne
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Tuple, Optional

Vec = Dict[str, float]  # {"A1": 0.7, "A2": 0.3, ...}


@dataclass
class Constraint:
    """Une contrainte g(x) <= 0 quand satisfaite."""
    name: str
    g: Callable[[Vec], float]
    weight: float = 1.0


@dataclass
class Transition:
    """Une transition possible vers une autre forme."""
    target: str
    condition: str
    surface: str  # description formelle de la surface de franchissement


@dataclass
class Form:
    """Une forme = région dans [0,1]^5 définie par contraintes."""
    id: str
    name: str
    constraints: List[Constraint]
    signature_description: str = ""
    transitions: List[Transition] = field(default_factory=list)


# ─────────────────────────────────────────────
# Violation et distance
# ─────────────────────────────────────────────

def violation(c: Constraint, x: Vec) -> float:
    """Violation pondérée d'une contrainte. 0 si satisfaite."""
    return c.weight * max(0.0, c.g(x))


def distance_to_form(F: Form, x: Vec) -> float:
    """Distance totale pondérée aux contraintes d'une forme."""
    return sum(violation(c, x) for c in F.constraints)


def margin(c: Constraint, x: Vec) -> float:
    """Marge : négatif = satisfait (plus c'est négatif, plus c'est dedans)."""
    return c.g(x)


def explain(F: Form, x: Vec, top_k: int = 6) -> List[Dict]:
    """Explique la classification : contraintes violées + marges."""
    results = []
    for c in F.constraints:
        v = violation(c, x)
        m = margin(c, x)
        results.append({
            "constraint": c.name,
            "violated": v > 0,
            "violation": round(v, 4),
            "margin": round(m, 4),
            "weight": c.weight
        })
    # Trier : violations d'abord (desc), puis marges (desc = plus serré)
    results.sort(key=lambda r: (-r["violation"], r["margin"]))
    return results[:top_k]


def classify(forms: List[Form], x: Vec) -> Dict:
    """Classifie un point dans la forme la plus proche."""
    scored = []
    for F in forms:
        d = distance_to_form(F, x)
        scored.append((F.id, F.name, d, F))
    scored.sort(key=lambda t: t[2])

    best_id, best_name, best_d, best_F = scored[0]
    result = {
        "best_form": best_id,
        "best_form_name": best_name,
        "best_distance": round(best_d, 4),
        "inside": best_d == 0.0,
        "explanation": explain(best_F, x),
    }
    if len(scored) > 1:
        result["runner_up"] = scored[1][0]
        result["runner_up_name"] = scored[1][1]
        result["runner_up_distance"] = round(scored[1][2], 4)
    if len(scored) > 2:
        result["third"] = scored[2][0]
        result["third_name"] = scored[2][1]
        result["third_distance"] = round(scored[2][2], 4)

    return result


def profile_all(forms: List[Form], x: Vec) -> List[Dict]:
    """Donne la distance à toutes les formes, triées."""
    scored = []
    for F in forms:
        d = distance_to_form(F, x)
        scored.append({
            "form": F.id,
            "name": F.name,
            "distance": round(d, 4),
            "inside": d == 0.0
        })
    scored.sort(key=lambda r: r["distance"])
    return scored


# ─────────────────────────────────────────────
# Définition des 6 formes (polytopes V0)
# ─────────────────────────────────────────────

def make_F01() -> Form:
    """F01 — Homéostasie"""
    return Form(
        id="F01",
        name="Homéostasie",
        signature_description="Δ₂₃ ≤ 0.15 (propagation ≈ intégration), Δ₄₅ ≤ 0.25 (normativité ≈ révision)",
        constraints=[
            # Contraintes de zone
            Constraint("A2 >= 0.35", lambda x: 0.35 - x["A2"]),
            Constraint("A2 <= 0.65", lambda x: x["A2"] - 0.65),
            Constraint("A3 >= 0.45", lambda x: 0.45 - x["A3"]),
            Constraint("A3 <= 0.75", lambda x: x["A3"] - 0.75),
            Constraint("A4 >= 0.35", lambda x: 0.35 - x["A4"]),
            Constraint("A4 <= 0.65", lambda x: x["A4"] - 0.65),
            Constraint("A5 >= 0.25", lambda x: 0.25 - x["A5"]),
            Constraint("A5 <= 0.55", lambda x: x["A5"] - 0.55),
            Constraint("A1 <= 0.65", lambda x: x["A1"] - 0.65),
            # Invariants de signature
            Constraint("sig: Δ₂₃ = A2-A3 ≤ 0.15",
                        lambda x: (x["A2"] - x["A3"]) - 0.15, weight=2.0),
            Constraint("sig: Δ₄₅ = A4-A5 ≤ 0.25",
                        lambda x: (x["A4"] - x["A5"]) - 0.25, weight=2.0),
        ],
        transitions=[
            Transition("F03", "Perturbations > capacité de compensation",
                       "Δ₂₃ franchit 0.15 vers le haut"),
            Transition("F05", "Bande de fonctionnement se rétrécit",
                       "A4 ↑ au-delà de 0.65 avec A5 stable"),
            Transition("F02", "Surplus au-delà du maintien",
                       "A1 ↑, A2 ↑"),
        ]
    )


def make_F03() -> Form:
    """F03 — Crise"""
    return Form(
        id="F03",
        name="Crise",
        signature_description="Δ₂₃ ≥ 0.30 (propagation sans stabilisation), A4 débordé",
        constraints=[
            Constraint("A2 >= 0.65", lambda x: 0.65 - x["A2"]),
            Constraint("A3 <= 0.35", lambda x: x["A3"] - 0.35),
            Constraint("A4 <= 0.40", lambda x: x["A4"] - 0.40),
            # Invariants de signature
            Constraint("sig: Δ₂₃ = A2-A3 ≥ 0.30",
                        lambda x: 0.30 - (x["A2"] - x["A3"]), weight=2.0),
            Constraint("sig: normativité inefficace A3-A4 ≤ 0.10",
                        lambda x: (x["A3"] - x["A4"]) - 0.10, weight=1.5),
        ],
        transitions=[
            Transition("F01", "Perturbations cessent + structure intacte",
                       "Δ₂₃ redescend sous 0.15"),
            Transition("F08", "Régulation irrémédiablement détruite",
                       "A3 ↓ sous 0.30, A2 ↓ sous 0.30"),
            Transition("F06", "Crise provoque réorganisation supérieure",
                       "A5 franchit 0.60 avec A3 ↑"),
        ]
    )


def make_F04() -> Form:
    """F04 — Saturation"""
    return Form(
        id="F04",
        name="Saturation",
        signature_description="Δ₃₅ ≥ 0.25 (intégration sans révision), Δ₁₂ ≥ 0.20 (profondeur sans propagation)",
        constraints=[
            Constraint("A1 >= 0.65", lambda x: 0.65 - x["A1"]),
            Constraint("A2 >= 0.20", lambda x: 0.20 - x["A2"]),
            Constraint("A2 <= 0.55", lambda x: x["A2"] - 0.55),
            Constraint("A3 >= 0.45", lambda x: 0.45 - x["A3"]),
            Constraint("A3 <= 0.75", lambda x: x["A3"] - 0.75),
            Constraint("A4 >= 0.40", lambda x: 0.40 - x["A4"]),
            Constraint("A4 <= 0.75", lambda x: x["A4"] - 0.75),
            Constraint("A5 <= 0.25", lambda x: x["A5"] - 0.25),
            # Invariants de signature
            Constraint("sig: Δ₃₅ = A3-A5 ≥ 0.25",
                        lambda x: 0.25 - (x["A3"] - x["A5"]), weight=2.0),
            Constraint("sig: Δ₁₂ = A1-A2 ≥ 0.20",
                        lambda x: 0.20 - (x["A1"] - x["A2"]), weight=2.0),
        ],
        transitions=[
            Transition("F05", "Saturation maintenue → sur-normativité",
                       "A4 franchit 0.65 avec A5 ≤ 0.25"),
            Transition("F06", "Rupture de symétrie",
                       "A5 ↑ au-delà de 0.60"),
            Transition("F03", "Pression destructrice sur les limites",
                       "A2 ↑ au-delà de 0.55, A3 ↓"),
        ]
    )


def make_F05() -> Form:
    """F05 — Rigidification"""
    return Form(
        id="F05",
        name="Rigidification",
        signature_description="Δ₄₅ ≥ 0.45 (normativité sans révision), Δ₄₃ ≥ 0.10 (norme > cohérence)",
        constraints=[
            Constraint("A4 >= 0.65", lambda x: 0.65 - x["A4"]),
            Constraint("A5 <= 0.25", lambda x: x["A5"] - 0.25),
            Constraint("A2 <= 0.40", lambda x: x["A2"] - 0.40),
            Constraint("A3 >= 0.40", lambda x: 0.40 - x["A3"]),
            # Invariants de signature
            Constraint("sig: Δ₄₅ = A4-A5 ≥ 0.45",
                        lambda x: 0.45 - (x["A4"] - x["A5"]), weight=2.0),
            Constraint("sig: Δ₄₃ = A4-A3 ≥ 0.10",
                        lambda x: 0.10 - (x["A4"] - x["A3"]), weight=1.5),
        ],
        transitions=[
            Transition("F03", "Perturbation brise la rigidité",
                       "A2 franchit 0.40, A4 ↓"),
            Transition("F08", "Inadaptation fatale",
                       "A3 ↓ sous 0.30, A2 ↓ sous 0.30"),
            Transition("F01", "Retrouve plasticité (rare)",
                       "A5 ↑ au-delà de 0.25, Δ₄₅ ↓"),
        ]
    )


def make_F06() -> Form:
    """F06 — Individuation"""
    return Form(
        id="F06",
        name="Individuation",
        signature_description="A5 > A4 (révision dépasse normativité), propagation stabilisée",
        constraints=[
            Constraint("A5 >= 0.60", lambda x: 0.60 - x["A5"]),
            Constraint("A3 >= 0.45", lambda x: 0.45 - x["A3"]),
            Constraint("A2 >= 0.45", lambda x: 0.45 - x["A2"]),
            Constraint("A4 <= 0.60", lambda x: x["A4"] - 0.60),
            # Invariants de signature
            Constraint("sig: A5-A4 ≥ 0.10",
                        lambda x: 0.10 - (x["A5"] - x["A4"]), weight=2.0),
            Constraint("sig: A2-A3 ≤ 0.10",
                        lambda x: (x["A2"] - x["A3"]) - 0.10, weight=1.5),
        ],
        transitions=[
            Transition("F01", "Individuation se stabilise",
                       "A5 ↓ sous 0.55, Δ₄₅ ≤ 0.25"),
            Transition("F04", "Tensions épuisées",
                       "A5 ↓, A1 ↑"),
            Transition("F07", "Forme individuée produit du transmissible",
                       "Ouverture au milieu ↑ (axe futur)"),
        ]
    )


def make_F08() -> Form:
    """F08 — Dissolution fonctionnelle"""
    return Form(
        id="F08",
        name="Dissolution fonctionnelle",
        signature_description="Δ₄₃ ≥ 0.30 (norme sans intégration), Δ₁₂ ≥ 0.25 (structure inerte)",
        constraints=[
            Constraint("A3 <= 0.30", lambda x: x["A3"] - 0.30),
            Constraint("A2 <= 0.30", lambda x: x["A2"] - 0.30),
            Constraint("A5 <= 0.20", lambda x: x["A5"] - 0.20),
            Constraint("A1 >= 0.55", lambda x: 0.55 - x["A1"]),
            Constraint("A4 >= 0.50", lambda x: 0.50 - x["A4"]),
            # Invariants de signature
            Constraint("sig: Δ₄₃ = A4-A3 ≥ 0.30",
                        lambda x: 0.30 - (x["A4"] - x["A3"]), weight=2.0),
            Constraint("sig: Δ₁₂ = A1-A2 ≥ 0.25",
                        lambda x: 0.25 - (x["A1"] - x["A2"]), weight=2.0),
        ],
        transitions=[
            Transition("F06", "Composants se réorganisent",
                       "A5 ↑, A3 ↑, A2 ↑"),
        ]
    )


# ─────────────────────────────────────────────
# Registre des formes
# ─────────────────────────────────────────────

def all_forms() -> List[Form]:
    """Retourne toutes les formes définies."""
    return [make_F01(), make_F03(), make_F04(), make_F05(), make_F06(), make_F08()]


# ─────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────

def test_ministere():
    """Test sur le Ministère de l'Éducation nationale (profil du premier test)."""
    x = {"A1": 0.7, "A2": 0.3, "A3": 0.4, "A4": 0.7, "A5": 0.15}
    forms = all_forms()

    print("=" * 60)
    print("TEST : Ministère de l'Éducation nationale")
    print(f"Profil : {x}")
    print("=" * 60)

    # Distances à toutes les formes
    print("\nDistances à toutes les formes :")
    for entry in profile_all(forms, x):
        marker = " ← INSIDE" if entry["inside"] else ""
        print(f"  {entry['form']} ({entry['name']:25s}) : d = {entry['distance']:.4f}{marker}")

    # Classification
    result = classify(forms, x)
    print(f"\nClassification : {result['best_form']} ({result['best_form_name']})")
    print(f"  Distance : {result['best_distance']}")
    print(f"  Inside : {result['inside']}")
    if result.get("runner_up"):
        print(f"  Runner-up : {result['runner_up']} ({result['runner_up_name']}) @ {result['runner_up_distance']}")
    if result.get("third"):
        print(f"  Third : {result['third']} ({result['third_name']}) @ {result['third_distance']}")

    # Explication
    print("\nExplication (contraintes les plus violées / serrées) :")
    for e in result["explanation"]:
        status = "VIOLÉE" if e["violated"] else "ok"
        print(f"  [{status:6s}] {e['constraint']:40s} violation={e['violation']:.4f}  marge={e['margin']:.4f}")


def test_cases():
    """Tests sur plusieurs systèmes contrastés."""
    cases = {
        "Ministère Éducation": {"A1": 0.7, "A2": 0.3, "A3": 0.4, "A4": 0.7, "A5": 0.15},
        "Startup hypercroissance": {"A1": 0.3, "A2": 0.7, "A3": 0.3, "A4": 0.2, "A5": 0.5},
        "Démocratie constitutionnelle": {"A1": 0.7, "A2": 0.5, "A3": 0.6, "A4": 0.5, "A5": 0.7},
        "Thermostat": {"A1": 0.1, "A2": 0.3, "A3": 0.5, "A4": 0.5, "A5": 0.0},
        "LLM (inférence)": {"A1": 0.9, "A2": 0.6, "A3": 0.7, "A4": 0.1, "A5": 0.0},
        "Organisme malade": {"A1": 0.5, "A2": 0.8, "A3": 0.2, "A4": 0.2, "A5": 0.3},
        "Cellule homéostatique": {"A1": 0.4, "A2": 0.6, "A3": 0.6, "A4": 0.5, "A5": 0.3},
        "Dogme doctrinal": {"A1": 0.4, "A2": 0.2, "A3": 0.5, "A4": 0.8, "A5": 0.0},
    }

    forms = all_forms()

    print("=" * 70)
    print("BATTERIE DE TESTS")
    print("=" * 70)

    for name, x in cases.items():
        result = classify(forms, x)
        profile = profile_all(forms, x)
        top3 = profile[:3]
        print(f"\n{name}")
        print(f"  Profil : A1={x['A1']} A2={x['A2']} A3={x['A3']} A4={x['A4']} A5={x['A5']}")
        print(f"  → {result['best_form']} ({result['best_form_name']}) [d={result['best_distance']}]", end="")
        if result["inside"]:
            print(" ★ INSIDE", end="")
        print()
        for t in top3:
            flag = "●" if t["inside"] else "○"
            print(f"    {flag} {t['form']} ({t['name']:25s}) d={t['distance']:.4f}")


if __name__ == "__main__":
    test_ministere()
    print("\n\n")
    test_cases()
