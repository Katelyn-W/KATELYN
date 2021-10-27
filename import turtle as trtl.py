import turtle as trtl
t = trtl.Turtle()
t.speed(0)
colo = input("What is your favorite color?")
def filled_circle():
  t.color(colo)
  t.begin_fill()
  t.circle(25)
  t.end_fill()

t.penup()
t.setposition(-500,0)
t.pendown()
for i in range(30):
  filled_circle()
  t.forward(50)
 

wn = trtl.Screen()
wn.mainloop()