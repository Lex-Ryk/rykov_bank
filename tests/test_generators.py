import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(data_transactions):
    usd_currency = filter_by_currency(data_transactions, 'USD')
    assert next(usd_currency) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(usd_currency) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    with pytest.raises(StopIteration):
        next(usd_currency)


def test_filter_by_currency_not_currency(data_transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transactions, 'NOT'))


def test_filter_by_currency_without_transactions_and_currency(data_transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(list(), "USD"))

    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transactions, ''))


