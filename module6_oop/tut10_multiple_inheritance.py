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


class Camera:
    def __init__(self, front_camera):
        self.front_camera = front_camera

    def display_camera_info(self):
        print(f"Front Camera: {self.front_camera}MP")


class FlagshipSmartPhone(SmartPhone, Camera):
    def __init__(
        self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera
    ):
        SmartPhone.__init__(
            self, brand, model_name, price, ram, internal_memory, rear_camera
        )
        Camera.__init__(self, front_camera)

    def display_info(self):  # Overriding display_info method
        super().display_info()
        super().display_camera_info()


# Create instances of the Phone, SmartPhone, and FlagshipSmartPhone classes
phone1 = Phone("Apple", "iPhone 12", 1000)
smartphone1 = SmartPhone("Samsung", "Galaxy S20", 800, 8, 128, 64)
flagship_smartphone1 = FlagshipSmartPhone(
    "OnePlus", "OnePlus 9 Pro", 900, 12, 256, 108, 32
)

# Display information about the phone, smartphone, and flagship smartphone
phone1.display_info()
print("\n")
smartphone1.display_info()
print("\n")
flagship_smartphone1.display_info()
