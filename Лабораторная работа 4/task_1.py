import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, "r" ,encoding="utf-8") as f:
        data = json.load(f)
    list_values = [i["score"]*i["weight"] for i in data]
    return round(sum(list_values), 3)

print(task())
