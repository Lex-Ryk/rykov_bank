from src import masks


def mask_account_card(info_card: str) -> str:
    """Функция обработки информации о карте или счете"""
    list_info_card = info_card.split()
    quantity_item_list = len(list_info_card)
    mask_info_card = ''

    if quantity_item_list == 3 or quantity_item_list == 2:
        mask_info_card += ' '.join(list_info_card[:-1])
    else:
        return 'Неверно введены данные карты!'

    if list_info_card[0] == 'Счет':
        mask_info_card += ' ' + masks.get_mask_account(list_info_card[-1])
    else:
        mask_info_card += ' ' + masks.get_mask_card_number(list_info_card[-1])

    return mask_info_card