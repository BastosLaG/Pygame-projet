import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.PV = 100
        self.max_PV = 100
        self.attack = 25
        self.velocity = 20
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("Ship2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 270

    def damage(self, amount):
        """
        Precondition: une cible - class object
                      un montant - int
        inflige un montant de degat a une cible et si les points de vie de la
        cible son inferieur au point de degat infliger alors lancer la fonction
        game_over

        postcondition: Les point de vie - int
                       La fonction game_over
        """
        if self.PV - amount > amount:
            self.PV -= amount
        else:
            self.game.game_over()


    def update_health_bar(self,surface):
        """
        precondition: surface
                      position du sprite en x et y
        Place la bar de point de vie au dessus du sprite associer
        """
        pygame.draw.rect(surface, (120, 120, 120), [self.rect.x + 15, self.rect.y + 25, self.max_PV, 9])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y + 27, self.PV, 6])

    def launch_projectile(self):
        """
        precondition: all_projectiles
                      acces au dossier projectiles
        permet de cree un projectile
        """
        self.all_projectiles.add(Projectile(self))


    def move_haut(self):
        """
        precondition: on doit savoir si une touche est presser
                      on doit savoir si le joueur est en contacte avec un ennemy
        deplace le joueur vers le haut
        """
        if not self.game.check_collision(self, self.game.all_ennemy):
            self.rect.y -= self.velocity

    def move_bas(self):
        """
        precondition: on doit savoir si une touche est presser
                      on doit savoir si le joueur est en contacte avec un ennemy
        deplace le joueur vers le bas
        """
        if not self.game.check_collision(self, self.game.all_ennemy):
            self.rect.y += self.velocity

