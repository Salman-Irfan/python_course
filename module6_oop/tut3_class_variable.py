class Circle:
    # class variables
    pi = 3.14

    # init method
    def __init__(self, radius):
        self.radius = radius

    # area method
    def area(self):
        print(self.pi * self.radius**2)
        return self.pi * self.radius**2

    # circumference method
    def circumference(self):
        print(2 * self.pi * self.radius)
        return 2 * self.pi * self.radius


c1 = Circle(4)
c1.area()
c1.circumference()
