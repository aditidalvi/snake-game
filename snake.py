# THE SNAKE GAME

import turtle
import time # it used to set the time at which the obj will run
import random #used to move to the random locations

delay = 0.2     # delay the time of the obj by 0.3 s
# set up the screen
wn = turtle.Screen()
wn.title("SNAKE GAME BY AD")
wn.bgcolor("Green")
wn.setup(width=600,height=600)
wn.tracer(0) # Turns off the animation

# the snake head
head = turtle.Turtle()
head.shape("square")
head.color("Black")
head.speed(0)
head.penup()      # does not draw lines as turtle module draws lines
head.goto(0,0)
head.direction = "stop"

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.penup()      # does not draw lines as turtle module draws lines
ball.goto(0,100)
# pen to write the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  Highest Score:0 " , align="center" , font=("Courier",20,"normal"))

# Score
score =0
high_score=0


segments = []
def go_up():
    if head.direction!="down":
       head.direction = "up"
def go_down():
    if head.direction != "up":
       head.direction = "down"
def go_left():
    if head.direction != "right":
       head.direction = "left"
def go_right():
    if head.direction != "left":
       head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
# Keyboard bindings
wn.listen()  # the window listens to the presses and sounds
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

# Main loop
while True:
    wn.update() # updates the screen
    # if the head collides with the border it should disappear
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
    # hide the segments
        for seg in segments:
               seg.goto(1000,1000)
        # clear the segments
        segments.clear()
        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highest Score:{}".format(score, high_score), align="center",font=("Courier", 20, "normal"))


    # when the food/ball touches the snake
    if head.distance(ball)<20:
        # move the ball or food to the random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        ball.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        # shorten the score
        delay-=0.001
        # increase the score
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{}  Highest Score:{}".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    # move the segments in the reverse order
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
     # if there is only one segment i.e.index at zero index location
    if len(segments)>0:
        x= head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # if the head touches the last part of the snake
    for segs in segments:
         if   segs.distance(head)<20:
             time.sleep(1)
             head.goto(0,0)
             head.direction = "stop"
             for seg in segments:
                 seg.goto(1000,1000)
             segments.clear()
             # Reset the score
             score = 0
             # Reset the delay
             delay = 0.1
             pen.clear()
             pen.write("Score:{}  Highest Score:{}".format(score, high_score), align="center",
                       font=("Courier", 20, "normal"))
    time.sleep(delay)


wn.mainloop()