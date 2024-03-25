from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):  # inherit turtle class
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1.0, stretch_wid=5.0)
        self.goto(x_pos, y_pos)

    def up(self):
        # self.forward(MOVE_DISTANCE)
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
