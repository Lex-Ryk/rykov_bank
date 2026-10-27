import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
masks_file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
masks_file_handler.setFormatter(file_formatter)
logger.addHandler(masks_file_handler)
logger.setLevel(logging.DEBUG)


def get_data_transactions(path: str) -> list[dict[str, Any]]:
    """Получение списка словарей с данными о финансовых транзакциях"""
    logger.info(f'Попытка открытия файла {path}')
    try:
        with open(path, encoding="utf-8-sig") as file_transactions:
            logger.info('Файл успешно найден и открыт')
            logger.info('Попытка декодирования json-файла')
            try:
                data_transactions = json.load(file_transactions)
                logger.info('JSON-файл успешно декодирован')
                if not isinstance(data_transactions, list):
                    logger.warning("Данные в файле не являются списком")
                    data_transactions = []
            except json.JSONDecodeError:
                logger.error('Ошибка декодирования файла')
                data_transactions = []
    except FileNotFoundError:
        logger.error(f'Файл {path} не найден')
        data_transactions = []

    return data_transactions
