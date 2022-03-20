import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):

    """
    An input action that controls the cycle.

    The responsibility of ControlActorsAction is to get a direction and turn\
    a cycle to move in that direction depending on the key a player presses.

    Attributes:
    ---
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _direction (Point): The direction assigned to cycle_one. 
        _cycle_two_direction (Point): The direction assigned to cycle_two.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
        ---
            keyboard_service (KeyboardService): An instance of KeyboardService.

        """
        self._keyboard_service = keyboard_service
        self._direction = Point(-constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Cycle one keyboard Inputs

        ship = cast.get_first_actor("ship")

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            ship.move_next()

        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            ship.move_next()

        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            ship.move_next()

        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            ship.move_next()