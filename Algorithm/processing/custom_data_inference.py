import lightgbm

# 미리 학습된 모델 불러오기
model = lightgbm.Booster(model_file='Algorithm/ml_models/custom_data_prediction.txt')

# 사용자 입력 받기
age = int(input("1. 나이: "))
age = age * 365
sex = int(input("2. 성별(여: 1, 남: 2): "))
height = int(input("3. 키(cm): "))
bfm = float(input("4. 체지방량(kg): "))
lbm = float(input("5. 제지방량(kg): "))

input_data = [[age, sex, height, bfm, lbm]]
pred = model.predict(input_data)
print("OO님 심장질환에 걸릴 확률:", pred)
