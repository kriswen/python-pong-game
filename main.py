from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# hide animation until game is ready
screen.tracer(0)
# event listener
screen.listen()

# initialization
paddle_r = Paddle(350, 0)
paddle_l = Paddle(-360, 0)
ball = Ball()
scoreboard = ScoreBoard()

# paddle control
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "q")
screen.onkey(paddle_l.down, "a")

# Main game
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Refresh the screen
    ball.move()

    # Detect ball collision with top/bottom wall
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()  # reverse the y_move

    # Detect collision with paddle_r or paddle_l
    if (ball.distance(paddle_r) < 60 and ball.xcor() > 330) or (ball.distance(paddle_l) < 60 and ball.xcor() < -330):
        ball.bounce_x()
        # increase the ball speed
        ball.move_speed /= 1.05

    # Detect if paddles missed the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_score("r")

    # Detect if left paddle miss:
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_score("l")

screen.exitonclick()

