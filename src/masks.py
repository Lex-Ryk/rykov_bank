def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску."""

    if not isinstance(card_number, str):
        raise TypeError("Ошибка типа данных")

    if not card_number.isdigit():
        raise ValueError("Неккоректные символы в номере карты")

    if len(card_number) != 16:
        raise ValueError("Слишком много или слишком мало цифр в номере карты!")

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""

    if not isinstance(account_number, str):
        raise TypeError("Ошибка типа данных")

    if not account_number.isdigit():
        raise ValueError("Неккоректные символы в номере карты")

    if len(account_number) < 4:
        raise ValueError("Слишком мало цифр в номере счёта для маскировки!")

    mask_account = "**" + account_number[-4:]

    return mask_account
