from turtle import * 
# i like the turtle shape  
shape('turtle')
#makes the dot purple
pencolor('purple')
dot(5)
#takes turtle to the bottom right corner of square
penup()
goto(-50,-50)
pendown()
#makes the squares red
pencolor('red')
#makes innersquare
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
#sets up outer square to go in same direction 
#although making it go reverse would look cool 
left(90)
#takes you to bottome right corner of outer square
penup()
goto(-150,-150)
pendown()
#makes outer square
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
#places turtle outside of the square
penup()
goto(-250,-250)
pendown()
#makes turtle blue
color('blue')
#points him up 
setheading(90)
#holds animation in window
done()
