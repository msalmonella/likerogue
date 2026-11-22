import pyray as rl
# import math
from Engine import Engine
from Input import Input

engine = Engine()
_input = Input(engine)

class Player:
    def __init__(self, position):
        pass

def main():
    engine()
    input = Input(engine)

    map_size = 10

    while not rl.window_should_close():
        if engine.show_stats:
            rl.draw_fps(10, 10)
        rl.begin_drawing()
        rl.clear_background(rl.SKYBLUE)
        rl.begin_mode_3d(input.camera)
        _input.MouseInput(input.camera)
        _input.KeyboardInput()
        rl.draw_grid(map_size * 10, 0.2)
        rl.draw_plane((0, 0.5, 0), (map_size * 2, map_size * 2), rl.WHITE)
        rl.end_mode_3d()
        rl.end_drawing()

if __name__ == "__main__":
    main()
