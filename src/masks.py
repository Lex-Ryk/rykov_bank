def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску."""
    if len(card_number) != 16:
        return "Слишком много или слишком мало цифр в номере карты!"

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    if len(account_number) < 4:
        return "Слишком мало цифр номера счета!"

    mask_account = "**" + account_number[-4:]

    return mask_account
