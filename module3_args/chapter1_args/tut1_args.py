def all_total(*args):
    print(args)  # type tuple
    total_sum = sum(args)
    return total_sum


result = all_total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print("Total sum:", result)
