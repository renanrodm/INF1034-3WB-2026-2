from turtle import *
from time import sleep

from random import randint

t = Turtle()
t.speed(0)

def desenha_plano():
    t.pu()
    t.goto(-400, 0)
    t.pd()
    t.goto(400, 0) # Eixo X
    t.stamp()
    t.pu()
    t.goto(0,-400)
    t.pd()
    t.goto(0, 400) # Eixo y
    t.left(90)
    t.stamp()
    
#TRIANGULO
def triangulo(x, y, tam, cor):
    t.up()
    t.goto(x, y)
    t.setheading(0) #Para resetar a rotação do cursor
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(3):
        t.fd(tam)
        t.left(120)
    t.end_fill()

#TRAPEZIO
def trapezio(x, y, tam, cor):
    t.pu()
    t.setheading(0)
    t.goto(x, y)
    t.fillcolor(cor)
    t.begin_fill()
    t.pd()

    t.fd(tam)
    t.left(120)
    t.fd(tam)
    t.left(60)
    t.fd(tam)
    t.left(60)
    t.fd(tam)
    t.left(120)
    t.fd(tam)



    t.end_fill()

#HEGXAGONO
def hexagono(x, y, tam, cor):
    t.pu()
    t.setheading(0)
    t.goto(x, y)
    t.fillcolor(cor)
    t.begin_fill()
    t.pd()
    for i in range(6):
        t.fd(tam)
        t.left(360/6)
        t.fd(tam)
    t.end_fill()

#ESPIRAL
def espiral(x, y, tam, cor):
    t.pu()
    t.setheading(0)
    t.goto(x, y)
    t.fillcolor(cor)
    t.begin_fill()
    t.pd()
    for i in range(100):
        t.circle(i, tam)
    t.end_fill()

#POLÍGONO EXTRA
def poligono_generico(x, y, tam, cor, qtde_lados):
    t.pu()
    t.setheading(0)
    t.goto(x, y)
    t.fillcolor(cor)
    t.begin_fill()
    t.pd()
    for i in range(qtde_lados):
        t.fd(tam)
        t.left(360/qtde_lados)
        t.fd(tam)
    t.end_fill()

#MAIN
desenha_plano()


x1 = randint(1, 200)
y1 = randint(1, 200)
triangulo(x1, y1, 100, "red")

x2 = randint(-200, -1)
y2 = randint(1, 200)
trapezio(x2, y2, 100, "green")

x3 = randint(-200, -1)
y3 = randint(-200, -1)
hexagono(x3, y3, 30, "blue")

x4 = randint(1, 200)
y4 = randint(-200, -1)
espiral(x4, y4, 20, "purple")

x5 = randint(1, 200)
y5 = randint(-200, -1)
poligono_generico(x5, y5, 35, "grey", 8)

mainloop()