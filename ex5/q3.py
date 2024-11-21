import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv('bodyPerformance.csv')
df.head()

numeric_data = df.select_dtypes(exclude='object')
categorical_data = df.select_dtypes(include='object')

print("\nCorrelation between numeric features: \n")
correlation_matrix = numeric_data.corr()
print(correlation_matrix)
