#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

spider.pensize(40)
spider.circle(20)

spider_legs = 8

leg_length = 70
leg_space = 380 / spider_legs


spider.pensize(5)
limit_legs = 0

while (limit_legs < spider_legs):
  spider.goto(0,0)
  spider.setheading(leg_space*limit_legs)
  spider.forward(leg_length)
  
  limit_legs = limit_legs + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()