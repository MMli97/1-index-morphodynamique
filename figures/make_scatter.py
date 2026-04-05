import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from style import apply_style, REGIME_COLORS

apply_style()

systems = [
    ("Eukaryotic cell",       -0.15, +0.30, "F01"),
    ("Thermostat",            -0.05, +0.50, "F05"),
    ("NYSE",                  +0.25, +0.10, "F03"),
    ("Adaptive immunity",     -0.05, +0.10, "F01"),
    ("Catholic Church",       -0.05, +0.65, "F04"),
    ("Fifth Republic",        +0.05, +0.20, "F01"),
    ("Multicellular org.",    -0.10, +0.45, "F04"),
    ("Authoritarian regime",  +0.20, +0.75, "F05"),
    ("Supply chain",          +0.35, +0.20, "F03"),
    ("Apple Inc.",            -0.05, +0.20, "F01"),
    ("TikTok",                +0.10, +0.10, "F01"),
    ("Static LLM",            -0.20, +0.05, "F04"),
    ("Linux",                 -0.15, +0.05, "F01"),
    ("Reformed order",        -0.15, +0.45, "F04"),
    ("Theor. physics",        -0.10, -0.05, "F01"),
]

# Manual offsets (dx, dy in points) to resolve overlapping labels
label_offsets = {
    "Multicellular org.": (-85, +8),
    "Reformed order":     (-75, -12),
    "Static LLM":         (-70, -8),
    "Linux":              (+7, -10),
    "Apple Inc.":         (-65, -8),
    "Adaptive immunity":  (+7, -10),
}
default_offset = (7, 5)

fig, ax = plt.subplots(figsize=(10, 7.5))

for name, d23, d45, regime in systems:
    c = REGIME_COLORS.get(regime, "#666")
    ax.scatter(d23, d45, c=c, s=110, zorder=3, edgecolors="white", linewidths=0.5)
    dx, dy = label_offsets.get(name, default_offset)
    ax.annotate(name, (d23, d45), textcoords="offset points", xytext=(dx, dy),
                fontsize=8.5, color="#333",
                arrowprops=dict(arrowstyle="-", color="#ccc", lw=0.5) if abs(dx) > 20 else None)

ax.axhline(0, color="grey", lw=0.5, ls="--")
ax.axvline(0, color="grey", lw=0.5, ls="--")
ax.axvspan(0.18, 0.23, alpha=0.08, color="orange")
ax.axhline(0.40, color="#E45756", lw=0.7, ls=":", alpha=0.5)
ax.axhline(0.05, color="#F58518", lw=0.7, ls=":", alpha=0.5)

ax.set_xlabel(r"$\Delta_{23}$ (Propagation $-$ Integration)", fontsize=12)
ax.set_ylabel(r"$\Delta_{45}$ (Normativity $-$ Revision)", fontsize=12)
ax.set_title("Distribution of systems in gradient space (V2.1.2)", fontsize=14)

legend = [Line2D([0],[0],marker='o',color='w',markerfacecolor=REGIME_COLORS[r],markersize=9,label=r)
          for r in ["F01","F03","F04","F05"]]
legend.append(plt.Rectangle((0,0),1,1, fc="orange", alpha=0.15, label="F01/F03 grey zone"))
ax.legend(handles=legend, title="Regime classification", loc="upper left", framealpha=0.9, fontsize=9)
ax.set_xlim(-0.28, 0.42)
ax.set_ylim(-0.12, 0.82)
plt.tight_layout()
plt.savefig("scatter_gradient_space.pdf", dpi=200)
plt.savefig("scatter_gradient_space.png", dpi=200)
print("Saved scatter_gradient_space.pdf/.png")
