from Address import Address


class Children :
    def __init__(self , name) :
        self.name = name
        self.wish = [ ]
        self.address = Address()
        self.statut = False


    def add_wish(self , wish) :
        self.wish.append(wish)

    def display_wish(self) :
        for wish in self.wish :
            print( f"Your wish is {wish}" )

    def check_delivery(self , statut) :
        if self.statut != statut :
            print( f"gift delivered !" )
        else :
            print( f"gift not delivered !" )
