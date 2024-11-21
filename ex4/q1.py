import pandas as pd

df_csv = pd.read_csv('random.csv')

print("CSV DataFrame shape:", df_csv.shape)
print("CSV DataFrame columns:", df_csv.columns)
print("CSV DataFrame dtypes:\n", df_csv.dtypes)
print("\nFirst 5 rows of CSV DataFrame:\n", df_csv.head())
print("\nLast 5 rows of CSV DataFrame:\n", df_csv.tail())
print("\nCSV DataFrame info:\n")
df_csv.info()
print("\nDescriptive statistics for CSV DataFrame:\n", df_csv.describe())
single_column = df_csv['SomeEmail']
print("\nSingle column data:\n", single_column)
multiple_columns = df_csv[['SomeLat', 'SomeLon']]
print("\nMultiple column data:\n", multiple_columns)
first_row = df_csv.iloc[0]
first_five_rows = df_csv.iloc[0:5]
print("\nFirst row data:\n", first_row)
print("\nFirst five rows data:\n", first_five_rows)
row_col_loc = df_csv.loc[0, 'Id']
rows_cols_loc = df_csv.loc[0:4, ['ParentId', 'UUID']]
print("\nFirst row and specific column data using loc:\n", row_col_loc)
print("\nRows 0 to 4 and multiple columns using loc:\n", rows_cols_loc)
row_col_iloc = df_csv.iloc[0, 1]
rows_cols_iloc = df_csv.iloc[0:5, 0:3]
print("\nFirst row and second column data using iloc:\n", row_col_iloc)
print("\nFirst five rows and first three columns using iloc:\n", rows_cols_iloc)