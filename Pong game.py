import turtle
import time


# Create the window
wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) # stops the automatically updating

# Add paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # initial size is 1 and 1
paddle_a.penup()
paddle_a.goto(-350, 0)

# Add paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Add the ball
ball = turtle.Turtle()
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# Move the paddles
def paddle_a_up():
    """
    Move paddle a up by pressing a key.
    """

    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    """
    Move paddle a down by pressing a key.
    """

    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    """
    Move paddle b up by pressing a key.
    """

    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    """
    Move paddle b down by pressing a key.
    """

    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboards binding
wn.listen()
wn.onkey(paddle_a_up, 'w')
wn.onkey(paddle_a_down, 's') 
wn.onkey(paddle_b_up, 'Up') 
wn.onkey(paddle_b_down, 'Down') 

# Set the move step of the ball
ball.dx = 2
ball.dy = 2

# Main game loop
while True:
    wn.update()

    # Make the ball move automatically
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bound check
    # top border
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    # Button border
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # Left border
    if ball.xcor() <= -390: 
        ball.goto(0, 0)
        ball.dx *= -1
    
    # Right border
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    # Left paddle
    if ball.xcor() == -330 and ((paddle_a.ycor() - 50) <= ball.ycor() <= (paddle_a.ycor() + 50)):
        ball.setx(-330)
        ball.dx *= -1

    # Right paddle
    if ball.xcor() == 330 and ((paddle_b.ycor() - 50) <= ball.ycor() <= (paddle_b.ycor() + 50)):
        ball.setx(330)
        ball.dx *= -1

    time.sleep(0.01)
    