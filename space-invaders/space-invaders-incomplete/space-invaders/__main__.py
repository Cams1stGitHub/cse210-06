import random
import pyray

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
from game.casting.ship_weapon import ShipWeapon
from game.casting.alien import Alien

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

    ship.set_position(Point(450, int(MAX_Y - 15)))
    ship.set_text("<v>")
    ship.set_font_size(FONT_SIZE)
    ship.set_color(RED)
    cast.add_actor("ship", ship)

    ship_weapon = ShipWeapon(KeyboardService.ship_weapon_direction(pyray.KEY_SPACE), Ship().get_position())

    # ship_weapon.set_text("!")
    # ship_weapon.set_position(ship.get_position())
    # ship_weapon.set_font_size(FONT_SIZE)
    # ship_weapon.set_color(WHITE)
    cast.add_actor("ship_weapon", ship_weapon)

    aliens = Alien()
    
    cast.add_actor("aliens", aliens)

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
