# Inheritance :
# Parent Class / base class (jasko method ra properties inherit hnx)
# Child Class / Derive class ( jasle aruko method ra properties la inherit garxa)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} is starting an engine...")

class Car(Vehicle):
    def __init__(self,brand, speed):
        super().__init__(brand)
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving with speed {self.speed}")

bmw = Car("BMW 200S", "220 KM/Hr")
bmw.drive()
bmw.start_engine()

thar = Car("TH-2024S", '200 KM/Hr')
thar.start_engine()
thar.drive()





