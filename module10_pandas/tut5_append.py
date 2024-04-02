import pandas as pd

# Dummy data for January sales
january_data = {
    "Date": ["2024-01-01", "2024-01-05", "2024-01-10"],
    "Product": ["A", "B", "C"],
    "Sales": [100, 150, 200],
}

# Dummy data for February sales
february_data = {
    "Date": ["2024-02-01", "2024-02-05", "2024-02-10"],
    "Product": ["A", "B", "C"],
    "Sales": [120, 180, 130],
}

# Create DataFrames for January and February sales
df_january = pd.DataFrame(january_data)
df_february = pd.DataFrame(february_data)

# Append February data to January data
combined_sales = pd.concat([df_january, df_february], ignore_index=True)

# Display the combined DataFrame
print("Combined Sales Data:")
print(combined_sales)
