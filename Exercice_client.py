import random
import pygame

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

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Père Noël Simulator")

screen.fill((255,0,0))

running = True
while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(60)

