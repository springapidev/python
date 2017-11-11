import turtle

#Draw a square
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
        
def draw_art():
    window=turtle.Screen()
    window.bgcolor("yellow")
   
   #Create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.forward(100)
    brad.backward(50)
    brad.right(50)
    brad.backward(50)
    #brad.speed(0)
   
   
         
    window.exitonclick()
   
draw_art()
