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
        print(self.get_velocity().get_x())
        # if self._position.get_x() >= 0 and self._position.get_x() <= 885:
        # x = (self._position.get_x() + self._velocity.get_x()) % MAX_X
        # y = (self._position.get_y() + self._velocity.get_y()) % MAX_Y
        #     # if x < 0:
        #     #         x = 0
        #     # if x > 885:
        #     #     x = 885
        # self._position = Point(x, y)
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

        for x in range(30, 870, 30):
            for y in range(4):
                position = Point(x + 0 * 15, 30 + y * 15)
                velocity = Point(0, 1)
                text = "<x>"

                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(self._color)
                self._segments.append(segment)

                # position = Point(x + 1 * 15, y * 15)
                # velocity = Point(0, 1)
                # text = "="

                # segment = Actor()
                # segment.set_position(position)
                # segment.set_velocity(velocity)
                # segment.set_text(text)
                # segment.set_color(self._color)
                # self._segments.append(segment)

                # position = Point(x + 2 * 15, y * 15)
                # velocity = Point(0, 1)
                # text = ">"

                # segment = Actor()
                # segment.set_position(position)
                # segment.set_velocity(velocity)
                # segment.set_text(text)
                # segment.set_color(self._color)
                # self._segments.append(segment)

    def set_name(self, name):
        """Sets the name for each player.

            Args:
            ---
                String: The players given name as text.
            """
        self._name = name
