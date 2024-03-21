class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person1 = Person('salman', 'irfan', 25)

print (person1)
print (person1.first_name)