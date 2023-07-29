# HRV + Body Composition Data

- 지도 학습
- 배치 학습
- 모델 기반 학습

ECG Data -> Heart Disease 여부 -> 심장병 여부 + BMI(Inbody Data) -> 당뇨병

## Heart Disease

https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

## Diabetes

https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset?resource=download

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

1. Id
2. Age (days)
3. Sex (Women: 1, Men: 2)
4. Height (cm)
5. Weight (kg)
6. Systolic blood pressure - 수축기 혈압: 심장이 수축하고 매박동마다 혈액을 밀어내는 동안 동맥 내부의 최대 압력
7. Diastolic blood pressure - 이완기 혈압: 심장이 수축하지 않고 휴식하는 동안 동맥 내부의 최소 압력
8. Cholesterol (1: normal, 2: above normal, 3: well above normal)
9. Gluc (1: normal, 2: above normal, 3: well above normal)
10. Smoke (0 or 1)
11. Alchol (0 or 1)
12. Active (0 or 1)
13. Cardiovascular (0 or 1) - Target Value

### 인바디 데이터 예측 모델 - Body Fat Prediction

https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset

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

### Heart Disease Prediction

https://www.kaggle.com/datasets/utkarshx27/heart-disease-diagnosis-dataset

1. age
2. sex
3. chest pain type  (4 values)
4. resting blood pressure - 안정혈압
5. serum cholestoral in mg/dl - 콜레스테롤: 몸의 모든 세포막과 혈관벽을 구성하는 데 사용되며, 지방 흡수에 필요한 담즙산을 형성하고, 성호르몬, 부신피질호르몬과 같은 필수적인 호르몬을 만드는 물질
6. fasting blood sugar > 120 mg/dl - 공복혈당
7. resting electrocardiographic results (values 0,1,2) - the electrical activity of your heart while you are at rest v
8. maximum heart rate achieved
9. exercise induced angina - 운동부하에 의한 심근허혈: 관동맥의 의미있는 협 착을 의미하면서 심근 경색이나 심인성 사망을 예측할 수 있게되나 좌심실 기능 부전은 운동부하에 의한 허 혈뿐만 아니라 이미 존재하던 좌심실의 손상이 심각하 게 있었거나 다시 발생된 것을 의미
10. oldpeak = ST depression induced by exercise relative to rest - 운동에 의해 유발된 ST 세그먼트 우울증을 휴식 상태와 비교한 것 v
11. the slope of the peak exercise ST segment - 운동 중에 측정되는 ST 세그먼트의 기울기 v
12. number of major vessels (0-3) colored by flourosopy
13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
14. Target(Absence (1) or presence (2) of heart disease)

"oldpeak = ST depression induced by exercise relative to rest"라는 문장은 의료 용어로서 'oldpeak'가 운동에 의해 유발된 ST 세그먼트 우울증을 휴식 상태와 비교한 것을 의미합니다. 이를 자세히 설명하겠습니다.

ST 세그먼트는 심전도 검사에서 기록되는 한 구간으로, 심장의 전기 활동을 반영하는 중요한 정보를 제공합니다. ST 세그먼트 우울증은 ST 세그먼트가 휴식 상태에 비해 운동 중에 아래로 향하는 현상을 의미합니다. 이는 일반적으로 심장 근육 부족으로 인해 특정 부위의 혈액 공급이 감소되어 발생합니다.

ST 세그먼트 우울증은 운동 전후에 비교하여 측정됩니다. "oldpeak"는 이러한 우울증의 크기를 의미하며, 일반적으로 밀리미터 (mm)로 측정됩니다. 우울증의 깊이가 클수록 심장 근육에 대한 혈액 공급이 부족할 가능성이 높으며, 이는 관상 동맥 질환(CAD) 또는 다른 심장 질환의 가능성을 나타낼 수 있습니다.

심장 검사 결과를 올바로 이해하고 적절한 진단과 치료 계획을 수립하기 위해서는 해당 검사 결과뿐만 아니라 환자의 임상 기록과 다른 진단적 정보를 종합적으로 고려하는 것이 중요합니다. 이러한 결과를 분석하고 해석하는 데는 심장과 전문적인 의료 전문가들이 필요합니다.
.

