import pandas as pd

from sklearn.model_selection import train_test_split

from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('Algorithm/Data/heart_disease_dataset.csv')
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
y_pred = lgbm.predict(x_test) # 심장병의 유무
y_prob = lgbm.predict_proba(x_test) # 심장병이 있을 확률
# print(y_pred)
# print(y_prob)
# print(accuracy_score(y_pred, y_test))



from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X_train = pd.DataFrame(x_train)
X_test = pd.DataFrame(x_test)

pipe = Pipeline(steps=[
    ("preprocessor", StandardScaler()),
    ("classifier", SVC())
])

pipe.fit(x_train, y_train)
y_pred = pipe.predict(x_test)
# print(accuracy_score(y_pred, y_test))
