import pygame
from player import Player
from Manche import MancheEvent
from Ennemy import Ennemy1

class Game:
    """
    Ma classe Game sert à gérer le nombre de (joueur, ennemy, projectile, input) à chaque début et fin de partie
    On peut actualiser les sprites
    Gerer le spawn des ennemies
    Et les boites de collisions
    """

    def __init__(self):

        # def si le jeu est lancer
        self.is_playing = False

        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'evenement de manche
        self.manche_event = MancheEvent()
        # groupe d'ennemy
        self.all_ennemy = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_Ennemy()

    def game_over(self):

        self.all_ennemy = pygame.sprite.Group()
        self.player.PV = self.player.max_PV
        self.is_playing = False

    def update(self, screen):
        """
        precondition: screen

        permet d'actualiser toute les images present a l'interieur de la
        fonction
        """
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        self.manche_event.update_bar(screen)

        for projectil in self.player.all_projectiles:
            projectil.move()

        for ennemy1 in self.all_ennemy:
            ennemy1.forward()
            ennemy1.update_health_bar(screen)

        self.player.all_projectiles.draw(screen)

        self.all_ennemy.draw(screen)

#-------------- voir comment on fait pour se deplacer beug a regler

        if self.pressed.get(pygame.K_UP)and self.player.rect.y > -20:
            self.player.move_haut()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 620:
            self.player.move_bas()

    def spawn_Ennemy(self):
        ennemy1 = Ennemy1(self)
        self.all_ennemy.add(ennemy1)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)