#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(10)

number_of_legs = 8
legs_length = 100
dis_between_legs = 360 / number_of_legs
spider_body.pensize(5)
legs_drawn = 0
while (legs_drawn < number_of_legs):
  spider_body.goto(0,20)
  spider_body.setheading(dis_between_legs*legs_drawn)
  spider_body.forward(legs_length)
  legs_drawn = legs_drawn + 1
spider_body.hideturtle()
wn = trtl.Screen()
wn.mainloop()