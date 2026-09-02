import pyray as rl

def parse_config():
    config = {}
    section = None

    with open("config.cfg") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1]
                config[section] = {}

            elif "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"')

                enum_value = getattr(rl.KeyboardKey, "KEY_" + value)
                config[section][key] = enum_value

    return config

