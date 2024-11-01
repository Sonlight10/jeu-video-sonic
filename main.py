import pygame
from game import Game
import math
import time

pygame.init()

# Charger l'icône
icon_img = pygame.image.load('assets/logo.png')
pygame.display.set_icon(icon_img)

# Charger la musique de fond du menu
pygame.mixer.music.load('sonic_audio_title.wav')  # Remplace par le fichier de musique du menu
pygame.mixer.music.play(-1)  # Joue la musique en boucle

# Générer la fenêtre du jeu
pygame.display.set_caption("S0NIC THE HEDGEHOG")
screen = pygame.display.set_mode((1280, 720))

# Charger l'image de l'arrière-plan du jeu
background = pygame.image.load('assets/sonic_1__green_hill__present__background_by_mtbvcdremixes_df1j81j-fullview.jpg')

# importer notre bannière
banner = pygame.image.load('assets/sonic_ring.png')
banner_rect = banner.get_rect()
banner_rect.y = math.ceil(screen.get_width() / 8)
banner_rect.x = math.ceil(screen.get_width() / 3.5)

# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/start button.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.7)
play_button_rect.y = math.ceil(screen.get_height() / 1.4)

FPS = 60  # Frames par seconde
clock = pygame.time.Clock()  # Implémentation d'une horloge interne au jeu (notion de temps)

# Charger le jeu
game = Game()

running = True  # Exécution du jeu débute

# boucle tant que
while running:

    # appliquer la fenetre du jeu
    screen.blit(background, (0, -1))

    # verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

        # Mettre à jour l'affichage
        pygame.display.flip()

        for event in pygame.event.get():
            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
            # Vérifier si une touche est pressée
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                # detecter si la touche espace est enclenchée pour lancer un projectile
                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()

                # Vérifier si le joueur souhaite sauter
                if game.pressed.get(pygame.K_SPACE):
                    game.player.jump()  # Appelle la méthode jump pour faire sauter le joueur


                # Mettre à jour le joueur (y compris la gestion du saut et de la gravité)
                game.player.gravity_jump()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # verification pour savoir si la souris est en collisiion avec le bouton jouer
                if play_button_rect.collidepoint(event.pos) :
                    # mettre le jeu en mode "lancé"
                    game.start()



        clock.tick(FPS)
