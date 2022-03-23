import random
from constants import *

from game.shared.point import Point
from game.scripting.action import Action


class ActorUpdates(Action):

    def __init__(self):
        pass

    def execute(self, cast, script):
        self._do_updates(cast)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        ship = cast.get_first_actor("ship")
        ship.move_next()

    def _update_positions(self, ship, actor, position):
        """Draws the actors on the screen.
        Args:
            self (Cast): Instance of Cast.
            robot (Robot): the player robot
            actor (Actor): Instance of actor
            position (Point): Instance of point
        """
        if ship.get_position().bounding_equals(actor.get_position()):
            actor.set_position(position)
            """ self._score += actor.get_value()  """
