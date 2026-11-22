import pyray as rl
from Config import parse_config
from Camera import Camera
import Engine

cfg = parse_config()
camera = Camera()

class Input:
    def __init__(self, engine):
        self.engine = engine

    def __call__(self, camera: rl.Camera3D):
        self.MouseInput(camera)
        self.KeyboardInput()

    def MouseInput(self, camera):
        mouse_delta = rl.get_mouse_delta()
        rotation = rl.Vector3(
                mouse_delta.x * 0.05,
                mouse_delta.y * 0.05,
                0.0
                )
        rl.update_camera_pro(camera, (0, 0, 0), rotation, 0.0)

    def KeyboardInput(self):
        if rl.is_key_down(getattr(rl.KeyboardKey, "KEY_" + cfg["KEYBOARD"]["mv_forward"])):
            rl.clear_background(rl.RED)
        if rl.is_key_down(getattr(rl.KeyboardKey, "KEY_" + cfg["KEYBOARD"]["mv_backwards"])):
            rl.clear_background(rl.GREEN)
        if rl.is_key_down(getattr(rl.KeyboardKey, "KEY_" + cfg["KEYBOARD"]["mv_left"])):
            rl.clear_background(rl.BLUE)
        if rl.is_key_down(getattr(rl.KeyboardKey, "KEY_" + cfg["KEYBOARD"]["mv_right"])):
            rl.clear_background(rl.YELLOW)
        if rl.is_key_pressed(getattr(rl.KeyboardKey, "KEY_" + cfg["KEYBOARD"]["cl_showstats"])):
            self.engine.toggle_stats()
