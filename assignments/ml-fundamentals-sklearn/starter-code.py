"""
Machine Learning Fundamentals with scikit-learn
Students will build their first ML models using this starter template.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Task 1 - Load your dataset
# df = pd.read_csv('your_dataset.csv')
# print(df.head())
# print(df.info())
# print(df.describe())

# TODO: Task 1 - Handle missing values
# df = df.dropna()  # or df.fillna(method='ffill')

# TODO: Task 1 - Separate features and target
# X = df.drop('target_column', axis=1)
# y = df['target_column']

# TODO: Task 1 - Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TODO: Task 1 - Scale features
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# TODO: Task 2 - Train a classification model
# model = LogisticRegression(random_state=42)
# model.fit(X_train_scaled, y_train)

# TODO: Task 2 - Make predictions and evaluate
# y_pred = model.predict(X_test_scaled)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy}")
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))

# TODO: Task 3 - Train multiple models and compare
# models = {
#     'Logistic Regression': LogisticRegression(random_state=42),
#     'Random Forest': RandomForestClassifier(random_state=42),
#     'SVM': SVC(random_state=42)
# }
#
# for name, model in models.items():
#     scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
#     print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")

# TODO: Task 4 - Hyperparameter tuning (Stretch)
# param_grid = {
#     'n_estimators': [50, 100, 200],
#     'max_depth': [5, 10, 15],
#     'min_samples_split': [2, 5, 10]
# }
# grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
# grid_search.fit(X_train_scaled, y_train)
# print(f"Best parameters: {grid_search.best_params_}")
# print(f"Best score: {grid_search.best_score_}")

# TODO: Task 4 - Save your model
# import joblib
# joblib.dump(model, 'my_model.pkl')

if __name__ == "__main__":
    print("Machine Learning Fundamentals with scikit-learn")
    print("Complete the TODOs to build your first ML models!")
