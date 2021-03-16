import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Turtle Crossing - Capstone Project')
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.drive_across()

    # Detect if player passed a level
    if player.ycor() > 260:
        car.next_level()
        player.refresh()
        scoreboard.update_scoreboard()

    # Detect if player collides with a car object
    if player.distance(car) < 15:
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()
