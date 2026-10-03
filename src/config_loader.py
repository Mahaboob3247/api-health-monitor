import json

def load_apis():
    with open("config/apis.json", "r") as file:
        data = json.load(file)

    return data["apis"]