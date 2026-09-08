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

                config[section][key] = value
        # for i in config["KEYBOARD"]:
        #     print("KEY_" + str(config["KEYBOARD"]))

    return config
