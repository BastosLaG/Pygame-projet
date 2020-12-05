import pygame
import math
import time
from game import Game
pygame.init()

#Tailles et nom de la fenetre
pygame.display.set_caption("PiouPiouGame")
screen = pygame.display.set_mode((1080,720))

#imoprtation du fond d'ecran
background = pygame.image.load("bg_star.png")
background = pygame.transform.scale(background, (1120, 720))

#importation du decors
planet = pygame.image.load("parallax-space-big-planet2.png")
planet1 = pygame.image.load("parallax-space-ring-planet.png")
lunePlanet = pygame.image.load("parallax-space-far-planets.png")
poussierePlanet = pygame.image.load("parallax-space-stars2.png")
#importation et positionnement du bouton demarrer plus nom du jeu dans la fenetre
banner = pygame.image.load("PiouPiouGame banner.png")
banner = pygame.transform.scale(banner, (360, 140))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 20)
#----
start = pygame.image.load("PiouPiouGame START.png")
start = pygame.transform.scale(start, (300, 100))
start_rect = start.get_rect()
start_rect.x = math.ceil(screen.get_width() / 10)
start_rect.y = 75

#importation de la musique
main_song = pygame.mixer.Sound("Flux-Gemini-Andromeda.ogg")
#lecture de la musique
main_song.play(1,0,7000)

#condition a l'ouverture du jeu
game = Game()
running = True

#condition tant que le jeu est ouvert
while running:

    #positionement du decors
    screen.blit(background,(-25,0))
    screen.blit(poussierePlanet,(500,150))
    screen.blit(planet,(425,300))
    screen.blit(planet1,(60,100))
    screen.blit(lunePlanet,(700,150))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        screen.blit(start, start_rect)
        #screen.blit(option, option_rect)

    pygame.display.flip()

    #evenement possible
    for event in pygame.event.get():
        #option quitter
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #mappage des touches
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                game.start()

