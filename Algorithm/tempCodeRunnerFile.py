x_train = x_data
y_train = y_data

# Create and train the LightGBM model
lgbm = LGBMClassifier()
lgbm.fit(x_train, y_train)

# Predict probabilities for the test set
y_prob = lgbm.predict_proba(x_train)[:, 1]  # Probability of class 1 (heart disease)
print(y_prob)