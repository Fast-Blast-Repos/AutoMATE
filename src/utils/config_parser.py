def parse_config(filepath):
    import json
    with open(filepath, "r") as file:
        data = file.read()
    return json.loads(data)
