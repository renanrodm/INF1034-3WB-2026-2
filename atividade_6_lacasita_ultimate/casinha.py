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
        lua_x = lua_x + 100 * dt
    elif keys[K_a] or keys[K_LEFT]:
        lua_x = lua_x - 100 * dt
    elif keys[K_w] or keys[K_UP]:
        lua_y = lua_y - 100 * dt
    elif keys[K_s] or keys[K_DOWN]:
        lua_y = lua_y + 100 * dt

    ##Define limites da Lua
    limite_esquerdo_lua = lua_raio
    limite_direito_lua = 1280 - lua_raio
    limite_superior_lua = lua_raio
    limite_inferior_lua = 720 - lua_raio

    if lua_x > limite_direito_lua:
        lua_x = limite_direito_lua
    elif lua_x < limite_esquerdo_lua:
        lua_x = limite_esquerdo_lua

    if lua_y > limite_inferior_lua:
        lua_y = limite_inferior_lua
    elif lua_y < limite_superior_lua:
        lua_y = limite_superior_lua

    ### Desenho
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