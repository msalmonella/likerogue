import pyray as rl
# import math
from Engine import Engine
from Input import Input
from Camera import Camera

engine = Engine()
_input = Input(engine)
camera = Camera()

class Player:
    def __init__(self, position):
        pass

def main():
    engine()

    map_size = 10

    while not rl.window_should_close():
        _input.MouseInput(camera.cam)
        _input.KeyboardInput()
        rl.begin_drawing()
        rl.begin_mode_3d(camera.cam)
        rl.clear_background(rl.SKYBLUE)
        rl.draw_grid(map_size * 10, 0.2)
        rl.draw_plane((0, 0.5, 0), (map_size * 2, map_size * 2), rl.WHITE)
        rl.end_mode_3d()
        if engine.show_stats:
            rl.draw_fps(10, 10)
        rl.end_drawing()

if __name__ == "__main__":
    main()
