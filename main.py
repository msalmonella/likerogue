import pyray as rl
import player
import math
import random

def mouse():
    

def main():
    rl.init_window(800, 600, "Raylib")
    rl.rl_set_line_width(3)
    angle: float = 0.0

    camera: rl.Camera3D = rl.Camera3D((0, 0.5, 0),
                                      (1, 0.5, 1),
                                      (0, 1, 0),
                                      60)
    map_size = 10

    while not rl.window_should_close():
        angle += 0.001
        camera.position.x = math.cos(angle) * 5
        camera.position.z = math.sin(angle) * 5

        rl.begin_drawing()
        rl.clear_background(rl.SKYBLUE)
        rl.begin_mode_3d(camera)
        rl.draw_grid(map_size * 10, 0.2)
        rl.draw_plane((0, 0.5, 0), (map_size * 2, map_size * 2), rl.WHITE)
        rl.end_mode_3d()
        rl.end_drawing()

main()
