
import turtle as trtl

painter = trtl.Turtle()

painter.fillcolor("black")
painter.begin_fill()

painter.circle(100, 90)
painter.left(90)
painter.forward(200)
painter.left(90)
painter.circle(100, 90)
painter.end_fill()

painter.penup()
painter.circle(100,90)
painter.pendown()
painter.fillcolor("orange")
painter.begin_fill()
painter.right(170)
painter.forward(200)
painter.right(100)
painter.forward(270)
painter.right(100)
painter.forward(200)
painter.left(10)
painter.right (180)
painter.circle(100, 180)
painter.end_fill()

painter.pensize(20)
painter.penup()
painter.circle(100, -90)
painter.right(90)
painter. forward (100)
painter.pendown()
painter.forward(100)

painter.pensize(5)
painter.right(90)
painter.circle(30,-90)
painter.circle(30,90)
painter.circle(30,90)
painter.left(90)
painter.forward(60)

wn=trtl.Screen()
wn.mainloop()
