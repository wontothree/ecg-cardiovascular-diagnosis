import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier

# [age, sex(women: 1, men: 2), height(cm), bfm(kg), lbm(kg), target]
data = pd.read_csv('Algorithm/data/custom_data.csv')

x_data = data.iloc[:, :-1].values  # Convert DataFrame to numpy array
y_data = data.iloc[:, -1].values   # Convert DataFrame to numpy array

# Convert y_data to integer type (assuming it contains binary labels 0 and 1)
y_data = y_data.astype(int)

lgbm = LGBMClassifier()
lgbm.fit(x_data, y_data)

lgbm.booster_.save_model('Algorithm/ml_models/custom_data_prediction.txt')
