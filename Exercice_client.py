import random
import pygame
from Button import Button
from children import Children
from city_dictionnary import random_name

children_list = []
order_of_delivery = []

def create_children_and_add_to_list(name):  # créée une instance d'enfant avec le nom en paramètre, et l'ajoute à la liste d'enfants
    children_list.append(Children(name))

def add_to_delivery_list(
        distance):  #### renvoie une liste de tous les enfants qui sont à la distance donnée en paramètre
    temporary_list = []
    for child in children_list:
        if child.address.distance_from_north_pole == distance:
            temporary_list = temporary_list + [child]
    return temporary_list

for name in range(50):  ### créé 50 enfant avec des noms aléatoires
    create_children_and_add_to_list(random.choice(random_name))

for distance in range(1, len(children_list) + 1):  ##trie la liste des enfants par ordre de distance
    temp_list = add_to_delivery_list(distance)
    order_of_delivery = order_of_delivery + temp_list

##############################################################################

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("christmas1.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Père Noël Simulator")

font = pygame.font.Font(None, 64)

screen.fill((255,0,0))

running = True
while running:
    position = pygame.mouse.get_pos()
    clicked = False

    pygame.draw.rect(screen, (145,145,145), (0, 0, 1920, 128))
    pygame.draw.rect(screen, (200, 200, 200), (550, 0, 1920, 128))
    screen.blit(font.render("L'Atelier du Père Noël", True, (255,255,255)), (42, 40))
    ## ajouter girlande

    if position[0] >= 1870 and position[1] <= 50:
        pygame.draw.rect(screen, (255,0,0), (1870, 0, 50, 50))
    else:
        pygame.draw.rect(screen, (128,128,128), (1870, 0, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

        if event.type == pygame.KEYDOWN:
            print ("quelqu'un a appuyé sur une touche")

        if event.type == pygame.QUIT or (clicked and position[0] >= 1870 and position[1] <= 50):
            running = False


    pygame.display.flip()
    clock.tick(60)
