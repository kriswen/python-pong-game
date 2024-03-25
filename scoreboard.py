from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Write left & right scores
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Arial", 60, "normal"))
        self.draw_center_line()

    def increase_score(self, win):
        if win == "l":
            self.score_l += 1
        if win == "r":
            self.score_r += 1
        self.update_scoreboard()

    def draw_center_line(self):
        y = -300
        while y < 300:
            self.goto(0, y)
            self.write("|", align="center", font=("Arial", 60, "normal"))
            y += 80
