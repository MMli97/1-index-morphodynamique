# Morphodynamic Index

This repository contains the code, data, and figure-generation scripts associated with the preprint:

**Toward a Gradient-Based Classification Space for Heterogeneous Complex Systems**

## Contents

- `index/` — classifier and regime definitions

- `data/` — empirical case tables and classifier version tables

- `figures/` — scripts to reproduce the figures

- `paper/` — PDF of the preprint

- `tests/` — minimal validation scripts

## Quick start

Create a virtual environment and install dependencies:

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Generate figures :

python figures/make_scatter.py

python figures/make_heatmap.py

python figures/make_pipeline.py

python figures/make_phase_space.py



## Purpose :

The repository provides an exploratory implementation of a gradient-based classifier for comparing heterogeneous complex systems across biological, institutional, technological, and economic domains.
