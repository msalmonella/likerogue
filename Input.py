import pyray as rl
from Config import parse_config

cfg = parse_config()

# getattr here get the content from config parser and apply the getattr function here.
# getattr here
# getattr here
# getattr here

class Input:
    camera: rl.Camera3D = rl.Camera3D()
    camera.position = rl.Vector3(1, 0.5, 0)
    camera.target = rl.Vector3(1, 0.5, 1)
    camera.up = rl.Vector3(0, 1, 0)
    camera.fovy = 60.0
    camera.projection = rl.CameraProjection.CAMERA_PERSPECTIVE
    camera_mode = 1

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
            # rl.draw_text("merhaba", 10, 10, 100, rl.RED)
            rl.clear_background(rl.RED)
