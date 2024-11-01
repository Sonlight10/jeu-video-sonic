import pygame
from game import Game
import time
pygame.init()

icon_img = pygame.image.load('assets/logo.png')  # Créer un logo dans la barre des tâches pour notre jeu
pygame.display.set_icon(icon_img)

pygame.mixer.music.load('green-hill-zone.wav')
pygame.mixer.music.play()

# Générer la fenêtre de notre jeu
pygame.display.set_caption("S0NIC THE HEDGEHOG")
screen = pygame.display.set_mode((1280, 720))

# Importer de charger l'arrière-plan de notre jeu
background = pygame.image.load('assets/sonic_1__green_hill__present__background_by_mtbvcdremixes_df1j81j-fullview.jpg')

FPS = 60
clock = pygame.time.Clock()

# Charger notre jeu
game = Game()

running = True

# Boucle tant que cette condition est vraie
while running:

    # Appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, 0))

    # Appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # Récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Récupérer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()

    # Appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # Appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

    # Vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Vérifier si le joueur souhaite sauter
    if game.pressed.get(pygame.K_SPACE):
        game.player.jump()  # Appelle la méthode jump pour faire sauter le joueur

    print(game.player.rect.x)

    # Mettre à jour le joueur (y compris la gestion du saut et de la gravité)
    game.player.gravity_jump()

    clock.tick(FPS)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # Détecter si un joueur enclenche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si la touche 'k' est enclenchée pour lancer notre projectile
            if event.key == pygame.K_k:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
