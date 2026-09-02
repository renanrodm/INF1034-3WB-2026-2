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

def desenha_retangulo(x, y, tam, cor):
    t.up()
    t.goto(x, y) #Limita no primeiro quadrante
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(4):
        t.fd(y)
        t.left(90)
        t.fd(x)
        t.left(90)
    t.end_fill()

desenha_plano()

x = randint(0, 200)
y = randint(0, 200)
desenha_retangulo(x, y)

mainloop()