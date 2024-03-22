class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # method to get full name
    def get_full_name(self):
        print(f"{self.first_name} {self.last_name}")

salman = Person('salman', 'irfan', 25)
salman.get_full_name()

person2 = Person('person2', 'last name', 30)
Person.get_full_name(person2) # logic behind self argument