import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='logs/masks.log',  # Запись логов в файл
                    filemode='w',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8')

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску."""
    mask_card_number = ''
    logger.info(f'Попытка зашифровки номера карты {card_number}')

    if not isinstance(card_number, str):
        logger.error(f"Ошибка типа данных: тип card number - {type(card_number)} not string")
    elif not card_number.isdigit():
        logger.error(f"Некорректные символы в номере карты.")
    elif len(card_number) != 16:
        logger.error(f"Слишком много или слишком мало цифр в номере карты!")
    else:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info(f'Номер карты успешно зашифрован: {mask_card_number}')

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    mask_account = ''
    logger.info(f'Попытка зашифровки номера счёта: {account_number}')

    if not isinstance(account_number, str):
        logger.error(f"Ошибка типа данных: тип card number - {type(account_number)} not string")
    elif not account_number.isdigit():
        logger.error("Некорректные символы в номере")
    elif len(account_number) < 4:
        logger.error(f"Слишком мало цифр в номере счёта для маскировки! {len(account_number)} меньше 4")
    else:
        mask_account = "**" + account_number[-4:]
        logger.info(f'Номер счёта успешно зашифрован: {mask_account}')


    return mask_account
