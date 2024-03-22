class Person:
    # class variables
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # increment counter
        Person.count_instance += 1


person1 = Person("salman", "irfan", 25)
print (Person.count_instance)