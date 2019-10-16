import turtle 
import time
import random

delay=0.1

#Score
score= 0
high_score= 0

#set up the screen 
wn=turtle.Screen()#object for the window screen to be dispwlayed 
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600 , height=600)
wn.tracer(0)#turns off animation on the screen/turns off the screen updates

#Snake head
head = turtle.Turtle()#makes a new turtle object 
head.speed(0)
head.shape("square")
head.color("black")
#turtles draw lines so this will lift the pen and wont draw anyline
head.penup()
head.goto(0,0)#starting coordiantes of the turtle object 
head.direction = "stop"

#Snake Food buff
food = turtle.Turtle()#makes a new turtle object 
food.speed(0)
food.shape("circle")
food.color("red")
#turtles draw lines so this will lift the pen and wont draw anyline
food.penup()
food.goto(0,100)

segments = [] #increase in body gets added using segments

# Pen 
pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 High Score : 0",align="center",font=("Courier" , 24 ,"normal"))

#Functions
def go_up():
    if head.direction != "down":
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
        y= head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down" :
        y= head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left" :
        x= head.xcor()
        head.setx(x - 20)

    if head.direction == "right" :
        x= head.xcor()
        head.setx(x + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


#main game loop
while True:
    wn.update()

    #check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #hide the segments/delete them 
        for segment in segments:
            segment.goto(1000, 1000)
            #other way is their in the comments try that later

        #clear the segments list 
        segments.clear() 

        #reset the score
        score = 0

        #resting the delay 
        delay=0.1

        #updating the score on the screen 
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score),align="center",font=("Courier" , 24 ,"normal"))

    #The distance between center of turtle to the edge is 20 pixles
    #so now if the distance between the two turtle heads is less than 20 then they collide 
    if head.distance(food) < 18:
        #move the food to random cooridinates on the screen
        #now we use the randomize module 
        x=random.randint(-280, 280)
        y=random.randint(-280, 280)
        food.goto(x,y)

        # Add a segment 
        new_segment=turtle.Turtle()
        new_segment.speed(0)# Animation speed
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay 
        delay -= 0.003

        #increase the score
        score +=10

        if score > high_score:
            high_score = score

        #updating the score on the screen
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score),align="center",font=("Courier" , 24 ,"normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x= segments[index-1].xcor()
        y= segments[index-1].ycor()
        segments[index].goto(x,y)
    
    # Move the segment 0 to where the head is 
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #Check for head collisions with the body segements
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segments/delete them 
            for segment in segments:
                segment.goto(1000,1000)
            
            #clear the segments list 
            segments.clear() 

            #reset the score
            score = 0

            #reset the delay 
            delay=0.1

            #updating the score 
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score, high_score),align="center",font=("Courier" , 24 ,"normal"))

    time.sleep(delay)

wn.mainloop()#will keep the window open for us
