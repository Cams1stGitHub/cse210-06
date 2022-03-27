from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast


class Alien(Actor):
    """An elite fighter space ship that is part of The Interstellar Armed Forces.

    The responsibility of Ship is to move itself.

    Attributes:
    ---
    """


    def __init__(self):
        """Constructs a new Ship.

            Args:
            ---
                position (Point): The position and direction that each cycle will travel in at game start.
            """
        super().__init__()
        self._segments = []
        self._prepare_ship(Point(100, 100))
        self.velocityX = 0
        self.velocityY = 0

    def get_segments(self):
        """Gets the segments for each cycle.

        Returns:
        ---
            List: The list of actors for each cycle"""
        return self._segments

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position
            from one side of the screen to the other when it reaches the given maximum x and y values.

            Args:
            ---
                max_x (int): The maximum x value.
                max_y (int): The maximum y value.
            """
        for segment in self._segments:
            segment.move_next()
    
    def set_ship_color(self, color):
        """Sets the color for each segment of a cycle.

            Args:
            ---
                color (Color): The given color.
            """

        self._color = color
        self._segments[0].set_color(self._color)

    def _prepare_ship(self, position):
        x = position.get_x()
        y = position.get_y()
        points = [15,10,5,20]
        for x in range(30, 870, 30):
            for y in range(4):
                position = Point(x + 0 * 15, 30 + y * 15)
                velocity = Point(0, 1)
                text = "<x>"

                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(ALIEN_COLORS[y-1])
                segment.set_points(points[y-1])
                self._segments.append(segment)

    def _remove_alien(self, alien):
        self._segments.remove(alien)