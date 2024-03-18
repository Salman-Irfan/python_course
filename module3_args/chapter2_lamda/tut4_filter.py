def is_even(a):
    return a % 2 == 0


numbers = [3,4,5,2,1,4,7,8,]

evens = tuple(filter(is_even, numbers))

print(evens)
