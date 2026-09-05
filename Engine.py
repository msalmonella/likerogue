import pyray as rl
from Config import parse_config

cfg = parse_config()

# getattr here
# getattr here
# getattr here
# getattr here
class Engine:
    def __init__(self):
        rl.init_window(int(cfg["ENGINE"]["res_width"]),
                       int(cfg["ENGINE"]["res_height"]),
                       cfg["ENGINE"]["title"])
        rl.rl_set_line_width(3)
        rl.set_target_fps(int(cfg["ENGINE"]["fps_max"]))
        rl.disable_cursor()

    def __call__(self):
        pass

