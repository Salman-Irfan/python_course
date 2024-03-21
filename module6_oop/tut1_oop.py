class Person:
    def __init__(self, first_name, last_name, age):
        print (f"init method or constructor method called")
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person1 = Person('salman', 'irfan', 25)

print (person1)
print (person1.first_name)

# laptop class
class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

# laptop instances
# Create two instances of the Laptop class
laptop1 = Laptop("HP", "Pavilion", 1200)
laptop2 = Laptop("Dell", "Inspiron", 1500)

# Accessing attributes of the laptop instances
print("Laptop 1:")
print("Brand Name:", laptop1.brand_name)
print("Model Name:", laptop1.model_name)
print("Price:", laptop1.price)

print("\nLaptop 2:")
print("Brand Name:", laptop2.brand_name)
print("Model Name:", laptop2.model_name)
print("Price:", laptop2.price)
