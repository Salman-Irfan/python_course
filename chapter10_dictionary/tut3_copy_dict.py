# Original dictionary
original_dict = {"name": "John", "age": 30, "city": "New York"}

# Method 1: Using the copy() method
copied_dict_1 = original_dict.copy()

# Method 2: Using the dictionary constructor
copied_dict_2 = dict(original_dict)

# Verify the results with the is keyword
print(
    "Are copied_dict_1 and original_dict the same object?",
    copied_dict_1 is original_dict,
)  # False
print(
    "Are copied_dict_2 and original_dict the same object?",
    copied_dict_2 is original_dict,
)  # False
