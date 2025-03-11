import turtle
turtle.speed(5)
turtle.pencolor("blue")
turtle.pensize(30)

def dibujar_cuadro():
    for _ in range (4):
        turtle.forward(300)
        turtle.right(90)
        
dibujar_cuadro()
turtle.goto(150, 0)
turtle.pencolor("red")
turtle.pensize(30)
turtle.right(90)
turtle.forward(300)

turtle.pensize(0)
turtle.right(90)
turtle.pencolor("blue")
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.pencolor("red")
turtle.pensize(30)
turtle.forward(300)



