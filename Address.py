import random
from city_dictionnary import city_dictionnary,street_list

class Address:
    def __init__(self,street_name):
        self.street_name = street_name
        self.city,self.distance_from_north_pole = random.choice(list(city_dictionnary.items()))


test = Address("84 Digue de Cuesmes")

print (test.street_name)
print (test.city)
print (test.distance_from_north_pole)