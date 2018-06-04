import turtle

def draw_diamond(d):
    for i in range(1,3):
        d.forward(100)
        d.right(150)
        d.forward(100)
        d.right(30)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("white")
    brad=turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(2)
    for i in range(1,37):
        draw_diamond(brad)
        brad.right(10)
    
    window.exitonclick

draw_art()
