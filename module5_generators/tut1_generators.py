# generators
# generators & iterators

# iterator, iterable

any_list = [1, 2, 3]  # iterable

# for loop
print("for loop")
for i in any_list:
    print(i)

# iter function
print("iter function")
i = iter(any_list)
print(next(i))
print(next(i))
print(next(i))

# map
print("map")
for num in map(lambda a: a**2, any_list):  # iterator
    print (num)
