import pygame
 
 # definir la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):
     
     # definir le constructeur de cette classe
     def __init__(self, player):
         super().__init__()
         self.velocity = 25
         self.player = player
         self.image = pygame.image.load('assets/munition_jeu.png')
         self.image = pygame.transform.scale(self.image, (50, 50))
         self.rect = self.image.get_rect()
         self.rect.x = player.rect.x + 70
         self.rect.y = player.rect.y + 25

     def remove(self):
        self.player.all_projectiles.remove(self)

     def move(self):
        self.rect.x += self.velocity
        
        # verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger des dégats
            monster.damage(1)

        # verifier si notre projectile n'est plus présent sur l'ecran
        if self.rect.x > 1280 :
            # supprimer le projectile ( en dehors de l'ecran )
            self.remove()
            print("Projectile supprimé !")
