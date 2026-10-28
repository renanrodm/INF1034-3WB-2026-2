import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
tile_size = 60
tile_size_joguinho = 64
collider_caixa = pygame.Rect(0, 0, 0, 0)
can_walk = True

pos_x = 0
pos_y = 0

mapa_joguinho = [
  "GGGGGGAGGGGGGG",
  "GGGGGGAGGGGGGG",
  "GGGGGGAGGGGGGG",
  "GGGGGGAGGGGGGG",
  "GGGGGGAAAGGGGG",
  "GGGGGGGGAGGGGG",
  "GGGGGGGGAGGGGG",
  "PPPPPPPPAPPPPP",
  "AAAAAAAAAAAAAA",
  "AAAAAAAAAAAAAA",
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    dt = clock.get_time()

    ##Primeiro mapa
    for i in range(len(mapa_joguinho)): #Para cada linha (contraintuitivamente, anda sobre o eixo y)
        linha_str = mapa_joguinho[i]
        for j in range(len(linha_str)): # Para cada coluna (contraintuitivamente, anda sobre o eixo x)
            if mapa_joguinho[i][j] == "G":
                pygame.draw.rect(screen, (39,153,0), (tile_size*j, tile_size*i, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), (tile_size*j, tile_size*i, 60, 60), 1)
            elif mapa_joguinho[i][j] == "A":
                pygame.draw.rect(screen, (63,125,232), (tile_size*j, tile_size*i, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), (tile_size*j, tile_size*i, 60, 60), 1)
            elif mapa_joguinho[i][j] == "P":
                pygame.draw.rect(screen, (230,235,134), (tile_size*j, tile_size*i, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), (tile_size*j, tile_size*i, 60, 60), 1)



    pygame.display.update()