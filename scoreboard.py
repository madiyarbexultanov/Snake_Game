from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.counter()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align="center", font=('Arial', 18, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Arial', 38, 'bold'))

    def counter(self):
        self.score += 1
        self.update_scoreboard()




