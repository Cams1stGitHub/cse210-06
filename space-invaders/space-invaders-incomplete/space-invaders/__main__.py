import random

from constants import *
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director
from game.scripting.actor_inputs import ActorInputs
from game.scripting.actor_updates import ActorUpdates
from game.scripting.actor_outputs import ActorOutputs

from game.casting.cast import Cast
from game.scripting.script import Script
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point

from game.casting.ship import Ship
from game.casting.gem import Gem
from game.casting.rock import Rock


def main():

    # create the cast

    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    ship = Ship()

    ship.set_position(Point(int(MAX_X / 2), int(MAX_Y - CELL_SIZE)))
    ship.set_text("#")
    ship.set_font_size(FONT_SIZE)
    ship.set_color(WHITE)
    cast.add_actor("ship", ship)

    score = Score()
    score.set_position(Point(MAX_X, 0))
    score.add_points(0)
    score.set_player_name("score")

    cast.add_actor("score", score)

    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ActorInputs(keyboard_service))
    script.add_action("update", ActorUpdates())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", MoveActorsAction())
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("output", ActorOutputs())
    print(script._actions)

    director = Director(keyboard_service, video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
