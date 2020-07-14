import turtle

ethan=turtle.Turtle()

ethan.shape('turtle')
ethan.color('red')
ethan.speed(1)

for i in range(8):
    ethan.right(45)
    ethan.forward(90)
    
ethan.fillcolor('blue')

ethan.penup()
ethan.goto(100,100)

ethan.pendown()
ethan.color('blue')

if ethan.xcor()<300:
    ethan.forward(80)
else:
    ethan.back(100)
    
if ethan.ycor()<300:
    ethan.forward(80)
else:
    ethan.back(100)

turtle.done()