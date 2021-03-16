from player import MOVE_DISTANCE
from turtle import Turtle, pos, shape
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self) -> None:
        super().__init__()

        spawn_point = random.randrange(-260, 260)
        for _ in range(1, 100):
            self.shape('square')
            self.color(random.choice(COLORS))
            self.penup()
            self.goto(280, spawn_point)
            self.move_speed = STARTING_MOVE_DISTANCE
            self.drive_across()

    def drive_across(self):
        new_x = self.xcor() + MOVE_INCREMENT*-1
        self.goto(new_x, self.ycor())

    def next_level(self):
        self.move_speed += MOVE_INCREMENT

    
