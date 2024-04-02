import pandas as pd

# Sample data for demonstration
data1 = {"ID": [1, 2, 3, 4], "Name": ["Alice", "Bob", "Charlie", "David"]}
data2 = {"ID": [5, 6, 7, 8], "Name": ["Eve", "Frank", "Grace", "Henry"]}

# Create DataFrames from the sample data
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenate the DataFrames vertically (along rows) using pd.concat()
combined_df = pd.concat([df1, df2], ignore_index=True)

# Display the combined DataFrame
print("Combined DataFrame:")
print(combined_df)
