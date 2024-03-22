class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    # instance methods
    # make_a_call
    def make_a_call(self, phone_number):
        print(f"calling {phone_number}")

    # full_name
    def full_name(self):
        return f"{self.brand} {self.model_name}"


class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute with name mangling
        self.__age = age  # Private attribute with name mangling

    def get_name(self):  # Getter method
        return self.__name

    def set_age(self, age):  # Setter method
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def print_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


# Creating an instance of the Student class
student1 = Student("Alice", 20)

# Accessing private attributes using name mangling
print(student1._Student__name)  # Output: Alice
print(student1._Student__age)  # Output: 20

# Updating private attributes using name mangling
student1._Student__name = "Bob"
student1._Student__age = 25

# Printing updated information using the print_info method
student1.print_info()  # Output: Name: Bob, Age: 25

print("Name:", student1.get_name())  # Output: Name: Alice

student1.set_age(5)  # Output: Invalid age

# conventions:
# _name: convention of private name
# __name__ dunder / magic method
