import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from style import apply_style

apply_style()

fig, ax = plt.subplots(figsize=(12, 2.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 1)
ax.axis("off")

boxes = [
    (0.5, "Input vector\n$(A_1, A_2, A_3, A_4, A_5)$"),
    (2.8, "Gradient computation\n$\\Delta_{23}=A_2-A_3$\n$\\Delta_{45}=A_4-A_5$\n$\\Delta_{12}=A_1-A_2$"),
    (5.6, "Regime constraints\n(F01 .. F09)"),
    (8.0, "Constraint-distance\nclassifier\n$\\hat{F}(x) = \\arg\\min_F d_F(x)$"),
]

for x, text in boxes:
    bbox = dict(boxstyle="round,pad=0.4", facecolor="#f8f8f8", edgecolor="#999", lw=1.2)
    ax.text(x, 0.5, text, fontsize=10, ha="center", va="center", bbox=bbox)

for x1, x2 in [(1.45, 1.85), (4.0, 4.4), (6.6, 7.0)]:
    ax.annotate("", xy=(x2, 0.5), xytext=(x1, 0.5),
                arrowprops=dict(arrowstyle="->", color="#555", lw=1.5))

ax.set_title("Classifier pipeline", fontsize=13, pad=5)
plt.tight_layout()
plt.savefig("classifier_pipeline.pdf", dpi=200)
plt.savefig("classifier_pipeline.png", dpi=200)
print("Saved classifier_pipeline.pdf/.png")
