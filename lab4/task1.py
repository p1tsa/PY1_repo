# TODO решите задачу
import json
INPUT_FILE = "input.json"
def task() -> float:
    with open(INPUT_FILE) as file:
        data = json.load(file)
        summary = 0
        for i in data:
            summary += i["score"] * i["weight"]
        return round(summary,3)
print(task())
