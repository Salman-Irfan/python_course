def add(a, b):
    return a + b


print(add) # add function memory address

add2 = lambda a, b: a + b
result2 = add2(2, 3)
print(result2) # 5
print(add2) # lamda function memory address
