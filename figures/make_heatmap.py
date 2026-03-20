import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from style import apply_style

apply_style()

regime_versions = [
    ["Eukaryotic cell",      "F01","F01","F01","F01"],
    ["Thermostat",           "F05","F05","F05","F05"],
    ["NYSE",                 "F03","F03","F03","F03"],
    ["Adaptive immunity",    "F01","F01","F01","F01"],
    ["Catholic Church",      "F04","F04","F04","F04"],
    ["Fifth Republic",       "F01","F01","F01","F01"],
    ["Multicellular org.",   "F04","F04","F04","F04"],
    ["Authoritarian regime", "F05","F05","F05","F05"],
    ["Supply chain",         "F03","F03","F03","F03"],
    ["Apple Inc.",           "F01","F01","F01","F01"],
    ["TikTok",               "F01","F01","F01","F01"],
    ["Static LLM",           "F04","F04","F04","F04"],
    ["Linux",                "F01","F01","F01","F01"],
    ["Reformed order",       "F04","F04","F04","F04"],
    ["Theor. physics",       "F01","F01","F01","F01"],
]

regime_to_num = {"F01":0, "F03":1, "F04":2, "F05":3, "F06":4}
cmap = mcolors.ListedColormap(["#4C78A8","#2F4B7C","#8F77B5","#E45756","#F58518"])

n_sys = len(regime_versions)
versions = ["V1","V2","V2.1.1","V2.1.2"]
data = np.array([[regime_to_num[r] for r in row[1:]] for row in regime_versions])

fig, ax = plt.subplots(figsize=(9, 8))
ax.imshow(data, cmap=cmap, aspect="auto", vmin=0, vmax=4)
for i in range(n_sys):
    for j in range(4):
        ax.text(j, i, regime_versions[i][j+1], ha="center", va="center",
                fontsize=10, color="white", fontweight="bold")

ax.set_xticks(range(4))
ax.set_xticklabels(versions, fontsize=11)
ax.set_yticks(range(n_sys))
ax.set_yticklabels([r[0] for r in regime_versions], fontsize=10)
ax.set_title("Evolution of the classification instrument across versions", fontsize=13, pad=12)
ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True)
plt.tight_layout()
plt.savefig("classifier_heatmap.pdf", dpi=200)
plt.savefig("classifier_heatmap.png", dpi=200)
print("Saved classifier_heatmap.pdf/.png")
