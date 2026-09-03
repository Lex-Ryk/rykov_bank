import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected", [("7000792289606361", "7000 79** **** 6361"), ("0000000000000000", "0000 00** **** 0000")]
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", ["700 7/22.9606361", "ghfdertygffgrwer"])
def test_get_card_number_incorrect_characters_in_card_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", ["1234567891012345678920", "2345"])
def test_get_mask_card_number_invalid_card_number_length(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [23456765432, 23456543.5432])
def test_get_mask_card_number_wrong_type(card_number):
    with pytest.raises(TypeError):
        get_mask_card_number(card_number)


# Тесты для функции get_mask_account:
@pytest.mark.parametrize("account_number, expected", [("73654432108430135874305", "**4305"), ("0000", "**0000")])
def test_get_mask_account_number(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", ["700 7/22.9606361", "ghfdertygffgrwer"])
def test_get_account_number_incorrect_characters_in_account_number(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


@pytest.mark.parametrize("account_number", ["", "345"])
def test_get_mask_account_number_invalid_account_number_length(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


@pytest.mark.parametrize("account_number", [23456765432, 23456543.5432])
def test_get_mask_account_number_wrong_type(account_number):
    with pytest.raises(TypeError):
        get_mask_account(account_number)
