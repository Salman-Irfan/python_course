# Original tuple
original_tuple = (1, 2, 3, 4, 5)

# Method 1: Using the tuple() constructor
copied_tuple_1 = tuple(original_tuple)

# Method 2: Using tuple unpacking
copied_tuple_2 = (*original_tuple,)

# Verify the results with the is keyword
print(
    "Is copied_tuple_1 the same object as original_tuple?",
    copied_tuple_1 is original_tuple,
)  # True
print(
    "Is copied_tuple_2 the same object as original_tuple?",
    copied_tuple_2 is original_tuple,
)  # False
