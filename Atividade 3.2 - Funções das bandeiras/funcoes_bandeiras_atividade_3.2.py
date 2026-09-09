from turtle import *
from time import sleep


t = Turtle()
t.speed(0)


def estrela(tamanho):
    for i in range(5):
        t.fd(tamanho)
        t.right(144)


def triangulo(tam):
    for i in range(3):
        t.fd(tam)
        t.left(120)


def desenha_retangulo(cor="#FFFFFF", base=100, altura=200):
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.fd(base)
        t.left(90)
        t.fd(altura)
        t.left(90)
    t.end_fill()


def italia():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#239E46", base=100, altura=200)
    t.pu()
    t.goto(100, 0)
    desenha_retangulo("#FFFFFF", base=100, altura=200)
    t.pu()
    t.goto(200, 0)
    desenha_retangulo("#BE0127", base=100, altura=200)
    t.pu()
    t.goto(0, 0)


def franca():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#3C5AA3", base=100, altura=200)
    t.pu()
    t.goto(100, 0)
    desenha_retangulo("#FFFFFF", base=100, altura=200)
    t.pu()
    t.goto(200, 0)
    desenha_retangulo("#BE0127", base=100, altura=200)
    t.pu()
    t.goto(0, 0)


def cuba():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#002C5F", base=300, altura=200)
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#FFFFFF", base=300, altura=50)
    t.pu()
    t.goto(0, 75)
    desenha_retangulo("#FFFFFF", base=300, altura=50)
    t.pu()
    t.goto(0, 150)
    desenha_retangulo("#FFFFFF", base=300, altura=50)
    t.pu()
    t.goto(0, 100)
    t.fillcolor("#D62828")
    t.begin_fill()
    triangulo(150)
    t.end_fill()
    t.pu()
    t.goto(120, 90)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    estrela(18)
    t.end_fill()
    t.pu()
    t.goto(0, 0)


def siria():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#D21034", base=300, altura=66)
    t.pu()
    t.goto(0, 66)
    desenha_retangulo("#FFFFFF", base=300, altura=66)
    t.pu()
    t.goto(0, 132)
    desenha_retangulo("#000000", base=300, altura=66)
    t.pu()
    t.goto(115, 75)
    t.fillcolor("#0B6E4F")
    t.begin_fill()
    triangulo(90)
    t.end_fill()
    t.pu()
    t.goto(150, 90)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    estrela(12)
    t.end_fill()
    t.pu()
    t.goto(0, 0)


def tunisia():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#E70013", base=300, altura=200)
    t.pu()
    t.goto(90, 0)
    desenha_retangulo("#FFFFFF", base=120, altura=200)
    t.pu()
    t.goto(145, 70)
    t.fillcolor("#E70013")
    t.begin_fill()
    triangulo(60)
    t.end_fill()
    t.pu()
    t.goto(0, 0)


def brasil():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#009B3A", base=300, altura=200)

    t.pu()
    t.goto(75, 25)
    t.fillcolor("#FFDF00")
    t.begin_fill()
    t.pd()
    t.goto(150, 100)
    t.goto(225, 25)
    t.goto(150, -50)
    t.goto(75, 25)
    t.end_fill()

    t.pu()
    t.goto(120, 35)
    t.fillcolor("#002776")
    t.begin_fill()
    t.pd()
    for i in range(36):
        t.fd(4)
        t.left(10)
    t.end_fill()

    t.pu()
    t.goto(150, 55)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    estrela(15)
    t.end_fill()
    t.pu()
    t.goto(0, 0)


def togo():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#D21034", base=90, altura=200)

    t.pu()
    t.goto(90, 0)
    desenha_retangulo("#006A4E", base=210, altura=50)
    t.pu()
    t.goto(90, 50)
    desenha_retangulo("#FFCE00", base=210, altura=50)
    t.pu()
    t.goto(90, 100)
    desenha_retangulo("#FFFFFF", base=210, altura=50)
    t.pu()
    t.goto(90, 150)
    desenha_retangulo("#FFCE00", base=210, altura=25)
    t.pu()
    t.goto(90, 175)
    desenha_retangulo("#006A4E", base=210, altura=25)

    t.pu()
    t.goto(35, 80)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    estrela(18)
    t.end_fill()
    t.pu()
    t.goto(0, 0)


def panama():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#D21034", base=150, altura=100)
    t.pu()
    t.goto(150, 0)
    desenha_retangulo("#FFFFFF", base=150, altura=100)
    t.pu()
    t.goto(0, 100)
    desenha_retangulo("#FFFFFF", base=150, altura=100)
    t.pu()
    t.goto(150, 100)
    desenha_retangulo("#D21034", base=150, altura=100)

    t.pu()
    t.goto(150, 100)
    t.fillcolor("#002C5F")
    t.begin_fill()
    estrela(13)
    t.end_fill()
    t.pu()
    t.goto(0, 0)


def reino_unido():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#012169", base=300, altura=200)

    t.pu()
    t.goto(120, 0)
    desenha_retangulo("#FFFFFF", base=60, altura=200)
    t.pu()
    t.goto(0, 70)
    desenha_retangulo("#FFFFFF", base=300, altura=60)

    t.pu()
    t.goto(130, 0)
    desenha_retangulo("#C8102E", base=40, altura=200)
    t.pu()
    t.goto(0, 80)
    desenha_retangulo("#C8102E", base=300, altura=40)
    t.pu()
    t.goto(0, 0)


def grecia():
    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#0D5EAF", base=300, altura=200)

    t.pu()
    t.goto(0, 0)
    desenha_retangulo("#FFFFFF", base=300, altura=20)
    t.pu()
    t.goto(0, 40)
    desenha_retangulo("#FFFFFF", base=300, altura=20)
    t.pu()
    t.goto(0, 80)
    desenha_retangulo("#FFFFFF", base=300, altura=20)
    t.pu()
    t.goto(0, 120)
    desenha_retangulo("#FFFFFF", base=300, altura=20)
    t.pu()
    t.goto(0, 160)
    desenha_retangulo("#FFFFFF", base=300, altura=20)

    t.pu()
    t.goto(120, 0)
    desenha_retangulo("#FFFFFF", base=60, altura=200)
    t.pu()
    t.goto(0, 80)
    desenha_retangulo("#FFFFFF", base=300, altura=40)
    t.pu()
    t.goto(0, 0)


italia()
sleep(2)
t.clear()

franca()
sleep(2)
t.clear()

cuba()
sleep(2)
t.clear()

siria()
sleep(2)
t.clear()

tunisia()
sleep(2)
t.clear()

brasil()
sleep(2)
t.clear()

togo()
sleep(2)
t.clear()


panama()
sleep(2)
t.clear()

reino_unido()
sleep(2)
t.clear()

grecia()
sleep(2)
t.clear()





mainloop()