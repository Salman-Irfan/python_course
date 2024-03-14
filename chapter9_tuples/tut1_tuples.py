# Create a tuple of days
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Print the tuple
print("Tuple of days:", days)

# Tuple methods
print("\nPopular tuple methods:")

# 1. count(): Returns the number of occurrences of a specified value in the tuple
print("Number of occurrences of 'Monday':", days.count("Monday"))

# 2. index(): Returns the index of the first occurrence of a specified value in the tuple
print("Index of 'Wednesday':", days.index("Wednesday"))

# 3. len(): Returns the length of the tuple
print("Length of the tuple:", len(days))

# 4. slicing: Accessing subsets of the tuple
print("First three days:", days[:3])
print("Last three days:", days[-3:])

# 5. accessing value by index
print(days[0])
