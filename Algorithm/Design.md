# HRV + Body Composition Data

- 지도 학습
- 배치 학습
- 모델 기반 학습

ECG Data -> Heart Disease 여부 -> 심장병 여부 + BMI(Inbody Data) -> 당뇨병

## Heart Disease

https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

## Diabetes

https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?resource=download

=============================================================================================

## Cardiovascular Disease(심혈관질환)

1. 심근경색증: 심근경색증은 심장 근육에 혈액 공급이 감소하거나 차단되어 심근 조직 손상을 초래하는 상태를 말합니다. 일반적으로 혈관 내에서 혈전이 형성되어 심장 동맥을 막는 경우에 발생합니다.
2. 심부전: 심부전은 심장이 제대로 작동하지 않아 심장이 혈액을 효과적으로 움직이지 못하는 상태를 말합니다. 이로 인해 체내의 적절한 혈압과 혈류가 유지되지 않을 수 있습니다.
3. 뇌졸중: 뇌졸중은 뇌 혈관이 혈전으로 막히거나 파열되어 뇌에 혈액 공급이 제한되어 뇌 조직 손상을 초래하는 상태를 말합니다.
4. 고혈압: 고혈압은 동맥의 혈압이 정상 범위를 초과하여 지속적으로 높은 상태를 말합니다. 만약 적절히 관리되지 않으면 심혈관계 질환 위험이 증가할 수 있습니다.
5. 동맥경화: 동맥경화는 혈관 벽에 지방 및 칼슘이 쌓여 혈관 내부 지름이 좁아지는 상태를 말합니다. 이로 인해 혈액의 흐름이 방해되어 심혈관질환을 유발할 수 있습니다.

Changes in predicted lean body mass, appendicular skeletal muscle mass, and body fat mass and cardiovascular disease

- Lean body mass(LBM, 마른체질량): 체지방량을 고려하지 않고 순수한 근육량을 기준으로 측정하는 체질량지수 LBMI = 체중 (kg) / (신장(m) ^ 2) * (1 - 체지방률)
- Appendicular skeletal muscle mass(ASM, 부록골격근육량): 지방량을 제외하고 상체와 하체의 근육량만을 고려하여 측정하는 체질량 지수 ASMI = (상체 근육량 + 하체 근육량) / 신장(m)^2 (kg/m^2)
- Body fat mass(BFM, 체지방량): 체지방량을 고려하여 측정하는 체질량 지수 BFMI = 체지방량 (kg) / (신장(m) ^ 2) (kg/m^2)

### 기본 모델 - Cardiovascular Disease Prediction

https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset

data

1. Id
2. Age(days)
3. Sex(Women: 1, Men: 2)
4. Height(cm)
5. Weight(kg)
6. Systolic blood pressure
7. Diastolic blood pressure
8. Cholesterol(1: normal, 2: above normal, 3: well above normal)
9. Gluc(1: normal, 2: above normal, 3: well above normal)
10. Smoke(0 or 1)
11. Alchol(0 or 1)
12. Active(0 or 1)
13. Cardiovascular(0 or 1) - Target Value

### 인바디 데이터 예측 모델 - Body Fat Prediction

https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset

data

1. Density determined from underwater weighing
2. Percent body fat from Siri's (1956) equation
3. Age (years)
4. Weight (lbs)
5. Height (inches)
6. Neck circumference (cm)
7. Chest circumference (cm)
8. Abdomen 2 circumference (cm)
9. Hip circumference (cm)
10. Thigh circumference (cm)
11. Knee circumference (cm)
12. Ankle circumference (cm)
13. Biceps (extended) circumference (cm)
14. Forearm circumference (cm)
15. Wrist circumference (cm)
