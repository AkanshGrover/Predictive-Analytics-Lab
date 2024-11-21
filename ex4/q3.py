import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'C'],
    'SubCategory': ['X', 'Y', 'X', 'Y', 'Z', 'Y', 'Z', 'X'],
    'Value': [10, 15, 10, 30, 45, 35, 60, 20],
    'Quantity': [1, 2, 3, 4, 5, 6, 7, 8]
}

df = pd.DataFrame(data)

grouped = df.groupby('Category').agg({
    'Value': ['mean', 'median', 'count'],
    'Quantity': 'sum'
})

print("\nGrouped Data with Aggregation:\n", grouped)

pivot_table = pd.pivot_table(df, values='Value', index='Category', columns='SubCategory', aggfunc='sum', fill_value=0)

print("\nPivot Table:\n", pivot_table)

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Akansh', 'Aditya', 'Vikas', 'Priti']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Salary': [70000, 80000, 90000, 100000]
})

df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)

print("\nConcatenated DataFrame:\n", df_concat)

df_merge_inner = pd.merge(df1, df2, on='ID', how='inner')

print("\nInner Join Result:\n", df_merge_inner)

df_merge_left = pd.merge(df1, df2, on='ID', how='left')

print("\nLeft Join Result:\n", df_merge_left)

df_merge_right = pd.merge(df1, df2, on='ID', how='right')

print("\nRight Join Result:\n", df_merge_right)

df_merge_outer = pd.merge(df1, df2, on='ID', how='outer')

print("\nOuter Join Result:\n", df_merge_outer)

df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)

df_join = df1.join(df2, how='outer')

print("\nJoin Result (on indices):\n", df_join)
