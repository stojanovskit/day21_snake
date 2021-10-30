from turtle import Turtle



class Snake:

    def __init__(self):
        self.food = Turtle("circle")
        self.all_snake = []

    def pos(self, numb):
        x = -20 * numb
        y = 0
        return x, y

    def make_snake(self):
        for num in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(self.pos(num))

            self.all_snake.append(snake)

    # def new_food(self):
    #     self.food.color("yellow")
    #     self.food.penup()
    #     self.food.goto(random.randint(-250, 250), random.randint(-250, 250))
    #     print(self.food.xcor())

    def move_snake(self):
        for seg_num in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[seg_num - 1].xcor()
            new_y = self.all_snake[seg_num - 1].ycor()
            self.all_snake[seg_num].goto(new_x, new_y)
        self.all_snake[0].forward(20)

        # if self.all_snake[0].xcor == self.food.xcor:
        #     self.food.clear()
        #     self.new_food()

    def up(self):
        self.all_snake[0].setheading(90)

    def down(self):
        self.all_snake[0].setheading(270)

    def left(self):
        self.all_snake[0].setheading(180)

    def right(self):
        self.all_snake[0].setheading(0)

    def poin(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(self.pos(len(self.all_snake)))

        self.all_snake.append(snake)