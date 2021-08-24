from turtle import Screen
from paddel_file import Peddle
from ball import Ball
import time
from scorebord import Scorebord

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong Game Created by JAYDIP")
screen.tracer(0)


r_paddle = Peddle((350, 0))
l_paddle = Peddle((-350, 0))
ball = Ball()
scorebord = Scorebord()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    # detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detact collisoon with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()> 320 or ball.distance(l_paddle)< 50 and ball.xcor()<-320:
        ball.bounce_x()
    # detact when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scorebord.l_point()
    # detact when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scorebord.r_point()


screen.exitonclick()
