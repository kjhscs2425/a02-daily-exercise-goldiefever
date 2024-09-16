import turtle

turtle.shape("turtle")

f=turtle.forward
r=turtle.right
rightangle=90

r(rightangle)

for spiralside in range(1,7):
    f(spiralside*50)
    r(rightangle)
    f(spiralside*50)
    r(rightangle)

turtle.exitonclick()

