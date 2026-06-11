# 📘 Assignment: Machine Learning Fundamentals with scikit-learn

## 🎯 Objective

Build your first machine learning models using Python and scikit-learn. You'll learn to load datasets, prepare data, train classification and regression models, and evaluate their performance. This assignment bridges data analysis and practical AI.

## 📝 Tasks

### 🛠️ Load and Prepare Data for Machine Learning

#### Description
Start with a real-world dataset and prepare it for training. You'll explore the data, handle missing values, split into training and testing sets, and perform feature scaling.

#### Requirements
Completed program should:

- Load a CSV dataset using pandas
- Examine the dataset shape, data types, and summary statistics
- Handle any missing values (drop or fill them)
- Separate features (X) from target variable (y)
- Split data into training (80%) and testing (20%) sets using `train_test_split`
- Scale features using `StandardScaler` for consistency

### 🛠️ Train and Evaluate a Classification Model

#### Description
Build your first supervised learning model using a classification algorithm. Train the model on the prepared data and evaluate its accuracy on the test set.

#### Requirements
Completed program should:

- Train a classification model (Logistic Regression or Decision Tree)
- Make predictions on the test set
- Calculate accuracy score
- Generate a confusion matrix to understand prediction errors
- Print a classification report showing precision, recall, and F1-score

### 🛠️ Experiment with Multiple Models and Compare Performance

#### Description
Try different algorithms and compare their results. This teaches you how to select the best model for your problem through systematic evaluation.

#### Requirements
Completed program should:

- Train at least 3 different models (e.g., Logistic Regression, Random Forest, SVM)
- Evaluate each model using cross-validation
- Compare accuracy scores across all models
- Display results in a clear format (table or chart)
- Identify which model performs best and explain why

### 🛠️ Fine-tune and Optimize Your Model (Stretch Goal)

#### Description
Improve your best model by adjusting hyperparameters and exploring feature engineering. This teaches you how to iteratively improve machine learning solutions.

#### Requirements
Completed program should:

- Use hyperparameter tuning (Grid Search or Random Search) on the best model
- Try at least 2 different feature engineering techniques
- Compare performance before and after optimization
- Save the best model to disk using joblib
- Create a visualization comparing model predictions vs actual values
