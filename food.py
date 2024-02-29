# TODO: create food
from turtle import Turtle
import random

SCREEN_BORDER_P = 280
SCREEN_BORDER_N = -280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(SCREEN_BORDER_N, SCREEN_BORDER_P)
        random_y = random.randint(SCREEN_BORDER_N, SCREEN_BORDER_P)
        self.goto(x=random_x, y=random_y)

