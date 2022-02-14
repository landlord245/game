# Here satrt No Humans
from re import S
import pygame
from sys import exit

pygame.init()
ventana = pygame.display.set_mode((800,400))#Hace Aparecer una ventana con altura y anchura
pygame.display.set_caption('No Humans')
fps = pygame.time.Clock()#Objeto de la clase time en pygame

#superficieArriba = pygame.Surface((800,500))#Supereficie dentro de la ventana
#superficieArriba.fill('Blue')#Color del superficie de la ventana
cielo = pygame.image.load('img/sky.png')
suelo = pygame.image.load('img/suelo.png')
suelo.fill((50,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Dibujar todos los elementos
    #Actualizar todo
    ventana.blit(cielo,(0,0))#Posicion de la imagen Sky.png
    ventana.blit(suelo,(0,0))
    pygame.display.update()
    fps.tick(60)#Objeto con el atributo 60 fotos por segundo