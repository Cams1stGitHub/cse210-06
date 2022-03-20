from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast


class Ship(Actor):
    """An elite fighter space ship that is part of The Interstellar Armed Forces.
    
    The responsibility of Ship is to move itself.
    
    Attributes:
    ---
    """
    def __init__(self, position):
        """Constructs a new Ship.
        
        Args:
        ---
            position (Point): The position and direction that each cycle will travel in at game start.
        """
        self._segments = []
        self._color = Color(255, 255, 255)
        self._prepare_ship(position)
        self.cast = Cast()

    def get_segments(self):
        """Gets the segments for the ship.

        Returns:
        ---
            List: The list of actors for the ship."""
        return self._segments

    def move_next(self):
        """Moves the actor to its next position."""
        for segment in self._segments:
            segment.move_next()

    def get_ship(self):
        """Gets the first actor from _segments.

        Returns:
        ---
            Actor: The first actor from the list of actors in _segments."""
        return self._segments[0]

    def _prepare_ship(self, position):
        """Constructs a new ship.

        Args:
        ---
            Point: A position to set the ship's position and direction which it will travel in.
        """
        x = int(420)
        y = int(585)
        position = Point(x, y)

        ship = Actor()
        ship.set_text("#")
        ship.set_font_size(FONT_SIZE)
        ship.set_color(WHITE)
        ship.set_position(position)
        self._segments.append(ship)
        # self.cast.add_actor("ship", ship)


        # x = position.get_x()
        # y = position.get_y() - 15
        position = Point(x, y - 15)

        front_of_ship = Actor()
        front_of_ship.set_text("#")
        front_of_ship.set_font_size(FONT_SIZE)
        front_of_ship.set_color(BLACK)
        front_of_ship.set_position(position)
        self._segments.append(front_of_ship)
        # self.cast.add_actor("front_of_ship", front_of_ship)

    def set_ship_color(self, color):
        """Sets the color for each segment of a cycle.

        Args:
        ---
            color (Color): The given color.
        """

        self._color = color
        self._segments[0].set_color(self._color)

    def set_name(self, name):
        """Sets the name for each player.

        Args:
        ---
            String: The players given name as text.
        """
        self._name = name