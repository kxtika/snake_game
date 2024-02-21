from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# TODO: create a snake body
squares = []

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(position)
    squares.append(new_square)

screen.update()

# TODO: move snake using keys(arrows or 'awsd')
game_is_on = True
while game_is_on:
    screen.update()
    for square in squares:
        square.forward(20)

# TODO: create food
# TODO: detect collision with food
# TODO: add a block to snake's body
# TODO: detect collision with the wall
# TODO: create a scoreboard
# TODO: detect collision with the tail
screen.exitonclick()
