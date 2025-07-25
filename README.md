# PhenoAge + Blood-Biomarker ENC  

Drop-in Python implementations of two validated biological-age clocks:  

1) **2018 Levine PhenoAge**  
2) **2023 Nature Full-ENC blood-biomarker clock**  

Compute biological age or Biological Age Acceleration (BAA) in one line of code.

## 📄 **Original Papers**  

1. Levine ME, Lu AT, Quach A, *et al.* **An epigenetic biomarker of aging for lifespan and healthspan**. *Aging (Albany NY)*. 2018 Apr 18;10(4):573-591. DOI: [10.18632/aging.101414](https://doi.org/10.18632/aging.101414) | PubMed: [29676998](https://pubmed.ncbi.nlm.nih.gov/29676998/)  
2. Chen F, Tang Y, *et al.* **Early-life exposure to tobacco, genetic susceptibility, and accelerated biological aging in adulthood**. *Med*. 2024. DOI: [10.1016/j.medj.2024.05.006](https://doi.org/10.1016/j.medj.2024.05.006) | PMC: [PMC11068008](https://pmc.ncbi.nlm.nih.gov/articles/PMC11068008/)
3. Bortz J, Guariglia A, Klaric L, *et al.* **Biological age estimation using circulating blood biomarkers**. *Commun Biol*. 2023 Oct 26;6:1089. DOI: [10.1038/s42003-023-05456-z](https://doi.org/10.1038/s42003-023-05456-z) | GitHub implementation: [bortzjd/bloodmarker_BA_estimation](https://github.com/bortzjd/bloodmarker_BA_estimation)

## 📋 Input Specification  

### PhenoAge

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

### Blood-Biomarker ENC  

| Parameter                                       | Unit        | Description                                     |
| ----------------------------------------------- | ----------- | ----------------------------------------------- |
| `age`                                           | years       | Chronological age                               |
| `albumin`                                       | g/L         | Serum albumin                                   |
| `alkaline_phosphatase`                          | U/L         | Alkaline phosphatase                            |
| `urea`                                          | mmol/L      | Blood urea nitrogen (BUN)                       |
| `cholesterol`                                   | mmol/L      | Total cholesterol                               |
| `creatinine`                                    | µmol/L      | Serum creatinine                                |
| `cystatin_c`                                    | mg/L        | Serum cystatin C                                |
| `glycated_haemoglobin`                          | mmol/mol    | HbA1c                                           |
| `log_c_reactive_protein`                        | log(mg/L)   | Log-transformed C-reactive protein              |
| `log_gamma_glutamyltransf`                      | log(U/L)    | Log-transformed gamma-glutamyltransferase (GGT) |
| `red_blood_cell_erythrocyte_count`              | 10¹²/L      | Red blood cell (RBC) count                      |
| `mean_corpuscular_volume`                       | fL          | Mean corpuscular volume (MCV)                   |
| `red_blood_cell_erythrocyte_distribution_width` | %           | Red cell distribution width (RDW)               |
| `monocyte_count`                                | 10⁹/L       | Monocyte count                                  |
| `neutrophill_count`                             | 10⁹/L       | Neutrophil count                                |
| `lymphocyte_percentage`                         | %           | Lymphocyte percentage                           |
| `mean_sphered_cell_volume`                      | fL          | Mean sphered cell volume (MSCV)                 |
| `log_alanine_aminotransfe`                      | log(U/L)    | Log-transformed alanine aminotransferase (ALT)  |
| `log_shbg`                                      | log(nmol/L) | Log-transformed sex hormone-binding globulin    |
| `log_vitamin_d`                                 | log(nmol/L) | Log-transformed 25-hydroxyvitamin D             |
| `high_light_scatter_reticulocyte_percentage`    | %           | High light scatter reticulocyte percentage      |
| `glucose`                                       | mmol/L      | Fasting plasma glucose                          |
| `platelet_distribution_width`                   | %           | Platelet distribution width (PDW)               |
| `mean_corpuscular_haemoglobin`                  | pg          | Mean corpuscular haemoglobin (MCH)              |
| `platelet_crit`                                 | %           | Platelet crit (PCT)                             |
| `apolipoprotein_a`                              | g/L         | Apolipoprotein A-I                              |
| `sexM`                                          | binary      | Sex (1 = male, 0 = female)                      |

---

## 🙏 Related Projects & Ports
| Language/Platform | Repo | Notes |
|---|---|---|
| **R (CRAN)** | [AnthropoAgeR](https://github.com/oyaxbell/AnthropoAgeR) | Full AnthropoAge + PhenoAge + S-AnthropoAge |
| **R (Streamlit)** | [hillarylinmd/phenoage](https://github.com/hillarylinmd/phenoage) | Paste raw lab text → get age |
| **JavaScript** | [DPUSystems/PhenoAge](https://github.com/DPUSystems/PhenoAge) | Client-side browser calculator |
| **R** | [bortzjd/bloodmarker_BA_estimation](https://github.com/bortzjd/bloodmarker_BA_estimation) | Official implementation of Blood-Biomarker ENC |

---

## 📄 License

MIT © 2025 FangTiancheng