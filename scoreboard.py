from turtle import Turtle

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, "Center", ('Arial', 15, 'normal'))

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "Center", ('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "Center", ('Arial', 15, 'normal'))