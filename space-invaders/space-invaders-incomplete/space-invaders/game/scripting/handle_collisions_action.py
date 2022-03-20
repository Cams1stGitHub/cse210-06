from constants import *

from game.scripting.action import Action
from game.shared.point import Point
from game.casting.game_over_message import GameOver


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with its segments or the segments of the other cycle, or the game is over.

    Attributes:
    ---
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._game_over_message = ""

    def get_is_game_over(self):
        return self._is_game_over

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of its segments or the other
        cycle.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        pass


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns both cycles white if the game is over.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """

        # Gets position for gameover message
        x = int(MAX_X / 2)
        y = int(MAX_Y / 2)
        position = Point(x, y)

        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            
            # Gets segments for cycle one and two
            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()
            
            # Creates gameover message
            game_over = GameOver()
            game_over.set_position(position)
            game_over.set_text(self._game_over_message)
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)

            # Changes color of cycles to white after the game ends
            for segment in segments_one:
                segment.set_color(WHITE)

            for segment in segments_two:
                segment.set_color(WHITE)