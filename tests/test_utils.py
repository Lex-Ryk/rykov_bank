from src.utils import get_data_transactions
from unittest.mock import patch, mock_open


@patch("builtins.open", new_callable=mock_open)
def test_get_data_transactions_correct(mock_file):
    # Корректный файл с транзакциями
    mock_file.return_value.__enter__.return_value.read.return_value = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
    result = get_data_transactions('data/test_operations.json')
    assert len(result) == 2

    # Пустой файл
    mock_file.return_value.__enter__.return_value.read.return_value = '[]'
    result = get_data_transactions('data/test_empty.json')
    assert result == []

    # Некорректный JSON
    mock_file.return_value.__enter__.return_value.read.return_value = '{"id":1, "amount":100}'
    result = get_data_transactions('data/test_invalid.json')
    assert result == []

    # Данные не являются списком
    mock_file.return_value.__enter__.return_value.read.return_value = '{"data": [{"id":1, "amount":100}]}'
    result = get_data_transactions('data/test_not_list.json')
    assert result == []

    # Файл не найден
    mock_file.side_effect = FileNotFoundError
    result = get_data_transactions('data/non_existent_file.json')
    assert result == []

