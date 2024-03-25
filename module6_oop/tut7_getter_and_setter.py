# we will discuss three problems in existing
# then we will solve them using getter and setter decorators


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
        # self.complete_specification = f"{self.brand} {self.model_name} and price {self._price}"

    # complete_specification
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price {self._price}"

    # price
    @property
    def price(self):
        return self._price

    # price setter
    @price.setter
    def price(self, value):
        self._price = max(value, 0)

    # method to make a call
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")

    # method to full name
    def full_name(self):
        return f"{self.brand} {self.model_name}"


# Phone instances
phone1 = Phone("Nokia", "1100", 1000)
print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
# change price after initialization & but at complete specification price would not be changed
phone1.price = -500
print(phone1.complete_specification)
