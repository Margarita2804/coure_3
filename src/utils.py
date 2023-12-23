from config import FILE_PATH
import json


def load_data(file_path):
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


def sorted_data(data):
    executed_list = []
    for item in data:
        if item.get("state") == "EXECUTED":
            executed_list.append(item)
    sorted_json = sorted(executed_list, key=lambda operation: operation["date"], reverse=True)
    return sorted_json
