import lightgbm

# 기존의 inbody 데이터 (사용하지 않으므로 주석 처리)
# inbody_data = [1.72, 21, 1, 52.9, 2.2, 2.8, 2.84, 8.76, 8.84]

# 기존의 변수들 (사용하지 않으므로 주석 처리)
# height = inbody_data[0]
# age = inbody_data[1]
# sex = inbody_data[2]
# lean_fat_mass = inbody_data[3]
# body_fat_mass = inbody_data[4]
# right_arm_mass = inbody_data[5]
# left_arm_mass = inbody_data[6]
# right_leg_mass = inbody_data[7]
# left_leg_mass = inbody_data[8]

# lbm = lean_fat_mass
# bfm = body_fat_mass

# 미리 학습된 모델 불러오기
model = lightgbm.Booster(model_file='Algorithm/ml_models/cardiovascular_disease_prediction_based_inbodydataset.txt')

# 사용자 입력 받기
age = int(input("1. 나이: "))
age = age * 365
sex = int(input("2. 성별(여: 1, 남: 2): "))
height = int(input("키(cm): "))
weight = int(input("몸무게(kg): "))

sbp = 110
dbp = 80
chol = 1
gluc = 1

smoke = int(input("담배여부(x: 0, o: 1): "))
alchol = int(input("술여부(x: 0, o: 1): "))
active = int(input("활동여부(x: 0, o: 1)"))

bfm = float(input("체지방(kg): "))
lbm = float(input("제지방(kg): "))

# 입력 데이터를 2D 배열로 구성하여 모델에 전달
input_data = [[age, sex, height, weight, sbp, dbp, chol, gluc, smoke, alchol, active, bfm, lbm]]
predicted_bodyfat_percent = model.predict(input_data)

print("김세원님 심장질환에 걸릴 확률:", predicted_bodyfat_percent)
