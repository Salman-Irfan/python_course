import pandas as pd

# Sample data for the DataFrame
data = {
    "Day": [1, 2, 3, 4, 5, 6],
    "Student_Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"],
    "English": [90, 85, 92, 88, 91, 87],
    "Math": [85, 88, 90, 86, 89, 84],
    "Physics": [88, 86, 85, 90, 87, 89],
    "Chemistry": [82, 87, 89, 84, 86, 90],
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Define a real-world problem that can be solved using pivot
# Suppose we want to analyze the average scores for each subject by day

# Pivot the DataFrame to calculate average scores by day for each subject
pivot_avg_scores = df.pivot_table(
    index="Day", values=["English", "Math", "Physics", "Chemistry"], aggfunc="mean"
)
print("\nAverage Scores by Day:")
print(pivot_avg_scores)

# Pivot the DataFrame to calculate average scores by day for each subject
# also use pivot columns, note that student names are repeated
pivot_avg_scores_students = df.pivot_table(
    index="Day",
    columns="Student_Name",
    values=["English", "Math", "Physics", "Chemistry"],
    aggfunc="mean",
)
print("\nAverage Scores by Day with Students as Columns:")
print(pivot_avg_scores_students)
