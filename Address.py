import random
from city_dictionnary import city_dictionnary,street_list

class Address:
    def __init__(self):
        self.street_name = random.choice(street_list)
        self.city,self.distance_from_north_pole = random.choice(list(city_dictionnary.items()))
