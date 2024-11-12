from player import Player
from monster import Monster
import pygame

# creer une seconde classe qui va representer notre jeu
class Game:
    
    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        # Position initiale du joueur
        self.x_initial = 0  # Remplacez par la position initiale souhaitée
        self.y_initial = 550  # Remplacez par la position initiale souhaitée
        self.reset_player_position()
        
    def reset_player_position(self):
        self.player.rect.x = self.x_initial
        self.player.rect.y = self.y_initial

    def start(self):
        self.is_playing = True
        self.reset_player_position()  # Réinitialiser la position du joueur
        self.spawn_monster()
        self.spawn_monster()
      

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 1 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False  # Jeu terminé
        self.reset_player_position()  # Réinitialiser la position du joueur
        pygame.mixer.music.stop()
        # Charger la musique de fond du menu
        pygame.mixer.music.load('sonic_audio_title.wav')  # Remplace par le fichier de musique du menu
        pygame.mixer.music.play(-1)  # Joue la musique en boucle
        print('Game Over')

    def update(self, screen):
        # Appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)
        # actualiser l'animation du joueur
        self.player.update_animation()
        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        # Récupérer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_animation()
        # Appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)
        # Appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)
        # Vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, groupe):
        return pygame.sprite.spritecollide(sprite, groupe, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)


