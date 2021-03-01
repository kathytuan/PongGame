from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# take away animated step
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.pause_pace)
    screen.update()
    ball.move()

    # TODO: detect collision with the top/bottom wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # TODO: detect collision with the paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 340 or ball.distance(l_paddle) <= 50 and ball.xcor() < -340:
        ball.bounce_x()

    # TODO: detect collision with the side wall
    # right wall
    if ball.xcor() >= 380:
        ball.reset_direction()
        score.l_point()

    # left wall
    if ball.xcor() <= -380:
        ball.reset_direction()
        score.r_point()

screen.exitonclick()
