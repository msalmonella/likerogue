import pyray as rl

class Camera():
    def __init__(self):
        self.cam: rl.Camera3D = rl.Camera3D()
        self.cam.position = rl.Vector3(1, 0.5, 0)
        self.cam.target = rl.Vector3(1, 0.5, 1)
        self.cam.up = rl.Vector3(0, 1, 0)
        self.cam.fovy = 60.0
        self.cam.projection = rl.CameraProjection.CAMERA_PERSPECTIVE
        self.camera_mode = 1
