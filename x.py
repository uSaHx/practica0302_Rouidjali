import pygame
from random import randint
from ladrillo import Brick

# Setup del juego
pygame.init()
ventana = pygame.display.set_mode((720, 1020))
pygame.display.set_caption("Juego Oussama y Asier")

# Fondo de pantalla
fondo = pygame.image.load("campo.jpg")
fondo = pygame.transform.scale(fondo, (720, 1020))

# Bases del ladrillo
brik1 = Brick(40, 400, "messi.png")

# Bases de la pelota
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
speed = [randint(2,5),randint(2,5)]
ballrect.move_ip(0,0)

# Bases de la barra
barra = pygame.image.load("botas.png")
barra = pygame.transform.scale(barra, (100, 50))
barrarect = barra.get_rect()
barrarect.move_ip(240,900)
fuente = pygame.font.Font(None, 36)

# Base fin de juego
texto = pygame.image.load("over.png")
texto_rect = texto.get_rect()
texto_x = ventana.get_width() / 2 - texto_rect.width / 2
texto_y = ventana.get_height() / 2 - texto_rect.height / 2

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

    # Velocidad al colisionar con la barra
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]
        if speed[0] < 20 and speed[1] < 20:
            speed[0] += 1
            if speed[1] < 0:
                speed[1] -= 1
            else:
                speed[1] += 1

    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    # Colision con Rocas
    if ballrect.colliderect(brik1.rect):
        speed[1] = -speed[1]
    # Limites Laterales
    if barrarect.right > 724:
        barrarect.right = 723
    if barrarect.left < 0:
        barrarect.left = 1

    ventana.blit(fondo, (0,0))
    ventana.blit(brik1.image, brik1.rect)
    ventana.blit(ball, ballrect)
    ventana.blit(barra, barrarect)

    # Pantalla de derrota
    if ballrect.bottom > 1000:
        ventana.blit(texto, texto_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(120)

pygame.quit()
