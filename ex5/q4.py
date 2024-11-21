import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv('bodyPerformance.csv')
numeric_data = df.select_dtypes(exclude='object')

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title("Boxplot")

plt.subplot(2, 2, 2)
numeric_columns = df.select_dtypes(include=[np.number]).columns
for column in numeric_columns:
    sns.histplot(df[column], kde=False, bins=15, alpha=0.7, label=column)
plt.legend(loc='upper right')
plt.title("Histograms")

plt.subplot(2, 2, 3)
for column in numeric_columns:
    sns.kdeplot(df[column], label=column)
plt.legend(loc='upper right')
plt.title("Density Plots")

plt.subplot(2, 2, 4)
sns.scatterplot(x='age', y='weight_kg', data=df)
plt.title("Age vs Weight Scatterplot")

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=df)
plt.title('Gender Distribution')
plt.show()
