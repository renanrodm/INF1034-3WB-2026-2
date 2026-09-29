from pygame import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

init()
screen = display.set_mode((1280, 720))
running = True
clock = time.Clock()

fonte = font.Font("font_stark.otf", 40)
image = image.load("ironman.png")
image = transform.scale(image, (150, 180))
# mixer.music.load("ironman.mp3")
# mixer.music.play(-1)
som_manha = mixer.Sound("manha.mp3")
som_tarde = mixer.Sound("tarde.mp3")
som_noite = mixer.Sound("noite.mp3")

background_color = "#062632"
texto = "Eu sou o Homem de Ferro"
corpo_celeste_x = 130
corpo_celeste_y = 130
corpo_celeste_raio = 70
corpo_celeste_cor = "#FFFFFF"
nuvem_x = 420
nuvem_x_inicial = nuvem_x
nuvem_y = 150
nuvem_vel = 60
casa_x = 500
casa_largura = 260
casa_altura = 200
casa_y = 600 - casa_altura  
arvore_x = 980
arvore_tronco_altura = 120
arvore_y = 600 - 60 - arvore_tronco_altura  

while running:
    
    clock.tick(60)
    
    for ev in event.get():
        if ev.type == QUIT:
            running = False

        if ev.type == MOUSEBUTTONUP:
            mouse_x, mouse_y = ev.pos

            if mouse_x < 426:
                som_manha.play(maxtime=5000)

            elif mouse_x < 853:
                som_tarde.play(maxtime=5000)

            else:
                som_noite.play(maxtime=5000)

        
    dt = clock.get_time() / 1000
    
    ##Comportamento nuvem
    nuvem_x = nuvem_x + nuvem_vel * dt

    limite_esquerdo = 45
    limite_direito = 1280 - 215
    if nuvem_x >= limite_direito:
        nuvem_x = limite_direito
        nuvem_vel = nuvem_vel * -1 ##para inverter o sentido da velocidade 
    elif nuvem_x <= limite_esquerdo:
        nuvem_x = limite_esquerdo
        nuvem_vel = nuvem_vel * -1 ##para inverter o sentido da velocidade 


    ##Comportamento lua teclado
    keys = key.get_pressed()
    if keys[K_d] or keys[K_RIGHT]:
        corpo_celeste_x = corpo_celeste_x + 100 * dt
    elif keys[K_a] or keys[K_LEFT]:
        corpo_celeste_x = corpo_celeste_x - 100 * dt
    elif keys[K_w] or keys[K_UP]:
        corpo_celeste_y = corpo_celeste_y - 100 * dt
    elif keys[K_s] or keys[K_DOWN]:
        corpo_celeste_y = corpo_celeste_y + 100 * dt

     ##Comportamento mouse lua
    mouse_x, mouse_y = mouse.get_pos()
    corpo_celeste_x = mouse_x
    corpo_celeste_y = mouse_y

    ##Define limites da Lua
    limite_esquerdo_corpo_celeste = corpo_celeste_raio
    limite_direito_corpo_celeste = 1280 - corpo_celeste_raio
    limite_superior_corpo_celeste = corpo_celeste_raio
    limite_inferior_corpo_celeste = 720 - corpo_celeste_raio

    if corpo_celeste_x > limite_direito_corpo_celeste:
        corpo_celeste_x = limite_direito_corpo_celeste
    elif corpo_celeste_x < limite_esquerdo_corpo_celeste:
        corpo_celeste_x = limite_esquerdo_corpo_celeste

    if corpo_celeste_y > limite_inferior_corpo_celeste:
        corpo_celeste_y = limite_inferior_corpo_celeste
    elif corpo_celeste_y < limite_superior_corpo_celeste:
        corpo_celeste_y = limite_superior_corpo_celeste

   


    ### Desenho


    screen.fill(background_color)

    if corpo_celeste_x < 426:
        # Fica de manhã e desenha sol com raios
        background_color = "#F6C56B"
        corpo_celeste_cor = "#FFD700"
        desenhar_raios = True
    elif corpo_celeste_x < 853:
        # Fica de tarde e desenha sol com raios
        background_color = "#5DADE2"
        corpo_celeste_cor = "#FFD700"
        desenhar_raios = True
    else:
        # Fica de noite e desenha lua sem raios
        background_color = "#062632"
        corpo_celeste_cor = "#FFFFFF"
        desenhar_raios = False

    if desenhar_raios:
        cor_raios = "#FFD700"
        largura_raios = 5

        # Raios horizontais
        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x - 105, corpo_celeste_y),
            (corpo_celeste_x - 80, corpo_celeste_y),
            largura_raios
        )

        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x + 80, corpo_celeste_y),
            (corpo_celeste_x + 105, corpo_celeste_y),
            largura_raios
        )

        # Raios verticais
        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x, corpo_celeste_y - 105),
            (corpo_celeste_x, corpo_celeste_y - 80),
            largura_raios
        )

        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x, corpo_celeste_y + 80),
            (corpo_celeste_x, corpo_celeste_y + 105),
            largura_raios
        )

        # Raios diagonais
        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x - 75, corpo_celeste_y - 75),
            (corpo_celeste_x - 55, corpo_celeste_y - 55),
            largura_raios
        )

        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x + 55, corpo_celeste_y - 55),
            (corpo_celeste_x + 75, corpo_celeste_y - 75),
            largura_raios
        )

        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x - 75, corpo_celeste_y + 75),
            (corpo_celeste_x - 55, corpo_celeste_y + 55),
            largura_raios
        )

        draw.line(
            screen,
            cor_raios,
            (corpo_celeste_x + 55, corpo_celeste_y + 55),
            (corpo_celeste_x + 75, corpo_celeste_y + 75),
            largura_raios
        )

    draw.circle(
        screen,
        corpo_celeste_cor,
        (corpo_celeste_x, corpo_celeste_y),
        corpo_celeste_raio
    )
                

    draw.rect(screen, "#4CAF50", (0, 600, 1280, 120))

    draw.circle(screen, corpo_celeste_cor, (corpo_celeste_x, corpo_celeste_y), corpo_celeste_raio)

    draw.circle(screen, "#FFFFFF", (nuvem_x, nuvem_y), 45)
    draw.circle(screen, "#FFFFFF", (nuvem_x + 55, nuvem_y - 15), 55)
    draw.circle(screen, "#FFFFFF", (nuvem_x + 120, nuvem_y), 50)
    draw.circle(screen, "#FFFFFF", (nuvem_x + 175, nuvem_y + 10), 40)
    draw.rect(screen, "#5C3A21", (arvore_x, arvore_y + 60, 30, arvore_tronco_altura))
    draw.circle(screen, "#2E8B57", (arvore_x + 15, arvore_y), 80)
    draw.polygon(screen, "#824124", [
        (casa_x - 40, casa_y),
        (casa_x + casa_largura + 40, casa_y),
        (casa_x + casa_largura / 2, casa_y - 150)])
    draw.rect(screen, "#3B3B3B", (casa_x, casa_y, casa_largura, casa_altura))
    draw.rect(screen, "#F5F236", (casa_x + 30, casa_y + 50, 60, 70))
    draw.rect(screen, "#4B2E13", (casa_x + 150, casa_y + 70, 80, 130))
    draw.circle(screen, "#000000", (casa_x + 220, casa_y + 135), 5)
    screen.blit(image, (100, 420))
    texto_render = fonte.render(texto, True, "#FFD700")
    screen.blit(texto_render, (30, 370))
    display.update()
quit()