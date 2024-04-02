import pandas as pd

# Sample data for demonstration
data1 = {"ID": [1, 2, 3, 4], "Name": ["Alice", "Bob", "Charlie", "David"]}
data2 = {"ID": [1, 2, 4, 5], "Age": [25, 30, 35, 40]}

# Create DataFrames from the sample data
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames on the 'ID' column using an inner join
merged_df = pd.merge(df1, df2, on="ID", how="inner")

# Display the merged DataFrame, resembles with sql inner join
print("Merged DataFrame:")
print(merged_df)
