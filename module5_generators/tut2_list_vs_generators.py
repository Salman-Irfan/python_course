# do same example with list and generator and compare their efficiency in terms of memory and time
import time

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to generate squared values of numbers greater than 5
start_time = time.time()
squared_greater_than_5_list = [num**2 for num in range(1,1000000000) if num > 5]
end_time = time.time()

# Printing the squared values
for squared_num in squared_greater_than_5_list:
    print(squared_num)

print("Time taken with list comprehension:", end_time - start_time)
