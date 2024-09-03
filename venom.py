class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} is starting an engine......")

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is drive with speed {self.speed}")

bmw = Car("BMW 300S", "430 KM/Hr")
bmw.drive()
bmw.start_engine()
