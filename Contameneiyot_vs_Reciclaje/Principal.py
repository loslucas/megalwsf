import pygame
import Constantes

pygame.init()

size = [Constantes.ANCHO_PANTALLA, Constantes.ALTURA_PANTALLA]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Contamineitor vs Reciclaje")

lista_sprites_activos  = pygame.sprite.Group()
lista_sprites_enemigos = pygame.sprite.Group()
Lista_sprite_objetos = pygame.sprite.Group()

#Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
salir = False
clock = pygame.time.Clock()

# -------- Loop Princiapl -----------
while not salir:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            salir = True 

        """if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_principal.retroceder()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.avanzar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.bajar()
            if evento.key == pygame.K_UP:
                jugador_principal.subir()

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugador_principal.parar()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.parar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.parar()
            if evento.key == pygame.K_UP:
                jugador_principal.parar()"""
                
    screen.fill(Constantes.AZUL)
    lista_sprites_activos.update()
    
    lista_sprites_activos.draw(screen)   
    
    
    clock.tick(60)

    pygame.display.flip()

pygame.quit()



