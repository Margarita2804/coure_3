from config import FILE_PATH
import json
from datetime import datetime


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


def date_conversion(data_time):
    convert_date = datetime.fromisoformat(data_time).strftime("%d.%m.%Y")
    return convert_date


def transaction_convert_check(data_check):
    data = data_check.split(' ')
    numbers_check = data[-1]
    name_check = ' '.join(data[:-1])
    if name_check.title() == "Счет":
        final_check = f"{name_check} **{numbers_check[-4:]}"
        return final_check
    else:
        check = f"{numbers_check[:6]}{'*' * 6}{numbers_check[-4:]}"
        format_check = ' '.join([check[x:x+4]for x in range(0, 16, 4)])
        final_check = f"{name_check} {format_check}"
        return final_check
