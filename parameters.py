import json


def read(path):
    with open(path) as json_data:
        return json.load(json_data)
