# OOP : Object-Oriented Programming
# class & object :

class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def start_engine(self):
        print(f'Model {self.model} & color {self.color} is starting an engine.')

    def drive(self):
        print(f'Model {self.model} & color {self.color} , car is driving with speed {self.speed}')

bmw = Car('BWM 200S', 'Grey', speed="320 KM/Hr")
bmw.start_engine()
bmw.drive()

hudai = Car("HUNDAI 24S", "White", speed="220 KM/Hr")
hudai.start_engine()
hudai.drive()



