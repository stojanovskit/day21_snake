from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

snake = Snake()
food = Food()
score = Score()
snake.make_snake()

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.2)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.all_snake[0].distance(food) < 15:
        food.refresh()
        snake.poin()
        score.increase_score()
    if snake.all_snake[0].xcor() > 280:
        snake.all_snake[0].goto(-280, snake.all_snake[0].ycor())
    elif snake.all_snake[0].xcor() < -280:
        snake.all_snake[0].goto(280, snake.all_snake[0].ycor())
    elif snake.all_snake[0].ycor() < -280:
        snake.all_snake[0].goto(snake.all_snake[0].xcor(), 280)
    elif snake.all_snake[0].ycor() > 280:
        snake.all_snake[0].goto(snake.all_snake[0].xcor(), -280)

screen.exitonclick()
