import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre du jeu
fenetre = pygame.display.set_mode((800, 600))

# Définir le titre de la fenêtre du jeu
pygame.display.set_caption("Jeu de cercle aléatoire")

# Définir la couleur de fond de la fenêtre
couleur_fond = (255, 255, 255)

# Définir la couleur du cercle
couleur_cercle = (255, 0, 0)

# Définir le rayon du cercle
rayon_cercle = 25

# Définir la position initiale du cercle
position_cercle = [random.randint(rayon_cercle, 800 - rayon_cercle), 
                   random.randint(rayon_cercle, 600 - rayon_cercle)]

# Définir une fonction pour dessiner le cercle à sa position actuelle
def dessiner_cercle():
    pygame.draw.circle(fenetre, couleur_cercle, position_cercle, rayon_cercle)

# Boucle principale du jeu
while True:
    # Traiter les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            position_souris = pygame.mouse.get_pos()
            # Vérifier si la position de la souris est dans le cercle
            if ((position_souris[0] - position_cercle[0]) ** 2 + 
                (position_souris[1] - position_cercle[1]) ** 2 <= rayon_cercle ** 2):
                # Définir une nouvelle position aléatoire pour le cercle
                position_cercle = [random.randint(rayon_cercle, 800 - rayon_cercle), 
                                   random.randint(rayon_cercle, 600 - rayon_cercle)]

    # Effacer l'écran
    fenetre.fill(couleur_fond)

    # Dessiner le cercle
    dessiner_cercle()

    # Mettre à jour l'affichage
    pygame.display.update()