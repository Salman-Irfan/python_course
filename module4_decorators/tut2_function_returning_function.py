# Consider a scenario where you want to create functions dynamically based on some input configuration. For instance, you may want to generate functions that perform different mathematical operations (addition, subtraction, multiplication, etc.) based on user input. Here's how you can achieve this using a function that returns another function:


def create_math_function(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "subtract":
        return lambda x, y: x - y
    elif operation == "multiply":
        return lambda x, y: x * y
    else:
        return None


# Usage example
add_function = create_math_function("add")
subtract_function = create_math_function("subtract")
multiply_function = create_math_function("multiply")

print(add_function(5, 3))  # Output: 8
print(subtract_function(10, 4))  # Output: 6
print(multiply_function(2, 6))  # Output: 12
