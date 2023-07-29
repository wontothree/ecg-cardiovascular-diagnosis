import pandas as pd
import numpy as np

from lightgbm import LGBMRegressor
import lightgbm

import csv

df = pd.read_csv('Algorithm/Data/cardiovascular_disease_dataset.csv')
cardiovascular_disease_dataset = df.values.tolist()

# 샘플 데이터 추출
data = []
data_target = []
for i in range(10000):
    data_string = cardiovascular_disease_dataset[i][0]
    data_list = data_string.split(';')
    data_list = [int(item) if item.isdigit() else float(item) for item in data_list]
    data.append(data_list)
    data_target.append(data_list[12])

for i in data: # [age(days), sex, height(cm), weight(kg)]
    i.pop(0)
    i.pop(1)
    i.pop(3)
    i.pop(3)
    i.pop(3)
    i.pop(3)
    i.pop(3)
    i.pop(3)
    i.pop(3)
    i.pop(3)

processed_data = [] # [age, height(inches), weight(lbs)]
for i in data:
    i[0] = i[0] // 365
    i[1] = i[1] * 0.393701
    i[2] = i[2] * 2.20462
    processed_data.append(i)


# 반지도 학습을 이용하여 나이(years), 키(inches), 몸무게(lbs)로 체지방을 예측하는 모델만들기
df = pd.read_csv('Algorithm/Data/bodyfat_dataset.csv')
bodyfat_dataset = df.values.tolist()

processed_bodyfat_data = [] # 학습 데이터 [percent body fat, age(years), weight[lbs], height(inches)]
for i in bodyfat_dataset:
    i = i[1:5]
    processed_bodyfat_data.append(i)

processed_bodyfat_data = np.array(processed_bodyfat_data)

# Separate features (x_data) and labels (y_data)
x_data = processed_bodyfat_data[:, 1:]  # Select all columns except the first one (target column)
y_data = processed_bodyfat_data[:, 0]   # Select the first column as the target

# Create and train the LightGBM model for regression
lgbm = LGBMRegressor()
lgbm.fit(x_data, y_data)
predicted_percent_bodyfat = lgbm.predict(data)


for i, j in zip(processed_data, predicted_percent_bodyfat):
    i.append(j)

for i, j in zip(processed_data, data):
    bfm = i[3] * i[2] * 0.01 / 2.20462
    lbm = i[2] / 2.20462 - bfm
    i.pop()
    i.append(bfm)
    i.append(lbm)


for i, j in zip(data, data_target):
    i.append(j)

print(data)

f = open('Algorithm/data/custom_data.csv', 'w')
writer = csv.writer(f)
# writer.writerows(data)
f.close()