import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

dog_img = pygame.image.load("chiens-funnyanimals.gif")

hero_img = pygame.image.load("assets/Hero_Walk_01.png")

megamen_spritesheet = pygame.image.load("megaman_spritesheet.png")

hero_anim_time = 0
hero_curr_frame = 0
hero_walk_list = [
    pygame.image.load("assets/Hero_Walk_01.png"),
    pygame.image.load("assets/Hero_Walk_02.png"),
    pygame.image.load("assets/Hero_Walk_03.png"),
    pygame.image.load("assets/Hero_Walk_04.png"),
]
pos_x = 0 #variaval de posicao para mover no eixo x


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            ...


    clock.tick(60) #chumbando 60 fps
    dt = clock.get_time() #delta time -> diferença de tempo de um frame e outro. Matematicamente  dt = 1/fps (60).
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pos_x = pos_x + 0.1*dt
        hero_anim_time = hero_anim_time + dt # temporizador, acumulando o dt.
        hero_anim_time_sec = hero_anim_time/1000 # converte de milisegundo para segundos
        
        if hero_anim_time_sec > 0.2: #dentro do delta time do meu fps, eu verifico qdo o tempo for maior que 0.2 ms para trocar de frame. Ou seja o frame troca dentro da diferença de tempo do fps. 
            hero_curr_frame = hero_curr_frame + 1
            if hero_curr_frame > 9: # para n deixar o quebrar indice da lista
                hero_curr_frame = 0 #se passar do indice, volta pro zero
            hero_anim_time = 0

    # Desenho dos elementos na tela
    screen.fill((255,255,255))

    if hero_curr_frame < 5:
        screen.blit(megamen_spritesheet, (pos_x, 200), (60 * hero_curr_frame, 0, 60, 60))
    else:
        screen.blit(megamen_spritesheet, (pos_x, 200), (60 * (hero_curr_frame - 5), 60, 60, 60))




    # screen.blit(dog_img, (0, 0))
    # screen.blit(hero_walk_list[hero_curr_frame], (pos_x, 0))

    pygame.display.update()