from turtle import Turtle

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_from_file()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_sore()

    def read_from_file(self):
        with open("data.txt") as file:
            context = file.read()
        return int(context)

    def write_to_file(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update_sore(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.high_score}", False, "Center",
                   ('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_sore()
        self.write_to_file()

    def increase_score(self):
        self.score += 1
        self.update_sore()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "Center", ('Arial', 15, 'normal'))