import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('random.csv')

print("Missing values in DataFrame:\n", df.isnull().sum())
numerical_columns = df.select_dtypes(include=['number']).columns
numerical_columns = numerical_columns.drop(['Id', 'ParentId'])
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())
df['SomeString'] = df['SomeString'].fillna('Unknown')
df['SomeCountry'] = df['SomeCountry'].fillna('UnknownCountry')
df_cleaned = df.dropna(subset=['SomeEmail', 'SomeLat', 'SomeLon'])
df_interpolated = df.interpolate()
scaler_min_max = MinMaxScaler()
df[numerical_columns] = scaler_min_max.fit_transform(df[numerical_columns])
print("\nDataFrame after Min-Max scaling:\n", df.head())
scaler_z_score = StandardScaler()
df[numerical_columns] = scaler_z_score.fit_transform(df[numerical_columns])
print("\nDataFrame after Z-Score scaling:\n", df.head())
df_with_dummies = pd.get_dummies(df, columns=['SomeCountry', 'MixedStringNumber'])
print("\nDataFrame with dummy variables:\n", df_with_dummies.head())
df_with_dummies.to_csv('cleaned_data.csv', index=False)