#your choice   (i chose vary in turtle speed)
import turtle as trtl
import random as rand


wn=trtl.Screen()
wall=trtl.Turtle()
maze_runner= trtl.Turtle()
maze_runner.shape("triangle")
maze_runner.shapesize(0.5,0.5,0.5)
maze_runner.color("blue")
maze_runner.penup()

length= 20 #wall length
door= 20
barrier=40
wall.speed(10)
door_random = rand .randint(0,length-door) #door random maker


#original maze runner speed
amount=2
#functions
def drawing_door():
    wall.forward(door_random)
    wall.penup()
    wall.forward(door)
    wall.pendown()

def drawing_barrier():
    wall.forward(barrier_random)
    wall.left(90)
    wall.forward(barrier)
    wall.back(barrier)
    wall.right(90)

def left():
    maze_runner.setheading(180)

def right():
    maze_runner.setheading(0)

def up():
    maze_runner.setheading(90)

def down():
    maze_runner.setheading(270)
def go():
    maze_runner.forward(amount)

def increase_speed():
    global amount
    amount=amount+1

def decrease_speed():
    global amount
    if amount>0:
        amount=amount-1


#for statement
for i in range (20):
    wall.left(90)
    #first few walls they want invisible
    if i < 4:
        wall.penup()
        wall.forward(length)
        wall.pendown()
        #next few walls cant have barriers or it looks odd
    elif i < 8:
        
        drawing_door()
        wall.forward(length-door_random-door)
        
    else:
       #door
        drawing_door()
        
        #barrier
        barrier_random = rand.randint(0,length-door-door_random-barrier)
        drawing_barrier()
        #rest of wall
        wall.forward(length-door_random-barrier_random-door)

    length=length+20

wall.hideturtle()


wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(up,("w"))
wn.onkeypress(down,"s")
wn.onkeypress(go,"g")

wn.onkeypress(increase_speed,"o")
wn.onkeypress(decrease_speed,"p")
wn.listen()



wn = trtl.Screen()
wn.mainloop()