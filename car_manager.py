import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 0

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.y_pos = random.randint(-250, 250)
            car.goto(300, car.y_pos)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE - (self.level * MOVE_INCREMENT)
            car.goto((new_x, car.y_pos))

    def increase_speed(self):
        self.level += 1



