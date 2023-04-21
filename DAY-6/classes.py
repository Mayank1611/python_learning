class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        if self.speed > 0:
            self.speed -= 10

    def get_speed(self):
        return self.speed


my_car = Car("Honda", "Civic", 2022)
my_car.accelerate()
print(my_car.get_speed())
