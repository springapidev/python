import turtle

#Draw a square
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
   
   
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)
    
    window.exitonclick()
   
draw_square()
