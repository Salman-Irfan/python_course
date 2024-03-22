class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # static methods
    @staticmethod
    def hello():
        print (f"hello, static method called")

person1 = Person("salman", "irfan", 25)
Person.hello()
