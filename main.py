import pygame
from game import Game
import math
from camera import Camera
from camera import Follow
from player import Player

pygame.init()

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
DISPLAY_W, DISPLAY_H = 1280, 720
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))  # Fix double set_mode
house = pygame.image.load('assets/sonic_1__green_hill__present__background_by_mtbvcdremixes_df1j81j-fullview.png').convert()

# Charger l'icône
icon_img = pygame.image.load('assets/logo.png')
pygame.display.set_icon(icon_img)

# Charger la musique de fond du menu
pygame.mixer.music.load('sonic_audio_title.wav')  # Remplace par le fichier de musique du menu
pygame.mixer.music.play(-1)  # Joue la musique en boucle

# Générer la fenêtre du jeu
pygame.display.set_caption("S0NIC THE HEDGEHOG")

# Charger l'image de l'arrière-plan du jeu
background = pygame.image.load('assets/sonic_1__green_hill__present__background_by_mtbvcdremixes_df1j81j-fullview.png')

# Charger l'image du sol
ground = pygame.image.load('assets/sol.png')
ground_rect = ground.get_rect()
ground_rect.y = window.get_height() - ground_rect.height + 34

# Importer notre bannière
banner = pygame.image.load('assets/sonic_ring.png')
banner_rect = banner.get_rect()
banner_rect.y = math.ceil(window.get_width() / 8)
banner_rect.x = math.ceil(window.get_width() / 4.7)

# Importer et charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/start button.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(window.get_width() / 2.7)
play_button_rect.y = math.ceil(window.get_height() / 1.4)

FPS = 60  # Frames par seconde
clock = pygame.time.Clock()  # Implémentation d'une horloge interne au jeu (notion de temps)

# Charger le jeu
game = Game()

################################# LOAD PLAYER AND CAMERA ###################################
sonic = Player(game)
camera = Camera(sonic)
follow = Follow(camera, sonic)

running = True  # Exécution du jeu débute

# Boucle principale du jeu
while running:
    # Effacer l'écran à chaque itération (remplir avec l'arrière-plan)
    window.blit(background, (0, 0))

    # Vérifier les actions du joueur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # Gérer les entrées au clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if game.is_playing:
                if event.key == pygame.K_SPACE:
                    game.player.jump()  # Faire sauter le joueur
                if event.key == pygame.K_k:
                    game.player.launch_projectile()  # Lancer un projectile

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  # Désactiver la touche

        # Détecter si la souris clique sur le bouton "Jouer"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos) and not game.is_playing:
                game.start()  # Lancer le jeu
                pygame.mixer.music.stop()  # Arrêter la musique du menu
                pygame.mixer.music.load('green-hill-zone.wav')  # Charger la musique du jeu
                pygame.mixer.music.play(-1)  # Jouer la musique du jeu en boucle

    # Si le jeu a commencé
    if game.is_playing:
        # Déclencher la logique du jeu
        game.player.gravity_jump()
        # Afficher le sol
        window.blit(ground, ground_rect)

        # Afficher les éléments du jeu avec la caméra
        canvas.blit(house, (0 - camera.offset.x, 0 - camera.offset.y))
        canvas.blit(sonic, (sonic.rect.x - camera.offset.x, sonic.rect.y - camera.offset.y))
        window.blit(canvas, (0, 0))
        pygame.display.update()

    # Si le jeu n'a pas encore commencé (menu)
    else:
        # Afficher les éléments du menu
        window.blit(banner, banner_rect)
        window.blit(play_button, play_button_rect)

    pygame.display.flip()
    
    # Contrôler le FPS du jeu
    clock.tick(FPS)

pygame.quit()
