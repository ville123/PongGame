# Pong Game in Python 3 / Windows 
# Origin: freeCodeCamp.org's Youtube-channel

# TODO: Ask if the player wants a new game
# TODO: Make ball hit the paddle a bit earlier and not overlap with the paddle

# MOVE THE LEFT PADDLE WITH 'w' and 's' AND RIGHT PADDLE WITH 'p' and 'l' !!

import time
import turtle
import winsound

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # stops the window not updating

# Run the game
new_game = True

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) # position of the paddle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.10 # Experiment which value works best on your computer
ball.dy = 0.10

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    if paddle_a.ycor() < 240:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if paddle_a.ycor() > -230:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if paddle_b.ycor() < 240:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if paddle_b.ycor() > -230:
        y -= 20
        paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")     # Pressing w on keyboard moves paddle_a up
window.onkeypress(paddle_a_down, "s")   # Pressing s on keyboard moves paddle_a down
window.onkeypress(paddle_b_up, "p")     # Pressing p on keyboard moves paddle_b up
window.onkeypress(paddle_b_down, "l")   # Pressing l on keyboard moves paddle_b down


# Main game loop
while new_game:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # ball direction is reversed
        winsound.PlaySound("boing.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

    # Ball has gone past the paddle
    if ball.xcor() > 390: 
        ball.goto(0, 0)
        ball.dx *= -1
        if score_a < 3:
            score_a += 1
            winsound.PlaySound("ping.wav", winsound.SND_ASYNC)
        else:
            new_game = False
            pen.clear()
            pen.write("WINNER: PLAYER A !!!!", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        if score_b < 3:
            score_b += 1
            winsound.PlaySound("ping.wav", winsound.SND_ASYNC)
        else:
            new_game = False
            pen.clear()
            pen.write("WINNER: PLAYER B !!!!", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle hits the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
