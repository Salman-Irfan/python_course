set_data = {1, 2, 3, 4, 5, 6, 7, 4}  # unique, no repetions
set_data.add(9)
set_data.discard(2)
print(set_data)


list_with_duplicates = [1, 2, 3, 4, 5, 6, 2, 3, 1]

# unique_set_from_list
unique_set_from_list = set(list_with_duplicates)
print(unique_set_from_list)


# unique list
unique_list = list(set(list_with_duplicates))
print(unique_list)
