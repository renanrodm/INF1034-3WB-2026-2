from turtle import *
from time import sleep


t = Turtle()

def desenha_estrela(x, y, larg, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(5):
        t.fd(larg)
        t.right(144)
    t.end_fill()

def desenha_triangulo_isosceles(x, y, larg, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(3):
        t.fd(larg)
        t.left(120)
    t.end_fill()

def desenha_retangulo(x, y, larg, alt, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.fd(larg)
        t.left(90)
        t.fd(alt)
        t.left(90)
    t.end_fill()

def desenha_losango(x, y, larg, cor):
    t.pu()
    t.goto(x, y)
    t.setheading(0)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()

    t.left(30)
    t.fd(larg)

    t.right(60)
    t.fd(larg)

    t.right(120)
    t.fd(larg)

    t.right(60)
    t.fd(larg)

    t.end_fill()

def desenha_circulo(x, y, raio, cor):
    t.pu()
    t.goto(x, y - raio)
    t.setheading(0)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()


def desenha_italia():
    desenha_retangulo(0, 0, 100, 200, "#009246")
    desenha_retangulo(100, 0, 100, 200, "white")
    desenha_retangulo(200, 0, 100, 200, "#ce2b37")

def desenha_franca():
    desenha_retangulo(0, 0, 100, 200, "#3C5AA3")
    desenha_retangulo(100, 0, 100, 200, "white")
    desenha_retangulo(200, 0, 100, 200, "#BE0127")

def desenha_cuba():
    desenha_retangulo(x=0, y=0, larg=400, alt=60, cor="#002C5F")
    desenha_retangulo(x=0, y=60, larg=400, alt=60, cor="white")
    desenha_retangulo(x=0, y=120, larg=400, alt=60, cor="#002C5F")
    desenha_retangulo(x=0, y=180, larg=400, alt=60, cor="white")
    desenha_retangulo(x=0, y=240, larg=400, alt=60, cor="#002C5F")
    t.left(30) # direciona o ponteiro para desenhar o triangulo na ordem correta
    desenha_triangulo_isosceles(0, 0, 300, "#CC0D0D")
    t.right(30)
    estrela(30, 170, 100, "white")

def siria():
    desenha_retangulo(x=0, y=0, larg=300, alt=66, cor="black")
    desenha_retangulo(x=0, y=66, larg=300, alt=66, cor="white")
    desenha_retangulo(x=0, y=132, larg=300, alt=66, cor="#017A3D")
    desenha_estrela(x=70, y=105, larg=40, cor="#CE1126")
    desenha_estrela(x=120, y=105, larg=40, cor="#CE1126")
    desenha_estrela(x=170, y=105, larg=40, cor="#CE1126")

def brasil():
    desenha_retangulo(x=0, y=0, larg=300, alt=200, cor="#009B3A")
    desenha_losango(20, 100, 150, "yellow")
    desenha_circulo(150, 100, 45, "#002776")
    t.pu()
    t.goto(0, 0)
    desenha_retangulo(x=105, y=95, larg=90, alt=7, cor="white")

def grecia():
    desenha_retangulo(x=0, y=0, larg=300, alt=200, cor="#0D5EAF")
    desenha_retangulo(x=0, y=22, larg=300, alt=22, cor="white")
    desenha_retangulo(x=0, y=66, larg=300, alt=22, cor="white")
    desenha_retangulo(x=0, y=110, larg=300, alt=22, cor="white")
    desenha_retangulo(x=0, y=154, larg=300, alt=22, cor="white")

    desenha_retangulo(x=0, y=110, larg=90, alt=90, cor="#0D5EAF")

    desenha_retangulo(34, 110, 22, 90, "white")
    desenha_retangulo(0, 144, 90, 22, "white")

def reino_unido():

    desenha_retangulo(x=0, y=0, larg=300, alt=200, cor="#012169")
    desenha_retangulo(x=0, y=0, larg=300, alt=200, cor="#012169")
    desenha_retangulo(x=120, y=0, larg=60, alt=200, cor="white")
    desenha_retangulo(x=0, y=70, larg=300, alt=60, cor="white")
    desenha_retangulo(x=130, y=0, larg=40, alt=200, cor="red")
    desenha_retangulo(x=0, y=80, larg=300, alt=40, cor="red")



t.speed(0)

reino_unido()


mainloop()