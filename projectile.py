import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 15
        self.player = player
        self.image = pygame.image.load("shot4_5.png")
        self.image = pygame.transform.scale(self.image,(150,75))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 50
        self.rect.y = player.rect.y + 25

    def remove(self):
        """
        quand cette fonction est appelee suprime l'element contenu dans
        all_projectiles
        """
        self.player.all_projectiles.remove(self)

    def move(self):
        """
        bouge le sprite de ca position de depart vers la droite
        quand le sprite sors de l'ecran ou touche un autre sprite on fait appele
        a la fonction remove
        """
        self.rect.x += self.velocity

        for Ennemy in self.player.game.check_collision(self, self.player.game.all_ennemy):
            self.remove()
            Ennemy.damage(self.player.attack)


        if self.rect.x > 1080:
            self.remove()
