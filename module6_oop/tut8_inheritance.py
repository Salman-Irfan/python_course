class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model_name}, Price: {self.price}")


class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def display_info(self):  # Overriding display_info method
        super().display_info()
        print(
            f"RAM: {self.ram}GB, Internal Memory: {self.internal_memory}GB, Rear Camera: {self.rear_camera}MP"
        )


# Create instances of the Phone and SmartPhone classes
phone1 = Phone("Apple", "iPhone 12", 1000)
smartphone1 = SmartPhone("Samsung", "Galaxy S20", 800, 8, 128, 64)

# Display information about the phone and smartphone
phone1.display_info()
print("\n")
smartphone1.display_info()
