class Children :
    def __init__(self , name) :
        self.name = name
        self.wich = [ ]
        self.adress = True

    def add_wich(self , wish) :
        self.wich.append(wish)

    def display_wish(self) :
        for wish in self.wich :
            print( f"Your wish is {wish}" )


child = Children( "test" )
child.add_wich( "car" )
child.add_wich( "poppy" )
child.display_wish( )
