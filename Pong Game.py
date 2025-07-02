import turtle  # import turtle module

# Initialize screen
wind = turtle.Screen()
wind.title("Ping Pong BY Mahmoud")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score
score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player2: 0", align="center", font=("courier", 24, "normal"))

# Functions
def paddle1_up():
    y = paddle1.ycor()
    if y < 250:
        y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    if y > -250:
        y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    if y < 250:
        y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    if y > -250:
        y -= 20
    paddle2.sety(y)

# Keyboard bindings
wind.listen()
wind.onkeypress(paddle1_up, "w")
wind.onkeypress(paddle1_down, "s")
wind.onkeypress(paddle2_up, "Up")
wind.onkeypress(paddle2_down, "Down")

# Main game loop
while True:
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom border collision
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right border - player 1 scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1} Player2: {score2}", align="center", font=("courier", 24, "normal"))

    # Left border - player 2 scores
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1} Player2: {score2}", align="center", font=("courier", 24, "normal"))

    # Paddle collision - paddle 2
    if (340 < ball.xcor() < 350) and (paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # Paddle collision - paddle 1
    if (-350 < ball.xcor() < -340) and (paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
