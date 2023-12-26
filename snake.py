import pygame
import time
import random

pygame.init()

# Définir les couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Définir la taille de la fenêtre
largeur, hauteur = 600, 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake Game")

# Définir les paramètres du serpent
taille_serpent = 15
vitesse_serpent = 10

# Définir les paramètres de la pomme
taille_pomme = 15

# Définir la police
police = pygame.font.SysFont(None, 30)

# Créer une instance de pygame.time.Clock
horloge = pygame.time.Clock()

# Fonction principale du jeu
def jeu():
    serpent = [(largeur // 2, hauteur // 2)]
    direction = (0, 0)
    pomme = generer_pomme(serpent)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -taille_serpent)
                elif event.key == pygame.K_DOWN:
                    direction = (0, taille_serpent)
                elif event.key == pygame.K_LEFT:
                    direction = (-taille_serpent, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (taille_serpent, 0)

        serpent[0] = (serpent[0][0] + direction[0], serpent[0][1] + direction[1])

        # Vérifier si le serpent a mangé la pomme
        if pygame.Rect(serpent[0], (taille_serpent, taille_serpent)).colliderect(pygame.Rect(pomme, (taille_pomme, taille_pomme))):

            serpent.append((0, 0))
            pomme = generer_pomme(serpent)
            score += 1

        fenetre.fill(blanc)

        # Dessiner le serpent
        for segment in serpent:
            pygame.draw.rect(fenetre, noir, [segment[0], segment[1], taille_serpent, taille_serpent])

        # Dessiner la pomme
        pygame.draw.rect(fenetre, rouge, [pomme[0], pomme[1], taille_pomme, taille_pomme])

        # Afficher le score
        afficher_infos("Score: " + str(score), 10, 10)

        pygame.display.update()

        # Utiliser l'horloge pour réguler la vitesse du serpent
        horloge.tick(vitesse_serpent)

# Fonction pour générer une nouvelle position pour la pomme
def generer_pomme(serpent):
    while True:
        x = random.randrange(0, largeur - taille_pomme, taille_pomme)
        y = random.randrange(0, hauteur - taille_pomme, taille_pomme)

        # Vérifier que la pomme ne se trouve pas sur le serpent
        if (x, y) not in serpent:
            return x, y

# Fonction pour afficher des informations
def afficher_infos(texte, x, y):
    texte_surface = police.render(texte, True, noir)
    fenetre.blit(texte_surface, (x, y))

# Lancer le jeu
jeu()
