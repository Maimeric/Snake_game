import turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            new_turtle = turtle.Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            self.snake_body.append(new_turtle)
            new_turtle.goto(x=x, y=0)
            x -= 20

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
