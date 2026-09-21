import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock() # 
nuvem_x = 480
nuvem_y = 150


fonte = pygame.font.Font("batmfa__.ttf", 50)
image = pygame.image.load("batman.png")
image = pygame.transform.scale(image, (200, 200))
pygame.mixer.music.load("batman_1966.mp3")
pygame.mixer.music.play(-1)



while running:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ## AÇÕES INSTANTANEAS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                #TODO: roda o sfx
                ...
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #TODO: RODA O SFX
                ...



    ## Seção para realizar movimentações e simulações físicas
    dt = clock.get_time()/1000
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] == True:
        nuvem_x = nuvem_x + 100 * dt
    elif keys[pygame.K_LEFT]:
        nuvem_x = nuvem_x - 100 * dt
    elif keys[pygame.K_UP]:
        nuvem_y = nuvem_y - 100 * dt
    elif keys[pygame.K_DOWN]:
        nuvem_y = nuvem_y + 100 * dt
    

    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)

    

    #Seção para desenhar os elementos na tela
    screen.fill("#97D1FA")
    pygame.draw.rect(screen, "#0D1664", (100, 200, 200, 50))
    pygame.draw.circle(screen, "#FFF251", (mouse_x, mouse_y), 50)
    pygame.draw.polygon(screen, "#F2883B", [(400, 300), (450, 300), (425, 250)])
    pygame.draw.line(screen, "#FFF251", (10, 150), (100, 20), 4)
    pygame.draw.circle(screen, "#FFFFFF", (nuvem_x, nuvem_y), 50)

    screen.blit(image, (500, 300))

    steve_text = fonte.render("I am BATMAN!", True, "#000000")
    screen.blit(steve_text, (500, 250))

    pygame.display.update()