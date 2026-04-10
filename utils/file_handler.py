import json
import os

FILE_PATH = "data/data.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return {"students": [], "rooms": []}
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

# 1 try bala kawa ka na washwa bss bia sti direct laray ta cha,,, khair lazzz pa ma shy khapal hn sabar nashta