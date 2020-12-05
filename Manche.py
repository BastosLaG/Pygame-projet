import pygame

class MancheEvent:

    #création d'un compteur
    def __init__(self):
        self.nbr_manche = 1
        self.percent = 0
        self.percent_speed = 50

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def indicateur_de_manche(self):
        if self.is_full_loaded():
            self.reset_percent()
            self.nbr_manche += 1
            print("Début de la manche",self.nbr_manche,"!!!")

    def update_bar(self, surface):
        # ajouter du poucentage
        self.add_percent()
        #appel de la méthode indicateur_de_manche
        self.indicateur_de_manche()
        # cree l'affichage
        pygame.draw.rect(surface, (0), [ 0, 0, surface.get_width(), 10])
        pygame.draw.rect(surface, (187,11,11), [ 0, 0, (surface.get_width() / 100) * self.percent, 8])