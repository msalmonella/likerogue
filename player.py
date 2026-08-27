import pyray as rl


class Player:

    def __init__(self, position: Vector2):
        self.position = position
        self.velocity = rl.Vector3(0, 0, 0)

        self.speed = 5
        self.camera = None
