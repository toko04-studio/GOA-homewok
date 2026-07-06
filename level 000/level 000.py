from turtle import *

#house

#step 1 draw a square
shape("turtle")
speed(15)
width(5)
color("grey")
begin_fill()
forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("black")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(60, 120)
pendown()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
goto(150, 120)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(0, 0)
pendown()


exitonclick()











