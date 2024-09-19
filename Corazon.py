import turtle

window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(3)

pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

pen.penup()
pen.goto(0, -40)
pen.color("black")
pen.write("éxito inge", align="center", font=("Arial", 16, "bold"))
pen.hideturtle()

window.mainloop()
