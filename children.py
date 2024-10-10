from Address import Address


class Children :
    def __init__(self , name) :
        self.name = name
        self.wish = [ ]
        self.address = Address()


    def add_wish(self , wish) :
        self.wish.append(wish)

    def display_wish(self) :
        for wish in self.wish :
            print( f"Your wish is {wish}" )

#
# child = Children( "test" )
# child.add_wish( "car" )
# child.add_wish( "poppy" )
# child.display_wish( )
