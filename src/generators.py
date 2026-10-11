from collections.abc import Iterable
from typing import Any


def filter_by_currency(list_transactions: list[dict[str, Any]], currency: str) -> Iterable[dict[str, Any]]:
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    filter_transactions = (
        transaction
        for transaction in list_transactions
        if transaction["operationAmount"]["currency"]["name"] == currency
    )
    return filter_transactions


def transaction_descriptions(list_transactions: list[dict[str, Any]]) -> Iterable[str]:
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in list_transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterable[str]:
    """
    Функция генерирующая номера карт в указанном диапазоне
    :param start: первый номер карты
    :param end: конечный номер карты
    :return: выдает номера банковских карт
    """
    length_card_number = 16

    if start < 1 or end > 9999999999999999:
        raise ValueError("Неверный диапазон значений генерации")

    numbers = (str(number) for number in range(start, end + 1))
    card_numbers = ("0" * (length_card_number - len(number)) + number for number in numbers)
    card_numbers = (
        card_number[0:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]
        for card_number in card_numbers
    )

    return card_numbers
