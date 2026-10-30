import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
# tile_size = 60
tile_size_joguinho = 64
tileset = pygame.image.load("atividade_12_mapas_bonitenhos/tileset.png")
bg = pygame.image.load("atividade_12_mapas_bonitenhos/bg.jpg")
player_spritesheet = pygame.image.load("atividade_12_mapas_bonitenhos/player.png").convert_alpha()
player_spritesheet = pygame.transform.scale(player_spritesheet, (512, 128))
player_anim_time = 0
player_curr_frame = 0
olhando_esquerda = False
andando = False



pos_x = 128
pos_y = 0

vel_y = 0
gravidade = 0.001
no_chao = False

mapa_joguinho = [
  "BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB",
  "BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB", 
  "BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB", 
  "BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXCCXXXXXXXXXB", 
  "BXXXXXXXXXXXXXXXXXXBBXXXXXXXXXXCCCCXXXXXXXXB", 
  "BXXXXBXXXXXXXXXXXXBBBBXXXXXXXXCCCCCCXXXXXXXB", 
  "BXXXXBBXXXXCCXXXXBBBBBBXXCCXXCCCCCCCCXXBBXXB", 
  "BGGGGGGGAADDDDDDDGGGGGGGAADDDDDDDDDDDGGGGGBB", 
  "BTTTTTTTPPUUUUUUUTTTTTTTPPUUUUUUUUUUUTTTTTTB", 
  "BTTTTTTTZZUUUUUUUTTTTTTTZZUUUUUUUUUUUTTTTTTB",
]


tiles_mapa = {
    #JUSTIFICATIVA TECNICA: MAPEIA A COORDENADA DE CADA TILE PARA EVITAR IFS NO SCREEN.BLIT()
    "G": (0, 64, tile_size_joguinho, tile_size_joguinho),
    "U": (64, 0, tile_size_joguinho, tile_size_joguinho),
    "D": (0, 0, tile_size_joguinho, tile_size_joguinho),
    "T": (64, 64, tile_size_joguinho, tile_size_joguinho),
    "B": (0, 128, tile_size_joguinho, tile_size_joguinho),
    "C": (64, 128, tile_size_joguinho, tile_size_joguinho),
    "P": (128, 0, tile_size_joguinho, tile_size_joguinho),
    "Z": (128, 64, tile_size_joguinho, tile_size_joguinho),
}

colisores = ["G","B", "C", "D"] #Lista de blocos que colidem com o jogador.
colliders_mapa = [] 
#JUSTIFICATIVA TECNICA: A ideia é ter um array de blocos colisores para utilizar colliderlist. Dado uma lista de colisores, retorna o objeto rect que o jogador colidiu. Muito mais eficiente!!!
for i in range(len(mapa_joguinho)):
    for j in range(len(mapa_joguinho[i])):
        if mapa_joguinho[i][j] in colisores:
            collider_rect = pygame.Rect(j * tile_size_joguinho, i * tile_size_joguinho, 64, 64) #Cria o colisor
            if collider_rect not in colliders_mapa: #Evita colisor duplicado
                colliders_mapa.append(collider_rect)
print(colliders_mapa)

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
        andando = True
        olhando_esquerda = False
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - 0.2*delta_time
        andando = True
        olhando_esquerda = True
    else:
        andando = False


    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)
    if collider_jogador.collidelist(colliders_mapa) != -1:
        pos_x = old_pos_x

    # ==================================
    #       MOVIMENTAÇÃO EIXO Y
    # ==================================
    old_pos_y = pos_y

    if keys[pygame.K_SPACE] and no_chao:
            vel_y = -0.60 #valores negativos aqui sobem no eixo y (esquisito!!)
            no_chao = False
            
    # ==================================
    #             GRAVIDADE
    # ==================================
    vel_y = vel_y + gravidade * delta_time #Acelerando a cada loop (valores positivos descem no eixo y)
    pos_y += vel_y * delta_time #posicao y sempre em relação a velocidade.


    # ==================================
    #         ANIMAÇÃO PLAYER
    # ==================================
    if andando:
        
        total_frames = 8
        linha_sprite = 1
    else:
        total_frames = 5
        linha_sprite = 0

    player_curr_frame = player_curr_frame % total_frames

    player_anim_time = player_anim_time + delta_time
    if player_anim_time / 1000 > 0.12:
        player_curr_frame = (player_curr_frame + 1) % total_frames
        player_anim_time = 0

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)
    if collider_jogador.collidelist(colliders_mapa) != -1:
           pos_y = old_pos_y
           vel_y = 0
           no_chao = True


    # ==================================
    #             CAMERA
    # ==================================
    camera_x = pos_x - 400
    
    # ==================================
    #             DESENHOS
    # ==================================
    screen.blit(bg, (0, 0))
    # pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, 64, 64)) #Personagem
    # pygame.draw.rect(screen, (0, 0, 255), collider_jogador, 2) # Visualização do collider

    area_player = (player_curr_frame * 64, linha_sprite * 64, 64, 64)
    frame_atual = player_spritesheet.subsurface(area_player)

    if olhando_esquerda:
        frame_atual = pygame.transform.flip(frame_atual, True, False)

    screen.blit(frame_atual, (pos_x-camera_x, pos_y)) #Desenha o player
    

    for i in range(len(mapa_joguinho)): #Desenho do mapa
        for j in range(len(mapa_joguinho[i])):
            letra = mapa_joguinho[i][j]
            if letra in tiles_mapa:
                tile_coordenada = tiles_mapa[mapa_joguinho[i][j]]
                screen.blit(tileset, (j*tile_size_joguinho-camera_x, i*tile_size_joguinho), tile_coordenada)


    pygame.display.update()