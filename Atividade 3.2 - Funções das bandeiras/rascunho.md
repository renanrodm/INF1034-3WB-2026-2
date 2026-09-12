```
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
```
