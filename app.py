import json
import os

path_karvands = os.path.join(
    os.path.dirname(__file__),
    "data",
    "karvands.json"
)

def load_karvand():
    try:
        with open(path_karvands, "r", encoding="utf-8") as file:
            data_karvands = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        os.makedirs(os.path.dirname(path_karvands), exist_ok=True)

        data_karvands = {
            "bootcamp":{
            "title":"karvand python",
            "year": 2026
        },
            "karvands": [{"id": 0,
                          }]
        }
    return data_karvands

def save_karvands(data_karvands):
    with open(path_karvands, "w", encoding="utf-8") as file:
        json.dump(data_karvands, file, indent=4)

data_karvands=load_karvand()
save_karvands(data_karvands)