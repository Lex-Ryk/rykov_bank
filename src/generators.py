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
    pass
