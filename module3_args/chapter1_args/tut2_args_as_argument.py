def all_multiply(*args):
    print(args)  # type tuple
    total_product = 1
    for num in args:
        total_product *= num
    return total_product


mul_list = [2, 3, 4, 5]
result = all_multiply(*mul_list)
print("Total product:", result)
