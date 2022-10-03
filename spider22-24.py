#   a116_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()

#creates spider body
spider.pensize(40)
spider.circle(20)
#configure spider legs
spider_legs = 8
leg_length = 70
leg_space = 380 / spider_legs


spider.pensize(5)
limit_legs = 0

#draw legs
while (limit_legs < spider_legs):
  spider.goto(0,0)
  spider.setheading(leg_space*limit_legs)
  spider.forward(leg_length)
  #when limit gets to 8 it will stop the while loop
  limit_legs = limit_legs + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()