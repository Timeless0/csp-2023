import turtle as trtl
import random as rand
wn = trtl.Screen()
target = trtl.Turtle()


target.penup()

#making shape of turtle target
aim =  ((-5,0),(-5,25),(-30,25),(-30,35),(-5,35),(-5,60),(5,60),(5,35),(30,35),(30,25),(5,25),(5,0))
trtl.register_shape('aim',aim)
target.shape('aim')

duck_list = []
duck = trtl.Turtle()
duck.color("blue")
duck.hideturtle()
duck_list.append(duck)
duck = trtl.Turtle()
duck.color("red")
duck.hideturtle()
duck_list.append(duck)
duck = trtl.Turtle()
duck.color("purple")
duck.hideturtle()
duck_list.append(duck)


selected_duck = rand.choice(duck_list)

#functions

#moves target
def move_up():
    target.sety(target.ycor()+10)
def move_right():
    target.setx(target.xcor()+10)
def move_left():
    target.setx(target.xcor()-10)
def move_down():
    target.sety(target.ycor()-10)

def duck_shape(selected_duck):
    duck.penup()
    duck.begin_fill()
    duck.circle(20)
    duck.end_fill()
    '''duck.goto(rand(-150,0),rand(0,150))'''
    duck.showturtle()

#function calls


wn.onkeypress(move_up,"w")
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left,"a")
wn.onkeypress(move_down,"s")
wn.listen()

duck_shape(selected_duck)



wn.mainloop()