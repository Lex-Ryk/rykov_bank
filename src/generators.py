def filter_by_currency(list_transactions: list[dict], currency: str):
    filter_transactions = (
        transaction for transaction in list_transactions
        if transaction['operationAmount']['currency']['name'] ==
           currency)
    return filter_transactions


def transaction_descriptions(list_transactions: list[dict]):
    descriptions = (
        transaction["description"] for transaction in list_transactions if 'description' in transaction
    )

    return descriptions


def card_number_generator(start: int, end: int):
    length_card_number = 16

    if start < 1 or end > 9999999999999999:
        raise ValueError('Неверный диапазон значений генерации')

    numbers = (str(number) for number in range(start, end + 1))
    card_numbers = ('0' * (length_card_number - len(number)) + number for number in numbers)
    card_numbers = (card_number[0:4] + ' ' + card_number[4:8] + ' ' + card_number[8:12] + ' ' + card_number[12:16] for card_number in card_numbers)

    return card_numbers
