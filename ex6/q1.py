import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("Telecom_customer churn.csv")

# Data Preprocessing
# Handling Missing Values
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Handling Outliers using IQR method
def detect_and_replace_outliers(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data[col] = np.where(data[col] < lower_bound, lower_bound, data[col])
    data[col] = np.where(data[col] > upper_bound, upper_bound, data[col])

for col in numeric_cols:
    detect_and_replace_outliers(df, col)

# Feature Scaling using Min-Max Scaler
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Exploratory Data Analysis (EDA)
# Basic Overview
print(df.head())
print(df.info())
print(df.describe())

# Visualize Churn Distribution
sns.countplot(x='churn', data=df)
plt.title("Churn Distribution")
plt.show()

# Correlation Matrix for Numerical Columns
corr_matrix = df[numeric_cols].corr()
plt.figure(figsize=(15, 10))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Analyzing relationships between numerical features and churn
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x='churn', y=col, data=df)
    plt.title(f"Churn vs {col}")
    plt.show()

# Analyzing relationships between categorical features and churn
for col in categorical_cols:
    churn_rate = pd.crosstab(df[col], df['churn'], normalize='index')
    churn_rate.plot(kind='bar', stacked=True)
    plt.title(f"Churn Rate by {col}")
    plt.ylabel('Proportion')
    plt.show()

# Linear Regression Model
# Feature Selection
features = ['mou_Mean', 'totmrc_Mean', 'totrev', 'rev_Mean', 'adjrev', 'adjmou', 'months', 'uniqsubs']
target = 'churn'
X = df[features]  # Independent variables
y = df[target]  # Dependent variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_continuous = model.predict(X_test)

# Convert continuous predictions to binary (0 or 1)
threshold = 0.5
y_pred = np.where(y_pred_continuous >= threshold, 1, 0)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred_continuous)
r2 = r2_score(y_test, y_pred_continuous)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Classification Metrics
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
precision = precision_score(y_test, y_pred)
print(f"Precision: {precision}")
recall = recall_score(y_test, y_pred)
print(f"Recall: {recall}")
f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1}")

# Coefficients of the model
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)
