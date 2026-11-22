import pyray as rl
from Config import parse_config

cfg = parse_config()

class Engine:
    def __init__(self):
        self.show_stats = False
        rl.init_window(int(cfg["ENGINE"]["res_width"]),
                       int(cfg["ENGINE"]["res_height"]),
                       cfg["ENGINE"]["title"])
        rl.rl_set_line_width(3)
        rl.set_target_fps(int(cfg["ENGINE"]["fps_max"]))
        rl.disable_cursor()

    def toggle_stats(self):
        self.show_stats = not self.show_stats

    def __call__(self):
        pass

