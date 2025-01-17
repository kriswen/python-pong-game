from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # triangle a=400, b=300, then c= 500

    # collision between paddle and ball
    def bounce_x(self):
        self.x_move *= -1
        # decrease the sleep time
        self.move_speed *= 0.9

    def bounce_y(self):
        # reverse the y direction by multiply -1
        self.y_move *= -1

    def reset(self):
        self.goto(0, 0)
        # ball change direction
        self.x_move *= -1
        self.move_speed = 0.1
