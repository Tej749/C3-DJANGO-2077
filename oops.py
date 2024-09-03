class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def start_engine(self):
        print(f'{self.model} & {self.color} is starting an engine...!')

    def drive(self):
        print(f'{self.model} & {self.color} is driving with speed {self.speed}')

bmw = Car("BMW24", "Black", "320 Km/Hr")
bmw.start_engine()
bmw.drive()