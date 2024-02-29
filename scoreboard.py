from turtle import Turtle
TOP_CENTER_X_Y = (0, 280)
FONT = ("Courier", 10, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(TOP_CENTER_X_Y)
        self.color("white")
        self.score = 0
        self.refresh()

    def refresh(self):
        self.write(align=ALIGNMENT, font=FONT, arg=f"Score: {self.score}")
