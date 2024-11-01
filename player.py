import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite):
    
    def __init__(self, game):
        super().__init__('sonic')
        self.health = 1
        self.max_health = 1
        self.attack = 10
        self.velocity = 5
        self.jump_strength = 15  # Force du saut
        self.gravity = 0.5  # Force de gravité
        self.is_jumping = False  # État du saut
        self.vertical_speed = 0  # Vitesse verticale
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 550
        self.game = game

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        # demarrer l'animation du lancer
        self.start_animation()
            
    def move_right(self):
        self.rect.x += self.velocity
        if self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity  # Annuler le mouvement si collision
        
    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        if not self.is_jumping:  # Ne peut sauter que s'il n'est pas déjà en train de sauter
            self.is_jumping = True
            self.vertical_speed = -self.jump_strength  # Applique la force de saut

    def gravity_jump(self):
        # Gérer la gravité
        if self.is_jumping:
            self.vertical_speed += self.gravity  # Ajoute la gravité à la vitesse verticale
            self.rect.y += self.vertical_speed  # Met à jour la position verticale
            
            # Vérifie si le joueur est au sol
            if self.rect.y >= 550:  # Suppose que 550 est la hauteur du sol
                self.rect.y = 550
                self.is_jumping = False
                self.vertical_speed = 0  # Réinitialise la vitesse verticale

    def update_animation(self):
        self.animate()
