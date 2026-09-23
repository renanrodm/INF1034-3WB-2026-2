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
mixer.music.load("ironman.mp3")
mixer.music.play(-1)

background_color = "#062632"
texto = "Eu sou o Homem de Ferro"
lua_x = 130
lua_y = 130
lua_raio = 70
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
    dt = clock.get_time() / 1000
    screen.fill(background_color)
    draw.rect(screen, "#4CAF50", (0, 600, 1280, 120))

    draw.circle(screen, "#FFFFFF", (lua_x, lua_y), lua_raio)

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