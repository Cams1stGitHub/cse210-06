import random
from constants import *

from game.shared.point import Point
from game.scripting.action import Action
from game.casting.ship import Ship


class ActorUpdates(Action):
    """updates the Actors location
    
    the responsibility of ActorUpdates is to update the actor so the location
    matches the right coordinates of the ship and the ship's weapon displays
    in the right area"""

    def __init__(self):
        pass

    def execute(self, cast, script):
        """Executes the Actor updates
        Args:
            cast (Cast): The cast of actors.
        """
        self._do_updates(cast)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        ship = cast.get_first_actor("ship")

        ship_weapon = cast.get_actors("ship_weapon")
        for bullet in ship_weapon:
            bullet.move_next()
            if bullet.get_position().get_y() <= 7:
                cast.remove_actor("ship_weapon", bullet)

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
