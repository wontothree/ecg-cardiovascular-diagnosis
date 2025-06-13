import lightgbm

# 미리 학습된 모델 불러오기
model = lightgbm.Booster(model_file='Algorithm/ml_models/heart_disease_prediction_model.txt')

# 사용자 입력 받기
age = 38
sex = 1
cp = 120
trestbps = 231
chol = 0
fbs = 1
restecg = 182 # resting electrocardiographic results # 0, 1, 2
thalach = 130 # 최대심박수 # 71 ~ 202 일반적인 계산 공식 220 - 나이
exang = 3.8
oldpeak = 1 # oldpeak = ST depression induced by exercise relative to rest # 0 ~ 6.2
slope = 0 # the slope of the peak exercise ST segment - 운동 중에 측정되는 ST 세그먼트의 기울기 # 1 ~ 3
ca = 3
thal = 0


# 입력 데이터를 2D 배열로 구성하여 모델에 전달
input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
pred = model.predict(input_data)

print("OO님 심장질환에 걸릴 확률: ", pred[0] * 100, '%')
