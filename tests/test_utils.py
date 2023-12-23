from src.utils import (load_data, sorted_data, date_conversion, transaction_convert_check, final_transaction,
                       list_transaction)
from config import TEST_FILE_PATH, TEST_SORTED_FILE_PATH, TEST_LIST_TRANSACTION_PATH
import json


def test_load_date():
    data = load_data(TEST_FILE_PATH)
    assert data == [1, 2, 3]


def test_sorted_data():
    with open(TEST_SORTED_FILE_PATH) as file:
        file_json = json.load(file)
    data = sorted_data(file_json)
    assert data == [{'date': '2019-08-26T10:50:58.294041', 'state': 'EXECUTED'},
                    {'date': '2019-07-03T18:35:29.512364', 'state': 'EXECUTED'},
                    {'date': '2018-06-30T02:08:58.425572', 'state': 'EXECUTED'}]


def test_date_conversion():
    data = '2019-07-03T18:35:29.512364'
    assert date_conversion(data) == '03.07.2019'


def test_transaction_convert_check():
    data1 = "Счет 90424923579946435907"
    data2 = "Visa Platinum 1246377376343588"
    assert transaction_convert_check(data1) == 'Счет **5907'
    assert transaction_convert_check(data2) == 'Visa Platinum 1246 37** **** 3588'


def test_final_transaction():
    data1 = {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
              "amount": "41096.24",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
    }
    data2 = {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
              "amount": "40701.91",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
    }
    assert final_transaction(data1) == ('\n08.12.2019 Открытие вклада\n'
                                        'Неизвестный отправитель -> Счет **5907\n'
                                        '41096.24 USD')
    assert final_transaction(data2) == ('\n04.04.2018 Перевод организации\n'
                                        'Visa Gold 5999 41** **** 6353 -> Счет **4472\n'
                                        '40701.91 USD')


def test_list_transaction():
    with open(TEST_LIST_TRANSACTION_PATH) as file:
        file_json = json.load(file)
    data = list_transaction(file_json)
    assert data == ['\n14.06.2019 Перевод со счета на счет\n'
                    'Счет **5679 -> Счет **8747\n'
                    '63150.74 USD',
                    '\n29.03.2019 Перевод с карты на счет\n'
                    'Visa Classic 1203 92** **** 4079 -> Счет **2721\n'
                    '30234.99 USD',
                    '\n23.12.2018 Перевод с карты на карту\n'
                    'МИР 8665 24** **** 6074 -> Maestro 3000 70** **** 4087\n'
                    '47408.20 USD']