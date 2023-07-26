import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')

y_data = df.pop('target')
x_data = df

x_train, x_test, y_train, y_test = train_test_split(
    x_data,
    y_data,
    test_size=0.2,
    random_state=2022,
    stratify=y_data) # 클래스 비율을 동일하게 분할한다

lgbm = LGBMClassifier()

lgbm.fit(x_train, y_train)

y_pred = lgbm.predict(x_test)

print(y_pred) # 심장병이 있는지 0 또는 1로 판단한다.