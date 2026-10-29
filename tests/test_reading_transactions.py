from unittest.mock import (
    Mock,
    patch,
)

import pandas as pd
import pytest

from src.reading_transactions import (
    read_csv_file,
    read_excel_file,
)


@pytest.fixture
def mock_df():
    return pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})


def test_read_csv_file_success(mock_df):
    with patch("src.reading_transactions.pd.read_csv", return_value=mock_df) as mock_read:
        result = read_csv_file("test.csv")

        # Проверяем, что read_csv вызвали с правильным аргументом
        mock_read.asser_called_once_with("test.csv", sep=";", encoding="utf-8")

        assert isinstance(result, list)
        assert len(result) == 2
        assert result == [
            {"name": "Alice", "age": 30},
            {'name': "Bob", 'age': 25}
        ]


def test_read_csv_file_parser_error():
    with patch("src.reading_transactions.pd.read_csv", side_effect=pd.errors.ParserError("bad CSV")):
        with pytest.raises(ValueError) as exc_info:
            read_csv_file("bad.csv")

        assert "Ошибка парсинга CSV-файла" in str(exc_info.value)


def test_read_csv_file_unicode_error():
    with patch(
        "src.reading_transactions.pd.read_csv", side_effect=UnicodeDecodeError("utf-8", b"", 0, 1, "bad encoding")
    ):
        with pytest.raises(ValueError) as exc_info:
            read_csv_file("ops.csv", encoding="utf-8")

        assert "Ошибка кодировки при чтении" in str(exc_info.value)


def test_read_excel_file_success(mock_df):
    with patch("src.reading_transactions.pd.read_excel", return_value=mock_df) as mock_read:
        result = read_excel_file("test.xlsx")

        mock_read.assert_called_once_with("test.xlsx", engine="openpyxl")

        assert isinstance(result, list)
        assert len(result) == 2
        assert result == [
            {"name": "Alice", "age": 30},
            {'name': "Bob", 'age': 25}
        ]


def test_read_excel_file_general_exception():
    with patch("src.reading_transactions.pd.read_excel", side_effect=RuntimeError("Excel engine failed")):
        with pytest.raises(ValueError) as exc_info:
            read_excel_file("broken.xlsx")

        assert "Не удалось прочитать Excel-файл" in str(exc_info.value)


def test_read_excel_file_notfound():
    with patch("src.reading_transactions.pd.read_excel", side_effect=FileNotFoundError("file not found")):
        with pytest.raises(FileNotFoundError) as exc_info:
            read_csv_file("bad.xlsx")

        assert "Файл не найден" in str(exc_info.value)
