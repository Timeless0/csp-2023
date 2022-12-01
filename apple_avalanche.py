#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple_list= []
apple = trtl.Turtle()
apple_list.append(apple)
apple = trtl.Turtle()
apple_list.append(apple)
apple = trtl.Turtle()
apple_list.append(apple)
apple = trtl.Turtle()
apple_list.append(apple)
apple = trtl.Turtle()
apple_list.append(apple)




letter_list=[]
letter=trtl.Turtle()
alphabet=("a","s","d","f","g","h","j","k","l")
selected_letter= alphabet[rand.randint(0, 8)]
letter_list.append(letter)
letter=trtl.Turtle()
letter_list.append(letter)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  apple_list[0].goto(-70,100)
  apple_list[1].goto(90,150)
  apple_list[2].goto(0,0)
  apple_list[3].goto(60,100)
  apple_list[4].goto(-30,50)
  wn.update()

def fall():
  apple.setx(0)
  apple.sety(0)
  apple.penup()
  apple.goto(0,-150)
  apple.pendown()
  apple.hideturtle()
  letter.clear()
  apple_list.pop(apple)
  letter_list.pop(letter)

def draw_random(selected_letter):
  if (apple in apple_list):
    
    letter.penup()
    letter.hideturtle()
    letter.setx(120)
    letter.sety(80)
    letter.color("red")
    letter.write(selected_letter, font=("Arial", 70, "bold"))
  
#-----function calls-----
draw_apple(apple_list[0])
draw_apple(apple_list[1])
draw_apple(apple_list[2])
draw_apple(apple_list[3])
draw_apple(apple_list[4])

for apple in apple_list:
  draw_random(selected_letter)
  wn.onkeypress(fall)
  wn.listen()




wn.mainloop()
