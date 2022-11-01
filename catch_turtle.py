# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----

spot = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()

color="green"
shape="turtle"
size=2
score=0


font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----

spot.shapesize(size)
spot.shape(shape)
spot.fillcolor(color)
font_setup=("Arial", 20, "normal")

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(400,300)
score_writer.pendown

counter.penup()
counter.hideturtle()
counter.goto(-400,300)
counter.pendown
#-----game functions--------
def spot_clicked(x,y):
  if timer_up == False:
    global score
    change_position()
    update_score()
  else:
    spot.hideturtle()

    

def change_position():
    spot.penup()
    spot.hideturtle()
    new_xpos=rand.randint(-400,400)
    new_ypos=rand.randint(-300,300)
    spot.goto(new_xpos,new_ypos)
    spot.pendown()
    spot.showturtle()
    
def update_score():
    global score
    score += 1
    score_writer.clear() 
    score_writer.write(score, font=font_setup)
    
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("orange")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()