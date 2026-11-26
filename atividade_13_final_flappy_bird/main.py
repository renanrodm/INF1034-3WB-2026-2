import pygame, sys
from pygame.locals import QUIT
from pathlib import Path
DIRETORIO_BASE = Path(__file__).parent

pygame.init()


bg = pygame.image.load(DIRETORIO_BASE / "assets" / "background-night.png")
LARGURA, ALTURA = bg.get_size()
screen = pygame.display.set_mode((LARGURA, ALTURA))
bg = bg.convert()
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

pipe_cano_baixo = pygame.image.load(DIRETORIO_BASE / "assets" / "pipe-red.png").convert_alpha()
pipe_cano_cima = pygame.transform.flip(pipe_cano_baixo, False, True)
LARGURA_PIPE_CANO, ALTURA_PIPE_CANO = pipe_cano_baixo.get_size()


tile_size_joguinho = 64
fonte = pygame.font.SysFont("Arial", 20)
texto_colisao = ""
player_anim_time = 0
player_curr_frame = 0

yellowbird_downflap = pygame.image.load(DIRETORIO_BASE / "assets" / "player" / "yellowbird-downflap.png").convert_alpha()
yellowbird_midflap = pygame.image.load(DIRETORIO_BASE / "assets" / "player" / "yellowbird-midflap.png").convert_alpha()
yellowbird_upflap = pygame.image.load(DIRETORIO_BASE / "assets" / "player" / "yellowbird-upflap.png").convert_alpha()
yellowbird_frames = [yellowbird_downflap, yellowbird_midflap, yellowbird_upflap]
LARGURA_YELLOWBIRD, ALTURA_YELLOWBIRD = yellowbird_frames[0].get_size()

pos_x = 48
pos_y = 0
vel_y = 0
gravidade = 0.001

mapa_x = 0 
vel_mapa = 0.2

mapa_joguinho = [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXUXXXXXXXXXXXXXXXXXXXXXXXXXXUXXXXXXXXXXXXXXXXXUXXXXXXXXXXXXXXUXXXXXXXXXXXXXX",  # linha 0 (y = 0)
        "XXXXXXUXXXXXXXUXXXXXXXXXUXXXXXUXXXXXXXXUXXXXXUXXXXXXXXXXXUXXUXXXXXXXXXXXXXXXXXXXXUXXXXXXXXXXXXXXUXXXXX",  # linha 1 (y = 64)
        "XXXXXXXXXXUXXXXXXXXXXUXXXXXXXXXXXUXXXXXXXXXXXXXXXXXUXXXXXXXXXXXXXXXXXUXXXXXUXXXXXXXXXXXXXXUXXXXXXXXXXX",  # linha 2 (y = 128)
        "XXXXXXXXXXXXXXXXXXUXXXXXXXXDXXXXXXXXUXXXXXUXXXXXXXXXXXDXXXXXXXXUXXXXXXXXDXXXXXXXXXXXUXXDXXXXXUXXXXXXXX",  # linha 3 (y = 192)
        "XXXXXXDXXXXXXXDXXXXXXXXXDXXXXXDXXXXXXXXDXXXXXDXXUXXXXXXXXDXXDXXXXXUXXXXXXXXXXXUXXDXXXXXXXXXXXXXXDXXXXX",  # linha 4 (y = 256)
        "XXXXXXXXXXDXXXXXXXXXXDXXXXXXXXXXXDXXXXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXXXDXXXXXDXXXXXXXXXXXXXXDXXXXXXXXXXX",  # linha 5 (y = 320)
        "XXXXXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXXXDXXXXXDXXXXXXXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXXXXXXDXXXXXXXXDXXXXXXXX",  # linha 6 (y = 384)
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXXXDXXXXXXXXXXXDXXXXXXXXXXXXXXXXXXXXXXX",  # linha 7 (y = 448)
    ]


tiles_mapa = {
    "D": (0, 0, tile_size_joguinho, tile_size_joguinho), 
    "U": (64, 0, tile_size_joguinho, tile_size_joguinho),
}

obstaculos = []      
colliders_mapa = []


for i in range(len(mapa_joguinho)):
    for j in range(len(mapa_joguinho[i])):
        letra = mapa_joguinho[i][j]
        x_mundo = j * tile_size_joguinho

        if letra == "D":  # Cano de baixo
            y_mundo = i * tile_size_joguinho
            rect = pygame.Rect(x_mundo, y_mundo, LARGURA_PIPE_CANO, ALTURA_PIPE_CANO)
            obstaculos.append((pipe_cano_baixo, rect))
            colliders_mapa.append(rect)

        elif letra == "U":  # Cano de cima
            y_boca = (i + 1) * tile_size_joguinho
            y_mundo = y_boca - ALTURA_PIPE_CANO
            rect = pygame.Rect(x_mundo, y_mundo, LARGURA_PIPE_CANO, ALTURA_PIPE_CANO)
            obstaculos.append((pipe_cano_cima, rect))
            colliders_mapa.append(rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vel_y = -0.35 #valores negativos aqui sobem no eixo y (esquisito!!)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                vel_y = -0.35
            

    clock.tick(60)
    delta_time = clock.get_time()
    old_mapa_x = mapa_x
    mapa_x = mapa_x - vel_mapa * delta_time #mapa andando


    # ==================================
    #       MOVIMENTAÇÃO EIXOS E COLISÕES
    # ==================================
   
    
    collider_jogador_x = pygame.Rect(pos_x - mapa_x, pos_y, LARGURA_YELLOWBIRD, ALTURA_YELLOWBIRD)
    idx_x = collider_jogador_x.collidelist(colliders_mapa)
    if idx_x != -1:
        mapa_x = old_mapa_x

    old_pos_y = pos_y
    vel_y = vel_y + gravidade * delta_time #Acelerando a cada loop (valores positivos descem no eixo y)
    pos_y += vel_y * delta_time #posicao y sempre em relação a velocidade.

    collider_jogador_y = pygame.Rect(pos_x - mapa_x, pos_y, LARGURA_YELLOWBIRD, ALTURA_YELLOWBIRD)
    indice_colisor = collider_jogador_y.collidelist(colliders_mapa)
    if indice_colisor != -1:
        pos_y = old_pos_y 
        vel_y = 0
        texto_colisao = str(colliders_mapa[indice_colisor])
        
    # ==================================
    #         ANIMAÇÃO PLAYER
    # ==================================
        
    total_frames = len(yellowbird_frames)


    player_curr_frame = player_curr_frame % total_frames

    player_anim_time = player_anim_time + delta_time
    if player_anim_time / 1000 > 0.1:
        player_curr_frame = (player_curr_frame + 1) % total_frames
        player_anim_time = 0

    # ==================================
    #             DESENHOS
    # ==================================
    screen.blit(bg, (0, 0))

    frame_atual = yellowbird_frames[player_curr_frame]


    screen.blit(frame_atual, (pos_x, pos_y)) #Desenha o player 
    
    
    for img_pipe, rect in obstaculos: #Desenho dos canos
        screen.blit(img_pipe, (rect.x + mapa_x, rect.y))
    pygame.draw.rect(screen, "yellow", (pos_x, pos_y, LARGURA_YELLOWBIRD, ALTURA_YELLOWBIRD), 2)

    

    pygame.display.update()