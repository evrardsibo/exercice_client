import pygame
import random
from city_dictionnary import random_name

from children import Children

children_list=[]
order_of_delivery=[]

def create_children_and_add_to_list(name):
    children_list.append(Children(name))

def add_to_delivery_list(distance):
    temporary_list = []
    for child in children_list:
        if child.address.distance_from_north_pole == distance:
            temporary_list = temporary_list +[child]
    return temporary_list

for name in range(50): ### créé 50 enfant avec des noms aléatoires
    create_children_and_add_to_list(random.choice(random_name))

for distance in range(1,51):  ##trie la liste des enfants par ordre de distance
    temp_list = add_to_delivery_list(distance)
    order_of_delivery = order_of_delivery + temp_list



# pygame.init()
#
# screen = pygame.display.set_mode((1920, 1080))
#
# screen.fill((128,0,128))
#
#
# running = True
# while running:
#     pygame.display.flip()




print (len(children_list))

print (children_list[0].address.distance_from_north_pole)
print (children_list[1].name)

print (len(order_of_delivery))

for child in order_of_delivery:
    print (child.name)



