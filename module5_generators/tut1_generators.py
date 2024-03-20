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
    print(num)

# list
# memory --- [................................] , list

# generator
# memory === () one number at a time will ge generated

# when to use list
# if your sequence has data, and you have to perform some operations on this data, then use list

# when to use generator
# when you have to use your sequence data only for one time, then use generator

# how to make a generator
# 1. generator function (yield key word)
# 2. generator comprehension

print("generators")


def nums(n):
    for i in range(1, n + 1):
        yield (i)


generated_nums = nums(10)
print(generated_nums)

# looping through numbers
print("generated_nums")
for i in generated_nums:
    print(i)

print("second time generated_nums")
for i in generated_nums:
    print(i)  # didn't print any thing


# generator comprehension example
# Suppose you have a list of numbers, and you want to generate a new list that contains only the squared values of the numbers greater than 5.
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generator comprehension to generate squared values of numbers greater than 5
squared_greater_than_5 = (num**2 for num in numbers if num > 5)

# Printing the squared values
for squared_num in squared_greater_than_5:
    print(squared_num)
