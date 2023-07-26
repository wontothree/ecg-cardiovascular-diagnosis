import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyClassifier
from sklearn.metrics import classification_report
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('diabetes_prediction_dataset1.csv')

y_data = df.pop('diabetes')
x_data = df

# 수동 시각화
# print(df.head())
# print(df.info()) # 데이터 프레임 정보
# print(df.nunique()) # 유니크한 값 정보

# AutoViz를 이용한 자동 시각화
# plt.style.use('dark_background')

# AV = AutoViz_Class()

# AV.AutoViz(
#     filename='',
#     dfte=df,
#     depVar='diabetes',
#     verbose=2, # 0: 간단히 표시; 1: 자세히 표시; 2: 파일로 저장
#     max_rows_analyzed=df.shape[0],
#     max_cols_analyzed=df.shape[1])

# 데이터
x_train, x_test, y_train, y_test = train_test_split(
    x_data,
    y_data,
    test_size=0.2,
    random_state=2022,
    stratify=y_data) 

# 모델 성능 비교
# clf = LazyClassifier(verbose=0, predictions=True)
# models, predictions = clf.fit(x_train, x_test, y_train, y_test)
# print(models) # 모델별 성능 비교
# print(predictions.head()) # 모델별 테스트 데이터 예측값

# 모델별 분류 리포트
# for model_name in predictions.columns.tolist():
#     print(f'{model_name}')
#     print(classification_report(y_test, predictions[model_name]))


# LightGBM Model
lgbm = LGBMClassifier()

lgbm.fit(x_train, y_train)

y_pred = lgbm.predict(x_test)

accuracy_score(y_pred, y_test)