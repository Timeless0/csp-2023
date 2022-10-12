#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  starting variables
startx = 0
starty = 0
direction = 45
# for loop creating the movement for each turtle rotated through
for t in my_turtles:
  t.setheading(direction)
  t.penup()
  t.goto(startx, starty)
  new_color=turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  t.pendown()
  t.right(45)     
  t.forward(50)
  

#	 new starting positions for turtles
  direction=t.heading()
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
