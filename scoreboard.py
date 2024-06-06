from turtle import Turtle

class ScoreBoard(Turtle) :

    def __init__(self) :
        super().__init__()
        self.score = 0
        self.goto(0,260)
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self) :
        self.write(f"Score : {self.score}", align="center" ,font=("Arial", 24, "bold"))

    def game_over(self) :
        self.goto(0,0)
        self.write(f"GAME OVER", align="center" ,font=("Arial", 24, "bold"))

    def increase_score (self) :
        self.score += 1
        self.clear()
        self.update_scoreboard()