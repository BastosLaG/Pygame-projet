import pygame
import random

class Ennemy1(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.PV = 100
        self.max_PV = 100
        self.attaque = 5
        self.velocity = 5
        self.image = pygame.image.load("Ship1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0,300)
        self.rect.y = random.randint(50,650)

    def damage(self, amount):
        """
        Precondition: une cible - class object
                      un montant - int
        inflige un montant de degat a une cible et si les points de vie de la
        cible son inferieur au point de degat infliger alors les Pv de l'ennemy
        se remette au maximum et il réapparait aleatoirement a droite de l'image

        postcondition: Les point de vie - int
                       La fonction game_over
        """
        self.PV -= amount

        if self.PV <= 0:
            self.rect.x = 1080
            self.PV = self.max_PV
            self.rect.y = random.randint(50,650)

    def update_health_bar(self,surface):
        """
        precondition: surface
                      position du sprite en x et y
        Place la bar de point de vie au dessus du sprite associer
        """
        pygame.draw.rect(surface, (120, 120, 120), [self.rect.x, self.rect.y -2, self.max_PV, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y, self.PV, 5])


    def forward(self):
        """
        precondition: sprite
        Permet au sprite de se deplacer vers l'avant si et seulement si il n'est pas en collision avec le joueur sinon il lui inflige des dégats
        """
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attaque)

        if self.rect.x <= 0:
            self.rect.x -= self.velocity
            self.game.player.damage(30)
            self.PV -= self.PV
            if self.PV <= 0:
                self.rect.x = 1080
                self.PV = self.max_PV
                self.rect.y = random.randint(50,650)