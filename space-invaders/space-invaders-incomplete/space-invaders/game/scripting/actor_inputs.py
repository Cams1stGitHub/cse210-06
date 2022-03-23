import random
from game.scripting.action import Action
from game.shared.point import Point
from constants import *


class ActorInputs(Action):
    def __init__(self, keyboard_services):
        self._keyboard_service = keyboard_services

    def execute(self, cast, script):
        self._get_inputs(cast)

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        ship = cast.get_first_actor("ship")
        velocity = self._keyboard_service.get_direction()
        print(ship.get_position().get_x())
        ship.set_velocity(velocity)
