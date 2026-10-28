import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

hero_img = pygame.image.load("assets/Hero_Walk_01.png")

mega_anim_time = 0
mega_curr_frame = 0
megaman_spritesheet = pygame.image.load("megaman_spritesheet.png")

hero_anim_time = 0
hero_curr_frame = 0
hero_walk_list = []
for i in range(4):
    hero_walk_list.append(pygame.image.load(f"assets/Hero_Walk_0{i+1}.png"))

hero_3_time = 0
hero_3_curr_frame = 0
hero_3_ativo = False

pos_x = 0 #variaval de posicao para mover no eixo x
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not hero_3_ativo:
                    hero_3_ativo = True
                    hero_3_curr_frame = 0
                    hero_3_time = 0


    clock.tick(60) #chumbando 60 fps
    dt = clock.get_time() #delta time -> diferença de tempo de um frame e outro. Matematicamente  dt = 1/fps (60).
    
    keys = pygame.key.get_pressed()

    # ========================
    # DESENHOS 
    # ========================
    screen.fill((255,255,255)) #Fundo branco
    
    ### 1. ANIMAÇÃO CONSTANTE:
    mega_anim_time += dt
    if mega_anim_time / 1000 > 0.2:  # troca de frame a cada 0.15s
        mega_curr_frame = (mega_curr_frame + 1) % 10
        mega_anim_time = 0

    screen.blit(megaman_spritesheet, (200, 200), (60*(mega_curr_frame%5), 60*(mega_curr_frame//5), 60, 60))

    ### 2. ANIMAÇÃO PRESSIONANDO TECLA D:
    if keys[pygame.K_d]:
        pos_x = pos_x + 0.1*dt
        hero_anim_time = hero_anim_time + dt # temporizador, acumulando o dt.
        hero_anim_time_sec = hero_anim_time/1000 # converte de milisegundo para segundos
        
        if hero_anim_time_sec > 0.2: #dentro do delta time do meu fps, eu verifico qdo o tempo for maior que 0.2 ms para trocar de frame. Ou seja o frame troca dentro da diferença de tempo do fps. 
            hero_curr_frame = hero_curr_frame + 1
            if hero_curr_frame > 3: # para n deixar o quebrar indice da lista
                hero_curr_frame = 0 #se passar do indice, volta pro zero
            hero_anim_time = 0

    screen.blit(hero_walk_list[hero_curr_frame], (pos_x, 0))

    ### 3. ANIMAÇÃO APERTANDO ESPAÇO:
    if hero_3_ativo:
        hero_3_time = hero_3_time + dt
        if hero_3_time / 1000 > 0.2:
            hero_3_curr_frame += 1
            hero_3_time = 0
            if hero_3_curr_frame >= len(hero_walk_list):
                hero_3_ativo = False
                hero_3_curr_frame = 0

    if hero_3_ativo:
        screen.blit(hero_walk_list[hero_3_curr_frame], (400, 200))
    else:
        screen.blit(hero_walk_list[0], (400, 200))
    

    pygame.display.update()