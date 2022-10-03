#   a116_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
#creates spider body
spider.pensize(40)
spider.circle(20)
#configure spider legs
spider.pencolor("black")
spider_legs = 8
leg_length = 70
leg_space = 270 / spider_legs


spider.pensize(5)
limit_legs = 0

#draw legs
while (limit_legs < spider_legs):
  spider.goto(0,20)
  spider.setheading(leg_space*limit_legs-45)
  spider.setheading(leg_space*limit_legs+45)
  spider.forward(leg_length)
  #when limit gets to 8 it will stop the while loop
  limit_legs = limit_legs + 1

#creates spider eyes
spider.pensize(2)
spider.pencolor("red")
eyes=2
eye_limit=0
position=0
while eye_limit<eyes:
  spider.penup()
  spider.goto(0,position)
  spider.pendown()
  spider.circle(5)
  position=position+40
  eye_limit=eye_limit+1



spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()