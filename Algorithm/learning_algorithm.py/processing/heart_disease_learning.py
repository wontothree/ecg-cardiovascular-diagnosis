import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('Algorithm/data/heart_disease_dataset.csv')
y_data = df.pop('target')
x_data = df

lgbm = LGBMClassifier()
lgbm.fit(x_data, y_data)

y_prob = lgbm.predict_proba(x_data)
print(y_prob)

lgbm.booster_.save_model('heart_disease_prediction_model.txt')







# print(y_pred)
# print(y_prob)
# print(accuracy_score(y_pred, y_test))



# from sklearn.svm import SVC
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler

# X_train = pd.DataFrame(x_train)
# X_test = pd.DataFrame(x_test)

# pipe = Pipeline(steps=[
#     ("preprocessor", StandardScaler()),
#     ("classifier", SVC())
# ])

# pipe.fit(x_train, y_train)
# y_pred = pipe.predict(x_test)
# # print(accuracy_score(y_pred, y_test))
