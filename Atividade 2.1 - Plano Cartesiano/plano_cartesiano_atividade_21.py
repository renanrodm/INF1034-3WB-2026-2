from turtle import *;


# variável é a unidade básica da programação!!!
t = Turtle()


## DESENHA PLANO CARTESIANO
t.pu()
t.goto(-400, 0)
t.pd()
t.goto(400, 0)
t.stamp()



t.pu()
t.goto(0, -400)
t.pd()
t.goto(0, 400)
t.left(90)
t.stamp()
t.pu()

#TRIANGULO
t.goto(80, 80) #INICIA PRIMEIRO QUADRANTE
t.pd()
t.goto(300,80)
t.goto(190, 300)
t.goto(80, 80)
t.pu()


#TRAPEZIO
t.goto(-320, 80) #INICIO SEGUNDO QUADRANTE
t.pd()
t.goto(-50, 80)
t.goto(-100, 250)
t.goto(-270, 250)
t.goto(-320, 80)
t.pu()

#HEXAGONO
t.goto(-320, -320) #INICIO TERCEIRO QUADRANTE
t.pu()
t.goto(-280, -220)
t.pd()
t.goto(-240, -289)
t.goto(-160, -289)
t.goto(-120, -220)
t.goto(-160, -151)
t.goto(-240, -151)
t.goto(-280, -220)
t.pu()

#DESENHA ESPIRAL
t.goto(200, -200)
t.pd()

for i in range(100):
    t.circle(i, 30)

t.pu()




mainloop()
