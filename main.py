from dataclasses import dataclass
import math

@dataclass
class PhenoAgeInput:
    """
    所有字段均使用 Levine et al. 2018 原文单位
    ------------------------------------------------
    age                : 实际年龄，岁
    albumin            : 血清白蛋白，单位 g/L   （原文为 g/L）
    creatinine         : 血清肌酐，单位 µmol/L  （原文为 µmol/L）
    glucose            : 空腹血糖，单位 mmol/L  （原文为 mmol/L）
    crp                : C-反应蛋白，单位 mg/L  （原文为 mg/dL，需取 ln）
    lymphocyte_pct     : 淋巴细胞百分比，%      （原文为 %）
    mcv                : 平均红细胞体积，fL     （原文为 fL）
    rdw                : 红细胞分布宽度，%      （原文为 %）
    alkaline_phosphatase : 碱性磷酸酶，单位 U/L （原文为 U/L）
    wbc                : 白细胞计数，单位 10⁹/L （原文为 10⁹ cells/L）
    """
    age: float
    albumin: float
    creatinine: float
    glucose: float
    crp: float
    lymphocyte_pct: float
    mcv: float
    rdw: float
    alkaline_phosphatase: float
    wbc: float

def pheno_age(data: PhenoAgeInput) -> float:
    """
    根据 Levine et al. 2018 原始系数计算 PhenoAge（年）
    所有单位必须与 PhenoAgeInput 注释一致，不可再转换
    """
    # 1. 构建线性组合 xb（所有变量保持原文单位）
    xb = (
        -19.907
        - 0.0336 * data.albumin            # g/L
        + 0.0095 * data.creatinine         # µmol/L
        + 0.1953 * data.glucose            # mmol/L
        + 0.0954 * math.log(0.1*data.crp)  # mg/L → ln(mg/dL)
        - 0.0120 * data.lymphocyte_pct     # %
        + 0.0268 * data.mcv                # fL
        + 0.3306 * data.rdw                # %
        + 0.0019 * data.alkaline_phosphatase  # U/L
        + 0.0554 * data.wbc                # 10⁹/L
        + 0.0804 * data.age                # 岁
    )

    # 2. Gompertz 参数
    gamma = 0.0076927
    M = 1 - math.exp(
        -math.exp(xb) * (math.exp(120 * gamma) - 1) / gamma
    )

    # 3. 计算最终 PhenoAge（年）
    pheno_age = 141.50225 + math.log(-0.00553 * math.log(1 - M)) / 0.090165
    return pheno_age


if __name__ == "__main__":
    sample = PhenoAgeInput(
        age=24,
        albumin=49.5,           # g/L
        creatinine=71.3,        # µmol/L
        glucose=4.9,            # mmol/L
        crp=0.5,                # mg/L
        lymphocyte_pct=49.2,    # %
        mcv=91.6,               # fL
        rdw=12.2,               # %
        alkaline_phosphatase=51,# U/L
        wbc=3.9                 # 10⁹/L
    )
    print("PhenoAge =", round(pheno_age(sample), 2), "years")
