import turtle as trtl
import random as rand
wn = trtl.Screen()
target = trtl.Turtle()


wn.bgcolor("lightblue")

target.penup()

#making shape of turtle target
aim =  ((-5,0),(-5,25),(-30,25),(-30,35),(-5,35),(-5,60),(5,60),(5,35),(30,35),(30,25),(5,25),(5,0))
trtl.register_shape('aim',aim)
target.shape('aim')
#duck list
duck_list = []
duck1 = trtl.Turtle()
duck1.color("blue")
duck1.hideturtle()
duck_list.append(duck1)

duck2 = trtl.Turtle()
duck2.color("red")
duck2.hideturtle()
duck_list.append(duck2)

duck3 = trtl.Turtle()
duck3.color("green")
duck3.hideturtle()
duck_list.append(duck3)

print(duck_list)

points= 0

selected_duck = rand.choice(duck_list)

counter_interval = 1000 #1000 = 1 second

#functions

#moves target
def move_up():
    target.sety(target.ycor()+5)
def move_right():
    target.setx(target.xcor()+5)
def move_left():
    target.setx(target.xcor()-5)
def move_down():
    target.sety(target.ycor()-5)

#duck takes form and position
def duck_shape():
    selected_duck.penup()
    selected_duck.shape('circle')
    selected_duck.goto(rand.randint(-300,300),rand.randint(-300,300))
    selected_duck.showturtle()

#get rid of duck if you shoot it and if you miss print "didnt work"
def delete_duck():
    global points
    if (abs(target.xcor() - selected_duck.xcor()) < 31) and (abs(target.ycor() - selected_duck.ycor()) < 31):
        selected_duck.hideturtle()
        points = points + 1
        print (points, "point(s)")
        duck_shape()
        victor()
    else:
        print ("didn't work")
        
def victor():
   toms_points=5
   if points>toms_points:
       print ("you passed toms points")
#working on clock
'''def timer():
    time=10
    clock = trtl.Turtle()
    clock.sety(120)'''


#clock
'''def timer():
    for time in range (10):
        clock.clear()
        if time > 0:
            clock.write(time,"Arial", 20, "normal")
            time -= 1
            clock.getscreen().ontimer(time, counter_interval)
            
        else:
            print("done")
            
'''

#function calls
'''wn.ontimer(timer,counter_interval)'''

wn.onkeypress(move_up,"w")
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left,"a")
wn.onkeypress(move_down,"s")
wn.onkeypress(delete_duck,"space")
wn.listen()

duck_shape()



wn.mainloop()
