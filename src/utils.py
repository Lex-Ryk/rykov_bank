import json
from typing import Any


def get_data_transactions(path: str) -> list[dict[str, Any]]:
    """ Получение списка словарей с данными о финансовых транзакциях """
    try:
        with open(path, encoding='utf-8-sig') as file_transactions:
            try:
                data_transactions = json.load(file_transactions)
                if not isinstance(data_transactions, list):
                    print('Данные в файле не являются списком')
                    data_transactions = []
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
                data_transactions = []
    except FileNotFoundError:
        print('Файл не найден')
        data_transactions = []

    return data_transactions