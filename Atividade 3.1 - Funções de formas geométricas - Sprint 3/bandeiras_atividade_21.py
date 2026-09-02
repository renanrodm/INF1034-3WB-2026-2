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
    t.goto(randint(0, ), randint(-400, 400)) #Limita no primeiro quadrante
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(4):
        t.fd(y)
        t.left(90)
        t.fd(x)
        t.left(90)
    t.end_fill()


def desenha_triangulo(x, y, cor, tam):
    t.goto(randint(-400, 400), randint(-400, 400)) #INICIA PRIMEIRO QUADRANTE
    t.pd()
    t.goto(300,80)
    t.goto(190, 300)
    t.goto(80, 80)
    t.pu()


desenha_plano()

desenha_retangulo("blue", 100, 100)

mainloop()