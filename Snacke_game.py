import turtle
import random
import time
delay=0.1
sc=0
hs=0
bodies=[]
#creating a Screen
s1=turtle.Screen()
s1.title("Snacke Game")
s1.bgcolor("light blue")
s1.setup(width=600,height=600)


#creating a  head
h1=turtle.Turtle()
h1.shape("circle")
h1.speed(0)
h1.color("red")
h1.fillcolor("green")
h1.penup()
h1.goto(0,0)
h1.direction="stop"

#creating a food
f1=turtle.Turtle()
f1.speed(0)
f1.shape("square")
f1.color("yellow")
f1.penup()
f1.ht()
f1.goto(290,290)
f1.st()

#score board
sb=turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-280,280)
sb.write("Score:0 | Highest Score:0")

#moving head Direction

def moveup():
    if h1.direction!="down":
        h1.direction="up"

def movedown():
    if h1.direction!="up":
        h1.direction="down"
def moveleft():
    if h1.direction!="right":
        h1.direction="left"
def moveright():
    if h1.direction!="left":
        h1.direction="right"

def movestop():
    h1.direction="stop"

# move the head
def move():
    if h1.direction=="up":
        y=h1.ycor()
        h1.sety(y+20)
    if h1.direction=="down":
        y=h1.ycor()
        h1.sety(y-20)
    if h1.direction=="right":
        x=h1.xcor()
        h1.setx(x+20)
    if h1.direction=="left":
        x=h1.xcor()
        h1.setx(x-20)

#event Handling
s1.listen()
s1.onkey(moveup,"Up")
s1.onkey(movedown,"Down")
s1.onkey(moveleft,"Left")
s1.onkey(moveright,"Right")
s1.onkey(movestop,"space")

while True:
    s1.update()
    #check collision with border
    if h1.xcor()>290:
        h1.setx(-290)
    if h1.xcor()<-290: 
        h1.setx(290)
    if h1.ycor()>290:
        h1.sety(-290)
    if h1.ycor()<-290:
        h1.sety(290)
    #check collinsion with food
    if h1.distance(f1)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        f1.goto(x,y)
    #increace the lenght of snake
        b1=turtle.Turtle()
        b1.speed(0)
        b1.shape("square")
        b1.penup()
        b1.color("blue")
        bodies.append(b1)

    #increase score
        sc=sc+100
        if sc>hs:
         hs=sc
        sb.clear()
        sb.write(f"Score :{sc}| HeghestScore:{hs}")
        delay=delay-0.001
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
            x=h1.xcor()
            y=h1.ycor()
            bodies[0].goto(x,y)
    move()
    #check collision with body
    for b in bodies:
        if b.distance(h1)<20:
            time.sleep(1)
            h1.goto(0,0)
            h1.direction="stop"
            for b in bodies:
                b.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("score :() | Highest :()",format(sc,hs))
    time.sleep(delay)
s1.mainloop()



