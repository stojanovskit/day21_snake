
from turtle import Turtle

from food import Food


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align='center', font=("Arial", 16, "normal"))
        self.hideturtle()

    def increase_score(self):

        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Arial", 16, "normal"))