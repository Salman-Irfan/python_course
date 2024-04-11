# how to change the shape of pandas file
import pandas as pd
import numpy as np

# Create sample data for the DataFrame
data = {
    "Day": np.arange(1, 7),
    "English": np.random.randint(60, 100, 6),
    "Maths": np.random.randint(50, 95, 6),
    "Physics": np.random.randint(55, 90, 6),
    "Chemistry": np.random.randint(65, 95, 6),
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Define a real-world problem that can be solved using melt
# Suppose we want to analyze the average scores across subjects over the 6 days
# We can use the melt function to transform the DataFrame for easier analysis

# Melt the DataFrame to transform it for analysis
melted_df = pd.melt(df, id_vars=["Day"], var_name="Subject", value_name="Score")

# Display the melted DataFrame
print("\nMelted DataFrame:")
print(melted_df)

# Now, we can easily calculate the average scores across subjects over the 6 days
average_scores = melted_df.groupby("Subject")["Score"].mean()
print("\nAverage Scores Across Subjects:")
print(average_scores)
