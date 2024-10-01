import json


def load_training_data(file):
    return json.load(open(file, "r"))
