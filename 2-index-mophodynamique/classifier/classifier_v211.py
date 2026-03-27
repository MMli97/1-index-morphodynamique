"""
Index des Formes Conceptuelles Dynamiques — Classifieur V2

V2 implements the two-level classification proposed in the structural analysis:
  Level 1: Typing by gradients (Δ₂₃, Δ₄₅, Δ₁₂, Δ₃₅, Δ₄₃)
  Level 2: Intensity qualification by absolute axes

Key changes from V1:
  - Forms defined primarily by gradient conditions (Δ), not absolute thresholds
  - Absolute axes used as secondary qualifiers (intensity/density of regime)
  - Broadened polytopes to accommodate the 15-case test battery
  - Explicit handling of overlap zones (F04∩F05, F01∩F06)
  - New form F09 (Architecture pure) for zero-normativity systems like LLMs

Axes:
  A1 - Complexité organisationnelle
  A2 - Couplage structurel interne
  A3 - Intégration informationnelle
  A4 - Normativité régulatoire
  A5 - Capacité de révision interne

Gradients:
  Δ₂₃ = A2 - A3  (couplage vs intégration)
  Δ₄₅ = A4 - A5  (normativité vs révision)
  Δ₁₂ = A1 - A2  (profondeur vs propagation)
  Δ₃₅ = A3 - A5  (intégration vs révision)
  Δ₄₃ = A4 - A3  (normativité vs intégration)
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Tuple, Optional

Vec = Dict[str, float]


def compute_deltas(x: Vec) -> Dict[str, float]:
    """Compute all structural gradients."""
    return {
        "D23": x["A2"] - x["A3"],
        "D45": x["A4"] - x["A5"],
        "D12": x["A1"] - x["A2"],
        "D35": x["A3"] - x["A5"],
        "D43": x["A4"] - x["A3"],
    }


@dataclass
class Constraint:
    name: str
    g: Callable[[Vec, Dict[str, float]], float]  # takes (x, deltas)
    weight: float = 1.0
    level: str = "gradient"  # "gradient" or "absolute"


@dataclass
class Transition:
    target: str
    condition: str
    surface: str


@dataclass
class Form:
    id: str
    name: str
    constraints: List[Constraint]
    signature: str = ""
    transitions: List[Transition] = field(default_factory=list)


# ─────────────────────────────────────────────
# Core functions
# ─────────────────────────────────────────────

def violation(c: Constraint, x: Vec, d: Dict[str, float]) -> float:
    return c.weight * max(0.0, c.g(x, d))


def distance_to_form(F: Form, x: Vec, d: Dict[str, float]) -> float:
    total = sum(violation(c, x, d) for c in F.constraints)
    return round(total, 10)  # avoid float artifacts


def explain(F: Form, x: Vec, d: Dict[str, float], top_k: int = 8) -> List[Dict]:
    results = []
    for c in F.constraints:
        v = violation(c, x, d)
        m = c.g(x, d)
        results.append({
            "constraint": c.name,
            "level": c.level,
            "violated": v > 0,
            "violation": round(v, 4),
            "margin": round(m, 4),
            "weight": c.weight
        })
    results.sort(key=lambda r: (-r["violation"], r["margin"]))
    return results[:top_k]


def classify(forms: List[Form], x: Vec) -> Dict:
    d = compute_deltas(x)
    scored = []
    for F in forms:
        dist = distance_to_form(F, x, d)
        scored.append((F.id, F.name, dist, F))
    scored.sort(key=lambda t: t[2])

    best_id, best_name, best_d, best_F = scored[0]
    result = {
        "best_form": best_id,
        "best_form_name": best_name,
        "best_distance": round(best_d, 4),
        "inside": best_d == 0.0,
        "deltas": {k: round(v, 2) for k, v in d.items()},
        "explanation": explain(best_F, x, d),
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
    d = compute_deltas(x)
    scored = []
    for F in forms:
        dist = distance_to_form(F, x, d)
        scored.append({
            "form": F.id, "name": F.name,
            "distance": round(dist, 4), "inside": dist == 0.0
        })
    scored.sort(key=lambda r: r["distance"])
    return scored


# ─────────────────────────────────────────────
# V2 Form definitions
# ─────────────────────────────────────────────

def make_F01() -> Form:
    """F01 — Équilibre différentiel (Homéostasie)
    Primary: Δ₂₃ controlled, Δ₄₅ moderate
    Secondary: moderate absolute levels, A5 > 0
    """
    return Form("F01", "Équilibre différentiel", signature="Δ₂₃ ≤ 0.15, Δ₄₅ ≤ 0.30",
        constraints=[
            # Level 1: Gradient conditions (primary)
            Constraint("Δ₂₃ ≤ 0.15 (propagation ≈ intégration)",
                       lambda x, d: d["D23"] - 0.15, weight=2.5, level="gradient"),
            Constraint("Δ₄₅ ≤ 0.30 (normativité ≈ révision)",
                       lambda x, d: d["D45"] - 0.30, weight=2.5, level="gradient"),
            # Level 2: Absolute qualifiers (secondary)
            Constraint("A3 ≥ 0.40 (intégration suffisante)",
                       lambda x, d: 0.40 - x["A3"], weight=1.0, level="absolute"),
            Constraint("A4 ≥ 0.25 (normativité présente)",
                       lambda x, d: 0.25 - x["A4"], weight=1.0, level="absolute"),
            Constraint("A5 ≥ 0.15 (révision non nulle)",
                       lambda x, d: 0.15 - x["A5"], weight=1.0, level="absolute"),

        ],
        transitions=[
            Transition("F03", "Δ₂₃ franchit 0.15 ↑", "Propagation dépasse intégration"),
            Transition("F05", "Δ₄₅ franchit 0.30 ↑", "Normativité creuse l'écart avec révision"),
        ])


def make_F03() -> Form:
    """F03 — Sur-couplage (Crise)
    Primary: Δ₂₃ high (propagation >> integration)
    Secondary: A4 low (normativity overwhelmed)
    """
    return Form("F03", "Sur-couplage", signature="Δ₂₃ ≥ 0.25",
        constraints=[
            Constraint("Δ₂₃ ≥ 0.25 (propagation >> intégration)",
                       lambda x, d: 0.25 - d["D23"], weight=2.5, level="gradient"),
            Constraint("A4 ≤ 0.50 (normativité débordée)",
                       lambda x, d: x["A4"] - 0.50, weight=1.0, level="absolute"),
            Constraint("A2 ≥ 0.55 (couplage réel)",
                       lambda x, d: 0.55 - x["A2"], weight=1.0, level="absolute"),
        ],
        transitions=[
            Transition("F01", "Δ₂₃ ↓ sous 0.15", "Intégration rattrape propagation"),
            Transition("F06", "A5 ↑ > 0.50", "Révision émerge de la crise"),
            Transition("F08", "A3 ↓ < 0.30, A2 ↓", "Dissolution"),
        ])


def make_F04() -> Form:
    """F04 — Plateau inertiel (Saturation)
    Primary: Δ₃₅ high (integration without revision), Δ₁₂ high (depth without propagation)
    Secondary: A1 high, A5 low
    """
    return Form("F04", "Plateau inertiel", signature="Δ₃₅ ≥ 0.35, Δ₁₂ ≥ 0.15",
        constraints=[
            Constraint("Δ₃₅ ≥ 0.35 (intégration sans révision)",
                       lambda x, d: 0.35 - d["D35"], weight=2.5, level="gradient"),
            Constraint("Δ₁₂ ≥ 0.15 (profondeur sans propagation)",
                       lambda x, d: 0.15 - d["D12"], weight=2.0, level="gradient"),
            Constraint("A1 ≥ 0.60 (complexité élevée)",
                       lambda x, d: 0.60 - x["A1"], weight=1.0, level="absolute"),
            Constraint("A5 ≤ 0.30 (révision faible)",
                       lambda x, d: x["A5"] - 0.30, weight=1.0, level="absolute"),
        ],
        transitions=[
            Transition("F05", "Δ₄₅ ↑ > 0.40", "Sur-normativité"),
            Transition("F06", "A5 ↑ > 0.50", "Rupture de symétrie"),
        ])


def make_F05() -> Form:
    """F05 — Dominance normative (Rigidification)
    Primary: Δ₄₅ high (normativity >> revision)
    Secondary: A4 elevated
    """
    return Form("F05", "Dominance normative", signature="Δ₄₅ ≥ 0.40",
        constraints=[
            Constraint("Δ₄₅ ≥ 0.40 (normativité >> révision)",
                       lambda x, d: 0.40 - d["D45"], weight=2.5, level="gradient"),
            Constraint("A4 ≥ 0.45 (normativité substantielle)",
                       lambda x, d: 0.45 - x["A4"], weight=1.5, level="absolute"),
            Constraint("A5 ≤ 0.30 (révision faible)",
                       lambda x, d: x["A5"] - 0.30, weight=1.0, level="absolute"),
        ],
        transitions=[
            Transition("F03", "A2 ↑ brise la rigidité", "Perturbation externe"),
            Transition("F08", "A3 ↓ + A2 ↓", "Dissolution fonctionnelle"),
        ])


def make_F06() -> Form:
    """F06 — Inversion normative (Individuation)
    Primary: Δ₄₅ negative or near zero (A5 ≥ A4), Δ₂₃ controlled
    Secondary: A5 elevated, A3 sufficient
    """
    return Form("F06", "Inversion normative", signature="Δ₄₅ ≤ 0.05, A5 ≥ 0.50",
        constraints=[
            Constraint("Δ₄₅ ≤ 0.05 (révision ≥ normativité)",
                       lambda x, d: d["D45"] - 0.05, weight=2.5, level="gradient"),
            Constraint("Δ₂₃ ≤ 0.15 (propagation stabilisée)",
                       lambda x, d: d["D23"] - 0.15, weight=2.0, level="gradient"),
            Constraint("A5 ≥ 0.50 (révision active)",
                       lambda x, d: 0.50 - x["A5"], weight=1.5, level="absolute"),
            Constraint("A3 ≥ 0.45 (intégration suffisante)",
                       lambda x, d: 0.45 - x["A3"], weight=1.0, level="absolute"),
        ],
        transitions=[
            Transition("F01", "Δ₄₅ ↑ vers 0.20, A5 ↓", "Stabilisation"),
        ])


def make_F08() -> Form:
    """F08 — Dissolution fonctionnelle
    Primary: Δ₄₃ high (norm without integration), Δ₁₂ high (structure without coupling)
    Secondary: A3 low, A2 low
    """
    return Form("F08", "Dissolution fonctionnelle", signature="Δ₄₃ ≥ 0.25, Δ₁₂ ≥ 0.20",
        constraints=[
            Constraint("Δ₄₃ ≥ 0.25 (norme sans intégration)",
                       lambda x, d: 0.25 - d["D43"], weight=2.5, level="gradient"),
            Constraint("Δ₁₂ ≥ 0.20 (structure sans couplage)",
                       lambda x, d: 0.20 - d["D12"], weight=2.0, level="gradient"),
            Constraint("A3 ≤ 0.40 (intégration effondrée)",
                       lambda x, d: x["A3"] - 0.40, weight=1.5, level="absolute"),
            Constraint("A5 ≤ 0.20 (révision nulle)",
                       lambda x, d: x["A5"] - 0.20, weight=1.0, level="absolute"),
        ],
        transitions=[
            Transition("F06", "A5 ↑, A3 ↑", "Recombinaison"),
        ])


def make_F09() -> Form:
    """F09 — Architecture pure (systèmes à normativité nulle)
    For systems like LLMs in inference: high complexity, high integration,
    but zero normativity and zero revision. No internal correction mechanism.
    """
    return Form("F09", "Architecture pure", signature="A4 ≤ 0.15, A5 ≤ 0.10, A3 ≥ 0.50",
        constraints=[
            Constraint("A4 ≤ 0.15 (normativité quasi nulle)",
                       lambda x, d: x["A4"] - 0.15, weight=2.0, level="absolute"),
            Constraint("A5 ≤ 0.10 (révision nulle)",
                       lambda x, d: x["A5"] - 0.10, weight=2.0, level="absolute"),
            Constraint("A3 ≥ 0.50 (intégration présente)",
                       lambda x, d: 0.50 - x["A3"], weight=1.5, level="absolute"),
            Constraint("A1 ≥ 0.60 (complexité élevée)",
                       lambda x, d: 0.60 - x["A1"], weight=1.0, level="absolute"),
            Constraint("Δ₄₃ ≤ -0.40 (intégration >> normativité)",
                       lambda x, d: d["D43"] - (-0.40), weight=2.0, level="gradient"),
        ],
        transitions=[
            Transition("F04", "A4 ↑ (normativité imposée ex.)", "Fine-tuning / RLHF"),
            Transition("F06", "A5 ↑ (auto-modification)", "Self-play / meta-learning"),
        ])


def all_forms() -> List[Form]:
    return [make_F01(), make_F03(), make_F04(), make_F05(),
            make_F06(), make_F08(), make_F09()]


# ─────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────

def test_battery():
    cases = {
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

    forms = all_forms()

    print("=" * 120)
    print("CLASSIFIEUR V2 — Batterie de 15 cas")
    print("=" * 120)
    print(f"{'Système':28s} | {'Best':5s} {'d':>5s} | {'2nd':5s} {'d':>5s} | {'3rd':5s} {'d':>5s} | In | Δ23    Δ45    Δ12    Δ43")
    print("-" * 120)

    inside_count = 0
    for name, x in cases.items():
        d = compute_deltas(x)
        result = classify(forms, x)
        prof = profile_all(forms, x)
        inside = "★" if result["inside"] else " "
        if result["inside"]:
            inside_count += 1
        print(f"{name:28s} | {prof[0]['form']:5s} {prof[0]['distance']:5.3f} | "
              f"{prof[1]['form']:5s} {prof[1]['distance']:5.3f} | "
              f"{prof[2]['form']:5s} {prof[2]['distance']:5.3f} | "
              f"{inside:2s} | {d['D23']:+5.2f}  {d['D45']:+5.2f}  {d['D12']:+5.2f}  {d['D43']:+5.2f}")

    print(f"\nInside: {inside_count}/15")


if __name__ == "__main__":
    test_battery()
