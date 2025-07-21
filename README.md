# PhenoAge

A drop-in Python implementation of the **2018 Levine Phenotypic Age** calculator (a.k.a. PhenoAge).  
Compute your biological age in one line of code.

---

📄 **Original Papers**  
1. Levine ME, Lu AT, Quach A, *et al.* **An epigenetic biomarker of aging for lifespan and healthspan**. *Aging (Albany NY)*. 2018 Apr 18;10(4):573-591. DOI: [10.18632/aging.101414](https://doi.org/10.18632/aging.101414) | PubMed: [29676998](https://pubmed.ncbi.nlm.nih.gov/29676998/)  
2. Chen F, Tang Y, *et al.* **Early-life exposure to tobacco, genetic susceptibility, and accelerated biological aging in adulthood**. *Med*. 2024. DOI: [10.1016/j.medj.2024.05.006](https://doi.org/10.1016/j.medj.2024.05.006) | PMC: [PMC11068008](https://pmc.ncbi.nlm.nih.gov/articles/PMC11068008/)

---

```python
from phenoage import pheno_age, PhenoAgeInput

# Example: 40-year-old male
p = PhenoAgeInput(
    age=40, albumin=42, creatinine=88, glucose=5.3,
    crp=0.5, lymphocyte_pct=30, mcv=90, rdw=13,
    alkaline_phosphatase=70, wbc=6.5
)
print("PhenoAge =", pheno_age(p), "years")
```

---

## 📋 Input Specification  
| Parameter | Unit | Description |
|---|---|---|
| `age` | years | Chronological age |
| `albumin` | g/L | Serum albumin |
| `creatinine` | µmol/L | Serum creatinine |
| `glucose` | mmol/L | Fasting plasma glucose |
| `crp` | mg/L | C-reactive protein |
| `lymphocyte_pct` | % | Lymphocyte percentage |
| `mcv` | fL | Mean cell volume |
| `rdw` | % | Red cell distribution width |
| `alkaline_phosphatase` | U/L | Alkaline phosphatase |
| `wbc` | 10⁹/L | White blood cell count |

---

## 🙏 Related Projects & Ports
| Language/Platform | Repo | Notes |
|---|---|---|
| **R (CRAN)** | [AnthropoAgeR](https://github.com/oyaxbell/AnthropoAgeR) | Full AnthropoAge + PhenoAge + S-AnthropoAge |
| **R (Streamlit)** | [hillarylinmd/phenoage](https://github.com/hillarylinmd/phenoage) | Paste raw lab text → get age |
| **JavaScript** | [DPUSystems/PhenoAge](https://github.com/DPUSystems/PhenoAge) | Client-side browser calculator |

---

## 📄 License

MIT © 2025 FangTiancheng