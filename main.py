from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "s")
screen.onkeypress(left_paddle.down, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    # detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()


    # detect collision with left paddle
    if  ball.distance(left_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect if ball misses right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect if ball misses left paddle
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
