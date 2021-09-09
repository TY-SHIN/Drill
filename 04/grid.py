import turtle

a = 0

turtle.penup()
turtle.goto(-250,-250)

turtle.pendown()
while (a<=5) :
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    if(a%2) :
        turtle.right(90)
    else :
        turtle.left(90)
    turtle.forward(100)
    if(a%2) :
        turtle.right(90)
    else :
        turtle.left(90)
        
    a += 1

a=0
turtle.right(90)
turtle.forward(100)

while (a<=5) :
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    if(a%2) :
        turtle.right(90)
    else :
        turtle.left(90)
    turtle.forward(100)
    if(a%2) :
        turtle.right(90)
    else :
        turtle.left(90)
        
    a += 1

turtle.exitonclick()
