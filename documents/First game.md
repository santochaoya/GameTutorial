This document is using the turtle to create a pong game. 



# Main Game

## Preparing

```python
import turtle
```

This is a basic graphics module used to create this game.



## Create a window

```python
wn = turtle.Screen()
wn.title('Pong by Xiao')

# backgroud color
wn.bgcolor('black')
wn.setup(width=800, height=600)

# Stops the window from automatically updating. Can speed up the games.
wn.tracer(0)
```



## Create a main game loop

The main game loop contains the entire process of the game. Every game will have a main game loop.

```python
# main game loop
while True:
		wn.update()
```

* ```wn.update()``` is the starting process. Every time the loop runs, it update the screen.



### Add paddles and a ball

#### 1. Get turtle object

In Python, start with a small letter represent a module name, a capital letter represents a class name

```python
paddle_a = turtle.Turtle()
```



### 2. Setup the paddle

**Initialize settings**

* Set the animation speed. Typically, set it to the possible maximal speed.

```python
paddle_a.speed(0)
```



**Customize settings**

* shape

  ```python
  paddle_a.shape('square')
  ```

* color

  ```python
  paddle_a.color('white')
  ```

* resize the shape

  ```python
  paddle_a.shapesize(stretch_width=5, stretch=1) # 5 * 20 pixels
  ```

  The initial size is 1 * 1

  

**System settings**

* Disable the turtle to draw a line

  ```python
  paddle_a.penup()
  ```

* Set the starting coordinate

  ```python
  paddle_a.goto(-350, 0)
  ```



### 3. Set another pandle

It is all the same settings as paddle A except for the starting coordinate.

```python
paddle_b.goto(350, 0)
```



### 4. Set the ball

All the same settings as paddle A. Except for starting coordinate and the stretch shape

```python
ball.goto(0, 0)
ball.shapesize(stretch_width=1, stretch=1)
```



## Functions to paddles and balls

After creating all the components for the game, we make some functions for them

### 1. Move paddles

```python
def paddle_a_up():
  	"""
  	Add 20 pixels to the y coordinate when the function calls.
  	"""
    
    y = paddle_a.ycor() 
    y += 20 # add 20 pixel to y
    paddle_a.sety(y) # set new y to paddle a
    
def paddle_a_down():
  	"""
  	Minus 20 pixels to the y coordinate when the function calls.
  	"""
    
    y = paddle_a.ycor() 
    y -= 20 # add 20 pixel to y
    paddle_a.sety(y) # set new y to paddle a
    
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w') 
wn.onkeypress(paddle_a_down, 's') 
```

* ```ycor()```  build in function, get the **current y coordinate**.
* ```sety()``` set new value to y coordinate
* ```wn.listen()``` listen for the keyboard input
* ```wn.onkeypress(paddle_a_up, 'w')``` bind key 'w' to function ```paddle_a_up```



Replace ```y += 20``` to ```y-=20```  in the ```paddle_a_down()```

Replace bind key to **Up** and **Down** to the paddle B.



### 2. Move the ball and bounce up

Next, let's get the ball move and bounce up from paddle and border. The ball will move from both x and y coordinate

```python
# every time the ball move will move by 2 pixel.
ball.dx = 2
ball.dy = 2 # might different from different computers
```



After defining the moving of the ball, inside the **main game loop**

```python
while True:
		wn.update()
		
		# Move the ball
		# get the current ball x coordinate plus the moving pixel under each iteration
    ball.setx(ball.xcor() + ball.dx) 
		ball.sety(ball.ycor() + ball.dy) 
    
    # Border Checking
		# The first border the ball will reach and bounce back
    # top border
    if ball.ycor() > 290:
      	ball.sety(290) # this avoids certain types of problems.
        ball.dy *= -1 # reverses the direction
    
    # botton border
   	if bar.ycor() < -290:
      	ball.sety(-290)
        ball.dy *= -1
    
    # if out of the left or right border, the ball will go back to the center and restart the game
    # Left border
    if ball.xcor() <= -390: 
        ball.goto(0, 0)
        ball.dx *= -1
    
    # Right border
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
      
```

NOTE: KEEP USING 4 SPACES OR A TAB CONSISTENTLY, OR IT WILL RAISE AN ERROR.



### 3. Paddle and ball collisions

```python
# Paddle and ball collisions
# Left paddle
if ball.xcor() == -330 and ((paddle_a.ycor() - 50) <= ball.ycor() <= (paddle_a.ycor() + 50)):
ball.dx *= -1

# Right paddle
if ball.xcor() == 330 and ((paddle_b.ycor() - 50) <= ball.ycor() <= (paddle_b.ycor() + 50)):
ball.dx *= -1
```



# Score System

## 

