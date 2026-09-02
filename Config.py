"""To read the config and properly return the values"""
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

                config[section][key] = "rl.KeyboardKey.KEY_" + value

    return config


config = parse_config()

print(config["KEYBOARD"]["mv_forward"])
print(config["KEYBOARD"]["mv_backwards"])
print(config["KEYBOARD"]["mv_left"])
print(config["KEYBOARD"]["mv_right"])

