from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_BORDER_P = 285
SCREEN_BORDER_N = -285
COLLISION_DISTANCE = 15

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < COLLISION_DISTANCE:
        food.refresh()
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.refresh()

        # add a block to snake's body
        snake.extend()

    # detect collision with the wall
    if snake.head.xcor() > SCREEN_BORDER_P or snake.head.xcor() < SCREEN_BORDER_N or snake.head.ycor() > SCREEN_BORDER_P or snake.head.ycor() < SCREEN_BORDER_N:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
