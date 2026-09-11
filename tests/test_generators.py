import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(data_transactions):
    usd_currency = filter_by_currency(data_transactions, "USD")
    assert next(usd_currency) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_currency) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    with pytest.raises(StopIteration):
        next(usd_currency)


def test_filter_by_currency_not_currency(data_transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transactions, "NOT"))


def test_filter_by_currency_without_transactions_and_currency(data_transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(list(), "USD"))

    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transactions, ""))


def test_transaction_descriptions(data_transactions):
    descriptions = transaction_descriptions(data_transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_without_value_description():
    assert next(transaction_descriptions([{"description": ""}])) == ""


def test_transaction_descriptions_without_key_description():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([{"state": "EXECUTED"}]))


def test_transaction_description_without_transactions():
    with pytest.raises(StopIteration):
        next(transaction_descriptions(list()))


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (2, 4, ["0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (
            9999999999999990,
            9999999999999993,
            ["9999 9999 9999 9990", "9999 9999 9999 9991", "9999 9999 9999 9992", "9999 9999 9999 9993"],
        ),
    ],
)
def test_card_number_generator(start, end, expected):
    gen_card_numbers = card_number_generator(start, end)

    for card_number in expected:
        assert next(gen_card_numbers) == card_number


def test_card_number_generator_extreme_start():
    with pytest.raises(ValueError):
        assert next(card_number_generator(0, 10))

    with pytest.raises(ValueError):
        assert next(card_number_generator(-10, 10))


def test_card_number_generator_extreme_end():
    with pytest.raises(ValueError):
        assert next(card_number_generator(10, 10000000000000000))


def test_card_number_generator_type_error():
    with pytest.raises(TypeError):
        assert next(card_number_generator("3", 234))

    with pytest.raises(TypeError):
        assert next(card_number_generator(234, "239"))

    with pytest.raises(TypeError):
        assert next(card_number_generator())

    with pytest.raises(TypeError):
        assert next(card_number_generator("", ""))


def test_card_number_generator_end_less_start():
    with pytest.raises(StopIteration):
        assert next(card_number_generator(2, 1))