"Peak exercise ST segment의 slope"는 운동 중에 측정되는 ST 세그먼트의 기울기를 의미합니다. 이는 일반적으로 심전도 검사(Exercise Electrocardiogram 또는 Stress Test)를 통해 평가되며, 심장 기능을 평가하고 심장 문제를 진단하는 데 도움이 됩니다.

ST 세그먼트는 심전도에서 기록되는 한 구간을 의미합니다. 이는 심부전과 같은 심장 문제를 감지하는 데 도움이 되는 중요한 정보를 제공합니다. Peak exercise ST segment의 기울기는 ST 세그먼트의 변화 추이를 나타내며, 일반적으로 다음과 같이 분류될 수 있습니다:

Positive Slope (양의 기울기): 운동이 진행됨에 따라 ST 세그먼트가 위로 올라가는 경향을 보입니다. 이는 정상적인 반응일 수 있으나 심장 동맥의 흐름이 부족한 동맥 질환을 가진 환자에서는 협심증을 나타낼 수 있습니다.

Flat Slope (평평한 기울기): 운동 중에 ST 세그먼트가 수평 상태를 유지합니다. 이는 심장에 미치는 부하가 부족하거나 환자가 어떤 심장 문제를 겪고 있을 수 있음을 나타낼 수 있습니다.

Negative Slope (음의 기울기): 운동 중에 ST 세그먼트가 아래로 기울어지는 경향을 보입니다. 이는 흔히 협심증과 관련이 있을 수 있으며, 특히 심장 동맥의 흐름이 부족한 상태에서 나타날 수 있습니다.

ST 세그먼트의 기울기 평가는 의사가 심장 건강을 평가하고 심장 이벤트의 가능성을 파악하는 데 도움이 됩니다. 그러나 최종적인 진단은 전문의가 다른 검사와 증상과 함께 고려하여 내릴 수 있습니다. 따라서 어떤 심장 검사든 의사와 상담하고 그들의 지시에 따라 진행하는 것이 중요합니다.

## 최종 데이터 양식

1. Age (days)
2. Sex (Women: 1, Men: 2)
3. Height (cm)
4. Systolic blood pressure
5. Diastolic blood pressure
6. Cholesterol (1: normal, 2: above normal, 3: well above normal)
7. Gluc (1: normal, 2: above normal, 3: well above normal)
8. Smoke (0 or 1)
9. Alchol (0 or 1)
10. Active (0 or 1)
11. bfm
12. lbm

데이터

1. Age (days)
2. Sex (Women: 1, Men: 2)
3. Height (cm)
4. bfm
5. lbm

## 의학 개념

- Cardiovascular Disease (심혈관질환): 심혈관질환은 심장과 혈관에 영향을 미치는 다양한 질환들을 포괄하는 범주입니다. 이에는 심장질환 뿐만 아니라 혈관질환도 포함됩니다. 주요한 심혈관질환에는 심장질환(심근경색, 심부전 등), 뇌졸중, 말초동맥질환 등이 포함됩니다. 즉, 심혈관질환은 심장 및 혈관에 영향을 미치는 다양한 질병을 통칭하는 개념입니다.
- Heart Disease (심장질환): 심장질환은 심장에 직접 영향을 미치는 질환들을 말합니다. 주로 심장의 구조, 기능, 혈액 공급 등과 관련된 질병들을 포함합니다. 대표적인 심장질환에는 심근경색, 심부전, 심전도 이상 등이 있습니다. 심장질환은 심혈관질환에 포함되지만, 심혈관질환은 심장질환 뿐만 아니라 혈관 질환도 포괄하는 더 큰 범주입니다.
- "Cardiovascular Disease"는 심장과 혈관에 영향을 미치는 다양한 질환들을 의미하는 범주이며, 이 중에 "Heart Disease"는 심장에 직접 영향을 미치는 질환들을 특정한 의미로 포함하는 개념입니다.
