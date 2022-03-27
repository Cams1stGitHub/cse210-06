import random
from game.scripting.action import Action
from game.shared.point import Point
from constants import *
from game.casting.ship import Ship
from game.casting.actor import Actor


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
        # a = Ship().move_next()
        ship = cast.get_first_actor("ship")
        velocity = self._keyboard_service.get_direction()
        print(f"psoition: {ship.get_position().get_x()}")
        ship.set_velocity(velocity)
        # ship.move_next()

        if self._keyboard_service.fire_weapon():
            ship_weapon = Actor()
            ship_weapon.set_position(ship.get_position())
            ship_weapon.set_velocity(Point(0, -7))
            ship_weapon.set_text("!")
            ship_weapon.set_font_size(FONT_SIZE)
            ship_weapon.set_color(YELLOW)
            cast.add_actor("ship_weapon", ship_weapon)