import requests
import os
from dotenv import load_dotenv
from typing import Any


load_dotenv()

headers = {
    "apikey": f'{os.getenv('API_KEY')}'
}

def get_amount_transactions(transaction: dict[str, Any]) -> float | bool:
    url = "https://api.apilayer.com/exchangerates_data/convert"
    try:
        currency = transaction['operationAmount']["currency"]["code"]
    except KeyError:
        print('Какой-то из ключей для \'from\' не найден')
        return False
    try:
        amount = transaction['operationAmount']['amount']
    except KeyError:
        print('Какой-то из ключей для \'amount\' не найден')
        return False

    if currency == 'RUB':
        return amount
    payload = {
        'amount': amount,
        'from': currency,
        'to': 'RUB'
    }

    try:
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()['result']
            return result
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
            return False
    except requests.exceptions.RequestException:
        print('Произошла ошибка. Пожалуйста, повторите попытку позже.')

