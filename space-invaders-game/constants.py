from game.shared.color import Color


MAX_X = 888
MAX_Y = 600
COLUMNS = 60
ROWS = 40
CELL_SIZE = 15
FRAME_RATE = 15
FONT_SIZE = 15
ALIEN_LENGTH = 20
CAPTION = "Space Invaders"
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
GREEN = Color(0, 255, 0)
PURPLE = Color(118,37,190)
BLUE = Color(37,75,190)
TEAL = Color(37,187,190)
ORANGE = Color(190,123,37)
YELLOW = Color(255,255,0)
ALIEN_COLORS = [PURPLE, BLUE, TEAL, ORANGE]

RED = Color(255, 0, 0)
DEFAULT_ROCKS = 20
DEFAULT_GEMS = 20

#sounds
EXPLOSION_SOUND = "game/assets/explosion.wav"
SHOT_SOUND = "game/assets/shot.wav"
LOOP_SOUND = "game/assets/loop.wav"
GAME_OVER = "game/assets/gameover.wav"
STAGE_CLEAR = "game/assets/win.wav"