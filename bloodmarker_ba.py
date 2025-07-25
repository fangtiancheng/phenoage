from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class BloodMarker:
    age: float
    albumin: float
    alkaline_phosphatase: float
    urea: float
    cholesterol: float
    creatinine: float
    cystatin_c: float
    glycated_haemoglobin: float
    log_c_reactive_protein: float
    log_gamma_glutamyltransf: float
    red_blood_cell_erythrocyte_count: float
    mean_corpuscular_volume: float
    red_blood_cell_erythrocyte_distribution_width: float
    monocyte_count: float
    neutrophill_count: float
    lymphocyte_percentage: float
    mean_sphered_cell_volume: float
    log_alanine_aminotransfe: float
    log_shbg: float
    log_vitamin_d: float
    high_light_scatter_reticulocyte_percentage: float
    glucose: float
    platelet_distribution_width: float
    mean_corpuscular_haemoglobin: float
    platelet_crit: float
    apolipoprotein_a: float
    sexM: float


# 字典：特征名 → (SexAge 模型系数, ENET 模型系数, 训练集均值)
BLOOD_MARKER_COEFS: Dict[str, Tuple[float, float, float]] = {
    "age": (0.100432393, 0.074763266, 56.0487752),
    "albumin": (0.0, -0.011331946, 45.1238763),
    "alkaline_phosphatase": (0.0, 0.00164946, 82.6847975),
    "urea": (0.0, -0.029554872, 5.3547152),
    "cholesterol": (0.0, -0.0805656, 5.6177437),
    "creatinine": (0.0, -0.01095746, 71.565605),
    "cystatin_c": (0.0, 1.859556436, 0.900946),
    "glycated_haemoglobin": (0.0, 0.018116675, 35.4785711),
    "log_c_reactive_protein": (0.0, 0.079109916, 0.3003624),
    "log_gamma_glutamyltransf": (0.0, 0.265550311, 3.3795613),
    "red_blood_cell_erythrocyte_count": (0.0, -0.204442153, 4.4994648),
    "mean_corpuscular_volume": (0.0, 0.017165356, 91.9251099),
    "red_blood_cell_erythrocyte_distribution_width": (0.0, 0.202009895, 13.4342296),
    "monocyte_count": (0.0, 0.36937314, 0.4746987),
    "neutrophill_count": (0.0, 0.06679092, 4.1849454),
    "lymphocyte_percentage": (0.0, -0.0108158, 28.5817604),
    "mean_sphered_cell_volume": (0.0, 0.006736204, 83.6363269),
    "log_alanine_aminotransfe": (0.0, -0.312442261, 3.077868),
    "log_shbg": (0.0, 0.292323186, 3.8202787),
    "log_vitamin_d": (0.0, -0.265467867, 3.6052878),
    "high_light_scatter_reticulocyte_percentage": (0.0, 0.169234165, 0.3988152),
    "glucose": (0.0, 0.032171478, 4.9563054),
    "platelet_distribution_width": (0.0, 0.071527711, 16.4543576),
    "mean_corpuscular_haemoglobin": (0.0, 0.02746487, 31.8396206),
    "platelet_crit": (0.0, -1.329561046, 0.2385396),
    "apolipoprotein_a": (0.0, -0.185139395, 1.5238771),
    "sexM": (0.51779499, 0.557512185, 0.0),
}

def bloodmarker_ba_esitmation(blood_marker: BloodMarker) -> float:
    marker_dict = blood_marker.__dict__
    marker_dict = {k: v for k, v in marker_dict.items() if k != "sexM"}
    delta_sum = 0.0
    for feat, value in marker_dict.items():
        coef_null, coef_enet, feat_mean = BLOOD_MARKER_COEFS[feat]
        delta_sum += (value - feat_mean) * (coef_enet - coef_null)
    return delta_sum * 10

if __name__ == '__main__':
    sample = BloodMarker(
        age=68,
        sexM=1,                         
        albumin=46.59,
        alkaline_phosphatase=66.1,
        urea=8.77,
        cholesterol=4.047,
        creatinine=105.2,
        cystatin_c=1.212,
        glycated_haemoglobin=41.2,
        log_c_reactive_protein=0.8754687,
        log_gamma_glutamyltransf=3.580737,
        red_blood_cell_erythrocyte_count=4.17,
        mean_corpuscular_volume=89.2,
        red_blood_cell_erythrocyte_distribution_width=14.8,
        monocyte_count=0.5,
        neutrophill_count=6.7,
        lymphocyte_percentage=11.7,
        mean_sphered_cell_volume=80.6,
        log_alanine_aminotransfe=2.98214,
        log_shbg=3.404525,
        log_vitamin_d=4.592085,
        high_light_scatter_reticulocyte_percentage=0.35,
        glucose=4.641,
        platelet_distribution_width=15.7,
        mean_corpuscular_haemoglobin=30.3,
        platelet_crit=0.298,
        apolipoprotein_a=1.647
    )
    baa = bloodmarker_ba_esitmation(sample)
    print(f"Biological Age Acceleration = {baa:.2f} years")
