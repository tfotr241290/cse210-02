from optparse import Values
from game.cards import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            
        """
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user ....

        Args:
            
        """
        
       
    def do_updates(self):
        """Updates the player's ....

        Args:
            
        """
        

    def do_outputs(self):
        """Displays ..... Also asks the player ..... 

        Args:
            
        """
        


