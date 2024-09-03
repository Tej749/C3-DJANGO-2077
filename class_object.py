class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def start_engine(self):
        print(f'{self.model} and  {self.color} is starting engine...')

    def drive(self):
        print(f'{self.model} and {self.color} is driving with speed {self.speed}')

bmw = Car('BMW', 'White', "420 km")
bmw.start_engine()
bmw.drive()