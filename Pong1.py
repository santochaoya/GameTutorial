import turtle


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

# moving paddles
def paddle_a_up():
    """
    Add 20 pixels when press the key.
    """

    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# bind keyboards
wn.listen()
wn.onkey(paddle_a_up, 'w') 


# Main game loop
while True:
    wn.update()
