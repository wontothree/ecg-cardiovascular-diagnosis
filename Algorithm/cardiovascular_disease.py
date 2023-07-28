from sklearn.metrics import classification_report
from lazypredict.Supervised import LazyClassifier
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd

# 키(m), 나이(만), 성별(0: 여, 1: 남), 제지방량(kg), 체지방량(kg), 오른팔 근육량(kg), 왼팔 근육량(kg), 오른다리 근육량(kg), 왼다리 근육량(kg)
inbody_data = [1.72, 21, 1, 52.9, 2.2, 2.8, 2.84, 8.76, 8.84]

height = inbody_data[0]
age = inbody_data[1]
sex = inbody_data[2]
lean_fat_mass = inbody_data[3]
body_fat_mass = inbody_data[4]
right_arm_mass = inbody_data[5]
left_arm_mass = inbody_data[6]
right_leg_mass = inbody_data[7]
left_leg_mass = inbody_data[8]

# Lean Body Mass Index, Appendicular Skeletal Muscle Mass Index, Body Fat Mass Index(체지방 질량 지수)
lbm = lean_fat_mass
bfm = body_fat_mass
asm = right_arm_mass + left_arm_mass + right_leg_mass + left_leg_mass

lbmi = lean_fat_mass / (height * height)
asmi = (right_arm_mass + left_arm_mass +
        right_leg_mass + left_leg_mass) / (height * height)
bfmi = body_fat_mass / (height * height)

# age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio, lbm, bfm, asm, hrv
# data = [18393, 2, 168, 62.0, 110, 80, 1, 1, 0, 0, 1, 0, 100, 10, 2.3]

df = pd.read_csv('cardio_train_copy.csv')
y_data = df.pop('cardio')
x_data = df

# 데이터
x_train, x_test, y_train, y_test = train_test_split(
    x_data,
    y_data,
    test_size=0.2,
    random_state=2022,
    stratify=y_data)

# LightGBM Model
lgbm = LGBMClassifier()
lgbm.fit(x_train, y_train)
y_pred = lgbm.predict(x_test)
accuracy_score(y_pred, y_test)

# 확률로 출력
prob_test = lgbm.predict_proba(y_test) # y_test 변경해야 함

print(prob_test[:,1])
