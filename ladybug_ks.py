#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
#line across for outline of wings
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)
dots=4
# draw two sets of dots
while (num_dots < dots ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos, ypos + 30)
  ladybug.pendown()
  ladybug.circle(2)
  


  xpos = xpos + 30
  ypos = ypos + 0
  num_dots = num_dots + 2



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()