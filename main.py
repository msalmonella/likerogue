import pyray as rl
import math

class Player:
    def __init__(self, position):
        pass

camera: rl.Camera3D = rl.Camera3D()
camera.position = rl.Vector3(1, 0.5, 0)
camera.target = rl.Vector3(1, 0.5, 1)
camera.up = rl.Vector3(0, 1, 0)
camera.fovy = 60.0
camera.projection = rl.CameraProjection.CAMERA_PERSPECTIVE
camera_mode = 1

def Input():
    mouse_delta = rl.get_mouse_delta()
    rotation = rl.Vector3(
            mouse_delta.x * 0.05,
            mouse_delta.y * 0.05,
            0.0
            )
    rl.update_camera_pro(camera, (0, 0, 0), rotation, 0.0)


def main():
    rl.init_window(1024, 768, "Raylib")
    rl.rl_set_line_width(3)
    rl.set_target_fps(60)
    rl.disable_cursor()

    map_size = 10

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.SKYBLUE)
        rl.begin_mode_3d(camera)
        Input()
        rl.draw_grid(map_size * 10, 0.2)
        rl.draw_plane((0, 0.5, 0), (map_size * 2, map_size * 2), rl.WHITE)
        rl.end_mode_3d()
        rl.end_drawing()

if __name__ == "__main__":
    main()
