import pygame
from random import randint

# Setup del juego
pygame.init()
ventana = pygame.display.set_mode((720,1020))
pygame.display.set_caption("Juego Oussama y Asier")

# Fondo de pantalla
fondo = pygame.image.load("campo.jpg")
fondo = pygame.transform.scale(fondo, (720, 1020))

# Bases de la pelota
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
speed = [randint(3,7),randint(3,7)]
ballrect.move_ip(0,0)

# Bases de la barra
barra = pygame.image.load("botas.png")
barra = pygame.transform.scale(barra, (100, 50))
barrarect = barra.get_rect()
barrarect.move_ip(240,900)
fuente = pygame.font.Font(None, 36)

# Funciones del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-5,0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(5,0)

    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    # Pantalla de derrota
    if ballrect.bottom > 1000:
        texto = pygame.image.load("over.png")
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    # Limites Laterales
    if barrarect.right > 724:
        barrarect.right = 723
    if barrarect.left < 0:
        barrarect.left = 1
    else:
        ventana.blit(fondo, (0,0))
        ventana.blit(ball, ballrect)
        ventana.blit(barra, barrarect)

    pygame.display.flip()
    pygame.time.Clock().tick(120)

pygame.quit()
