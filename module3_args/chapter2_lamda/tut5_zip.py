user_ids = [1, 2, 3]
user_names = ["salman", "umar", "ali"]

print(list(zip(user_ids, user_names)))
print(dict(zip(user_ids, user_names)))


list_tuple = [(1, 2), (3, 4), (5, 6), (7, 8)]

l1, l2 = list(zip(*list_tuple))

print(l1)
print(l2)
