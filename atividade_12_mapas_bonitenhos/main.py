import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
tile_size = 60
tile_size_joguinho = 64
tileset = pygame.image.load("atividade_12_mapas_bonitenhos/plataform_tileset.png")


pos_x = 0
pos_y = 0

vel_y = 0
gravidade = 0.001
forca_pulo = -0.60
no_chao = False

mapa_joguinho = [
  "XXXXXXXXXXXXXX",
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXBXXXXXXXXX", 
  "GGGGGGGAAGGGGG", 
  "TTTTTTTPPTTTTT", 
  "TTTTTTTPPTTTTT",
]


tiles_mapa = {
    #JUSTIFICATIVA TECNICA: MAPEIA A COORDENADA DE CADA TILE PARA EVITAR IFS NO SCREEN.BLIT()
    "G": (0, 0, tile_size_joguinho, tile_size_joguinho),
    "B": (0, 128, tile_size_joguinho, tile_size_joguinho),
    "P": (128, 64, tile_size_joguinho, tile_size_joguinho),
    "T": (64, 0, tile_size_joguinho, tile_size_joguinho)

}

colliders_mapa = [] 
#JUSTIFICATIVA TECNICA: A ideia é ter um array de blocos colisores para utilizar colliderlist ao inves de colliderect.
for i in range(len(mapa_joguinho)):
    for j in range(len(mapa_joguinho[i])):
        if mapa_joguinho[i][j] in ["G", "B"]:
            bloco_rect = pygame.Rect(j * tile_size_joguinho, i * tile_size_joguinho, 64, 64)
            colliders_mapa.append(bloco_rect)

#EXPLICAÇÃO: 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    delta_time = clock.get_time()

    
    


    keys = pygame.key.get_pressed()


    # ==================================
    #       MOVIMENTAÇÃO EIXO X
    # ==================================
    old_pos_x = pos_x
    
    if keys[pygame.K_RIGHT]:
        pos_x = pos_x + 0.2*delta_time
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - 0.2*delta_time

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)
    if collider_jogador.collidelist(colliders_mapa) != -1:
        pos_x = old_pos_x

    # ==================================
    #       MOVIMENTAÇÃO EIXO Y
    # ==================================
    old_pos_y = pos_y

    if keys[pygame.K_SPACE] and no_chao:
            vel_y = forca_pulo
            no_chao = False

    ## Gravidade
    vel_y = vel_y + gravidade * delta_time #Acelerando a cada loop
    pos_y += vel_y * delta_time #Atualizando a posicao

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)
    if collider_jogador.collidelist(colliders_mapa) != -1:
           pos_y = old_pos_y
           vel_y = 0
           no_chao = True

    screen.fill((152,209,250))
    pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, 64, 64))
    pygame.draw.rect(screen, (0, 0, 255), collider_jogador, 2)
    

    for i in range(len(mapa_joguinho)):
        for j in range(len(mapa_joguinho[i])):
            letra = mapa_joguinho[i][j]
            if letra in tiles_mapa:
                tile_coordenada = tiles_mapa[mapa_joguinho[i][j]]
                screen.blit(tileset, (j*tile_size_joguinho, i*tile_size_joguinho), tile_coordenada)


    pygame.display.update()