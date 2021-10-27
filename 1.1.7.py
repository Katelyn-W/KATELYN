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
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  my_turtles.append(t)

# creating the y and x variable 
startx = 0
starty = 0
direction = 90

# brings the turtle to the origin using the variables and starts the code by turing it.
for t in my_turtles:
  t.penup()
  t.setheading(direction)
  t.goto(startx, starty)
  t.pendown()
  t.right(45)     
  t.forward(50)
  start_x = t.xcor()
  start_y = t.ycor()

# adding integers to the code to move the turtle forward	
  direction = t.heading()
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()