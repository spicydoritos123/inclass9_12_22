from turtle import *
#settingup window size 
setup(640,640)
#i like the turtle but hes not to be seen for thius excersize
shape('turtle')
hideturtle()
#setting up the pensize
pensize(5)

#setting turtle at base of red circle 
penup()
goto(0,90)
pendown()
#drawing and coloring the red circle 
fillcolor('red')
begin_fill()
circle(50)
end_fill()
#setting turtle at base of yellow circle
penup()
goto(0,-50)
pendown()
#drawing and coloring the circle yellow
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()
#setting turtle at base of green circle
penup()
goto(0,-190)
pendown()
#drawing and coloring green circle
fillcolor('green')
begin_fill()
circle(50)
end_fill()
#setting turtle at bottom right of rectangle
penup()
goto(-70,-230)
pendown()
#drawing the traffic light box
setheading(360)
forward(140)
left(90)
forward(460)
left(90)
forward(140)
left(90)
forward(460)

done()