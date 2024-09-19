import turtle

def draw_circle(color, radius, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_rectangle(color, width, height, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Configuración de la ventana
window = turtle.Screen()
window.bgcolor("white")

# Configuración del lápiz
pen = turtle.Turtle()
pen.speed(3)

# Cuerpo del minion
draw_rectangle("yellow", 120, 180, -60, -150)

# Parte inferior azul (pantalones)
draw_rectangle("blue", 120, 60, -60, -150)

# Ojos
draw_circle("white", 20, -35, 10)
draw_circle("white", 20, 15, 10)

# Pupilas
draw_circle("black", 10, -35, 20)
draw_circle("black", 10, 15, 20)

# Gafas
pen.penup()
pen.goto(-55, 10)
pen.pendown()
pen.color("black")
pen.pensize(5)
pen.circle(25)

pen.penup()
pen.goto(5, 10)
pen.pendown()
pen.circle(25)

pen.penup()
pen.goto(-30, 10)
pen.pendown()
pen.forward(40)

# Boca
pen.penup()
pen.goto(-35, -20)
pen.pendown()
pen.right(90)
pen.circle(35, 180)

# Brazos
pen.pensize(10)
pen.color("yellow")
pen.penup()
pen.goto(-60, -50)
pen.pendown()
pen.right(180)
pen.forward(50)

pen.penup()
pen.goto(60, -50)
pen.pendown()
pen.right(180)
pen.forward(50)

# Guantes
pen.color("black")
pen.penup()
pen.goto(-110, -50)
pen.pendown()
pen.circle(10)

pen.penup()
pen.goto(110, -50)
pen.pendown()
pen.circle(10)

# Piernas
pen.color("blue")
pen.pensize(15)
pen.penup()
pen.goto(-40, -150)
pen.pendown()
pen.right(90)
pen.forward(60)

pen.penup()
pen.goto(40, -150)
pen.pendown()
pen.forward(60)

# Zapatos
pen.color("black")
pen.pensize(10)
pen.penup()
pen.goto(-40, -210)
pen.pendown()
pen.right(90)
pen.forward(20)

pen.penup()
pen.goto(40, -210)
pen.pendown()
pen.forward(20)

# Ocultar el lápiz
pen.hideturtle()

# Mantener la ventana abierta
window.mainloop()
