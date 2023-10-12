from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snakes = Snake()
foods = Food()
scores = ScoreBoard()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

# TODO 2 : membuat snake bisa tetap berjalan maju
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snakes.move()
    # Detect collision with food
    if snakes.head.distance(foods) < 8:
        foods.refresh_food()
        snakes.extend()
        scores.increase_score()

    # Detect collision with wall
    if snakes.head.xcor() > 295 or snakes.head.xcor() < -295 or snakes.head.ycor() > 295 or snakes.head.ycor() < -295:
        # game_on = False
        # scores.game_over()
        scores.reset()
        snakes.reset_snake()

    # Detect collision with tail using slice methode
    for segments in snakes.seg_snake[1:]:
        if snakes.head.distance(segments) < 8:
            # game_on = False
            # scores.game_over()
            scores.reset()
            snakes.reset_snake()

screen.exitonclick()
