import turtle

window = turtle.Screen() # screen of the game
window.title("Ping Pong") # title of the game
window.bgcolor("black") # background colour
window.setup(width=800 , height=600) # size of the screen
window.tracer(0) # stop the window updating automatically

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.shapesize(stretch_wid=5 , stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350 , 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5 , stretch_len=1)
paddle_2.penup()
paddle_2.goto(350 , 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.2
ball.dy = 0.2

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write("player 1: 0  |  player 2: 0" , align="center" , font=("courier", 24 ,"normal"))

def paddle_1_up(): # move of first paddle up
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down(): # move of first paddle down
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up(): # move of second paddle up
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down(): # move of second paddle down
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#keybourd control
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "5")
window.onkeypress(paddle_2_down, "2")

while True:
    window.update() # update the screen everytime the loop run
    
    #move of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # when the ball hit border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # right border
        ball.goto(0 , 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {}  |  player 2: {}".format(score1 , score2) , align="center" , font=("courier", 24 ,"normal"))

    if ball.xcor() < -390: # left border
        ball.goto(0 , 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {}  |  player 2: {}".format(score1 , score2) , align="center" , font=("courier", 24 ,"normal"))
    
    # ball collision with the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
