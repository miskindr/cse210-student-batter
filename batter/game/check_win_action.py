import sys
from game.action import Action

class CheckWinAction(Action):
    """A code template for handling a wins. The responsibility 
        of this class of objects is to update the game state when all bricks are gone.
        
        Stereotype:
            Controller
        """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if len(cast["brick"]) == 0:
            print("You Win")
            sys.exit()