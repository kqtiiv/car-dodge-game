import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create a car
    car.create_car()
    car.move()

    # detect collision with car
    for _ in car.cars:
        if player.distance(_) < 20:
            game_is_on = False
            scoreboard.game_over()

    # if player reaches the other end
    if player.reached_end():
        time.sleep(1)
        player.next_level()
        scoreboard.increase_level()
        car.increase_speed()


screen.exitonclick()
