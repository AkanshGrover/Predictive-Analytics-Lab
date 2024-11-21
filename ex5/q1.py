import pandas as pd
import statistics
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv('bodyPerformance.csv')
df.head()

numeric_data = df.select_dtypes(exclude='object')
categorical_data = df.select_dtypes(include='object')

print("Mean of all numeric data: \n")
print(numeric_data.mean())

print("\nMean of only one column(here it is body_fat): ", df['body fat_%'].mean())

print("Gmean of all numeric data: \n")
print(scipy.stats.gmean(numeric_data))

print("\nMean of only one column(here it is body_fat): ", scipy.stats.gmean(df['body fat_%']))

# print("Hmean of all numeric data: \n")
# print(statistics.harmonic_mean(numeric_data))

print("\nMean of only one column(here it is body_fat): ", statistics.harmonic_mean(df['body fat_%']))

print("\nMode of all numeric data:")
print(df.mode())

print("\nMedian of all numeric data: ", statistics.median(df['body fat_%']))
