import pandas as pd
import statistics
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv('bodyPerformance.csv')
df.head()

numeric_data = df.select_dtypes(exclude='object')

print("The statistics variance of body_fat% is:", statistics.variance(df['body fat_%']))
print("\nThe statistics variance of height is:", statistics.variance(df['height_cm']))
print("\nThe Standard deviation of body_fat% is:", statistics.stdev(df['body fat_%']))

print("Skewness of the numerical data:")
print(numeric_data.skew())

print("\nThe Inter Quartile Range of numeric data is: ")
for col in numeric_data.columns:
    Q1 = df[col].quantile(.25)
    Q3 = df[col].quantile(.75)
    IQR = Q3 - Q1
    print('IQR of %s : %d' % (col, IQR))

print("\nThe percentile of weight is: ", df['weight_kg'].quantile([0.1, 0.2, 0.4, 0.5]))

print("\nThe range of data is: ")
for col in numeric_data.columns:
    range = df[col].max() - df[col].min()
    print('range of %s : %d' % (col, range))

print("\nMean Absolute Deviation (MAD) of numeric data:", (numeric_data[col] - numeric_data[col].mean()).abs().mean())
