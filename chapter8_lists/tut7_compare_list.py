# Define three fruit lists
fruits1 = ["apple", "banana", "orange"]
fruits2 = ["apple", "banana", "orange"]
fruits3 = ["kiwi", "grape", "melon"]

# 1. Compare with ==
print("Comparing with ==:")
print("fruits1 == fruits2:", fruits1 == fruits2)  # True, compares value
print("fruits1 == fruits3:", fruits1 == fruits3)  # False, compares memory address

# 2. Compare with is keyword
print("\nComparing with is keyword:")
print("fruits1 is fruits2:", fruits1 is fruits2)  # False
print("fruits1 is fruits3:", fruits1 is fruits3)  # False
