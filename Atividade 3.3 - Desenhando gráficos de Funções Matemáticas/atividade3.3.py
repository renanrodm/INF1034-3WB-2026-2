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
from turtle import *


t = Turtle()

def desenha_plano_cartesiano(x, y):
    #Eixo x
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



desenha_plano_cartesiano(300, 300)

mainloop()