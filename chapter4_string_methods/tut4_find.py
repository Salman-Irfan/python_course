# Dummy string
dummy_string = "It is a dummy string with at least 2 is in it."

# Find the position of the first 'is'
is_pos1 = dummy_string.find("is")

# Find the position of the second 'is' after the first one
is_pos2 = dummy_string.find("is", is_pos1 + 1)

print("Position of the second 'is':", is_pos2)
