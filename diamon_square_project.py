import turtle

#Draw a square
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window=turtle.Screen()
    window.bgcolor("yellow")
   
   #Create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
   
    for i in range(1,37):
         draw_square(brad)
         brad.right(10)

   #Create the turtle angle- draws a circle

    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
 
    window.exitonclick()
   
draw_art()
