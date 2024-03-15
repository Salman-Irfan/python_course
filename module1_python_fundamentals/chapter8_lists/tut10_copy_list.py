# Original list
original_list = [1, 2, 3, 4, 5]

# Method 1: Using the copy() method
copied_list_1 = original_list.copy()

# Method 2: Using list slicing
copied_list_2 = original_list[:]

# Method 3: Using the list constructor
copied_list_3 = list(original_list)

# Verify the results with the is keyword
print(
    "Are copied_list_1 and original_list the same object?",
    copied_list_1 is original_list,
)  # False
print(
    "Are copied_list_2 and original_list the same object?",
    copied_list_2 is original_list,
)  # False
print(
    "Are copied_list_3 and original_list the same object?",
    copied_list_3 is original_list,
)  # False
