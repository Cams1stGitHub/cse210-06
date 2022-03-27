from tkinter.messagebox import NO
from wsgiref.util import shift_path_info
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
            self._handle_collision(cast)
        else:
            self._handle_game_over(cast)

    def _handle_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of its segments or the other
        cycle.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        bullets = cast.get_actors("ship_weapon")
        score = cast.get_first_actor("score")
        ship = cast.get_first_actor("ship")
        alienslist = cast.get_first_actor("aliens")
        
        if len(alienslist.get_segments()) == 0:
            self._is_game_over = True
            self._game_over_message = "You win!"
            ship.set_font_size(50)
            ship.set_position(Point(int(MAX_X/2), int(MAX_Y/4)))
        
        for alien in alienslist.get_segments():
            if alien.get_position().get_y() >= MAX_Y-7:
                self._is_game_over = True

            for bullet in bullets:
                if alien.get_position().bounding_equals(bullet.get_position()):
                    alienslist._remove_alien(alien)
                    cast.remove_actor("ship_weapon", bullet)
                    score.add_points(alien.get_points())
                    
        for alien in alienslist.get_segments():
            if ship.get_position().bounding_equals(alien.get_position()):
                self._is_game_over = True
                self._game_over_message = "Game over!"
                

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

            # Gets segments for cycle one and two

            # Creates gameover message
            game_over = GameOver()
            game_over.set_position(position)
            game_over.set_text(self._game_over_message)
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)