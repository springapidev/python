import turtle

#Draw a square
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
#Move forware and turn right
def draw_square(some_turtle):
   for i in range(1,5):
        some_turtle.forward(150)
        some_turtle.right(140)
def draw_squares(some_turtles):
   for i in range(1,5):
        some_turtles.forward(80)
        some_turtles.right(75)
        
def draw_art():
    window=turtle.Screen()
    window.bgcolor("yellow")
   
   #Create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    #brad.speed(2)
   
   

   #Create the turtle angle- draws a circle

    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    
    for i in range(1,4):
        draw_square(brad)
        brad.right(10)
        for i in range(1,10):
            draw_squares(brad)
            brad.right(5)
         
    window.exitonclick()
   
draw_art()
