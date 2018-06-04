import turtle

def draw_square(square):
    for i in range(1,5):
        square.forward(100)
        square.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("black")
    brad=turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    angie=turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    shabi=turtle.Turtle()
    shabi.shape('turtle')
    shabi.color('red')
    for j in range(1,4):
        shabi.forward(100)
        shabi.right(120)
    
    window.exitonclick

draw_art()
