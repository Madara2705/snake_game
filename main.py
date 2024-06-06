from turtle import Screen
from snake_game import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_main = Snake()
snake_main.create_snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake_main.up, "Up")
screen.onkey(snake_main.down, "Down")
screen.onkey(snake_main.left, "Left")
screen.onkey(snake_main.right, "Right")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake_main.snake_move()

    if snake_main.all_snakes[0].distance(food) < 15 :
        food.refresh()
        scoreboard.increase_score()
        snake_main.extend()

    if snake_main.all_snakes[0].xcor() > 300 or snake_main.all_snakes[0].xcor() < -300 or snake_main.all_snakes[0].ycor() > 300 or snake_main.all_snakes[0].ycor() < -300 :
        game_is_on = False
        scoreboard.game_over()

    for snake_body in snake_main.all_snakes :
        if snake_body == snake_main.all_snakes[0] :
            pass
        elif snake_main.all_snakes[0].distance(snake_body) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()