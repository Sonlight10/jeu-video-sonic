import pygame
import random
import animation

# créer une classe qui va gérer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('gamma')
        self.game = game
        self.health = 1
        self.max_health = 1
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0,300)
        self.rect.y = 570
        self.velocity = 1
        self.start_animation()
        
    def damage(self, amount):
        # Infliger des dégâts
        self.health -= amount
        # Verifier si son nouveau nombre de points de vie est inférieur ou égal à 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1080 + random.randint(0, 300)

    def update_animation(self):
        self.animate(loop=True)

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # Infliger des degats (au joueur)
            self.game.player.damage(self.attack) 

