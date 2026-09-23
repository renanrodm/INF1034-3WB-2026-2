# PRINCIPAL (400XP)

# Criar uma função para desenhar o plano cartesiano (25XP);
# Devem ser desenhadas as seguintes funções matemáticas:
#     - y = √x (50XP)
#     - y = 1/x (50XP)
#     - y = 2^x (50XP)
#     - y = 5 - x^2 (75XP)
#     - y = x^2 - 5x + 6 (75XP)
#     - y = x^3 - x^2 - x + 1 (75XP)
# OBS.: Dar o clear depois de desenhar cada função.

# EXTRA (100XP)

# Fazer uma função para rodar uma "corrida de tartarugas" para N tartarugas (a função só receberá o N como parâmetro).
from math import sqrt
from turtle import *
from time import sleep


t = Turtle()

def desenha_plano_cartesiano(x=300, y=300):
    #Eixo x
    t.color("black")
    t.pu()
    t.setheading(0)
    t.goto(-x, 0)
    t.pd()
    t.goto(x, 0)
    t.stamp()

    #Eixo y
    t.pu()
    t.left(90)
    t.goto(0, -y)
    t.pd()
    t.goto(0, y)
    t.stamp()
    t.setheading(0)

def raiz_quadrada(x):
    t.color("red")
    return x**(1/2)

def inversa(x):
    t.color("blue")
    return 1 / x 

def exponencial(x):
    t.color("green")
    return 2**x

def parabola_1(x):
    t.color("orange")
    return 5 - x**2

def parabola_2(x):
    t.color("purple")
    return x**2 - 5*x + 6

def cubica(x):
    t.color("brown")
    return x**3 - x**2 - x + 1

t.speed(0)




desenha_plano_cartesiano()
ESCALA = 20
t.pu()
t.goto(0, raiz_quadrada(0)*ESCALA)
t.pd()
for x in range(0, 150):
    t.goto(x, raiz_quadrada(x)*ESCALA)

sleep(1)
t.clear()

desenha_plano_cartesiano()

t.pu()
t.goto(12, inversa(12) * 3000)
t.pd()

for x in range(12, 300):
  t.goto(x, inversa(x) * 3000)

sleep(1)
t.clear()


desenha_plano_cartesiano()

### EXPONENCIAL
t.pu()
t.goto(-200, exponencial(-200 / 25))
t.pd()
for x in range(-201, 200):
    t.goto(x, exponencial(x / 25))

sleep(1)
t.clear()


desenha_plano_cartesiano()

t.pu()
t.goto(-10, parabola_1(-10))
t.pd()
for x in range(-10, 11):
    t.goto(x, parabola_1(x))

sleep(1)
t.clear()


desenha_plano_cartesiano()

t.pu()
t.goto(-10, parabola_2(-10))
t.pd()
for x in range(-10, 11):
    t.goto(x, parabola_2(x))

sleep(1)
t.clear()


desenha_plano_cartesiano()

t.pu()
t.goto(-5, cubica(-5))
t.pd()
for x in range(-5, 6):
    t.goto(x, cubica(x))

mainloop()