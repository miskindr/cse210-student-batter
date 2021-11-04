from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast

        if paddle.get_position().get_x() == 2 and direction.get_x() < 0:
            paddle.set_velocity(Point(-1,0))
        elif paddle.get_position().get_x() == 68 and direction.get_x() > 0:
            paddle.set_velocity(Point(1,0))
        elif (paddle.get_position().get_x() == 1 and direction.get_x() < 0) \
            or (paddle.get_position().get_x() == 69 and direction.get_x() > 0):
            paddle.set_velocity(Point(0,0))
        else:
            paddle.set_velocity(direction)
