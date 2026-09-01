import pytest

from src.widget import mask_account_card, get_date
from tests.conftest import correct_format_dates


# Тестирование функции account_card
def test_account_card(info_cards):
    for info_card, expected in info_cards:
        assert mask_account_card(info_card) == expected


def test_account_card_invalid_info_card(invalid_info_cards):
    for invalid_info_card in invalid_info_cards:
        with pytest.raises(ValueError):
            mask_account_card(invalid_info_card)


# Тестирование функции get_date
def test_get_date(correct_format_dates):
    for date, expected in correct_format_dates:
        assert get_date(date) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("not-a-date")

    with pytest.raises(ValueError):
        get_date("")