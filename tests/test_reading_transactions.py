import pytest
import pandas as pd
from unittest.mock import patch, Mock

from src.reading_transactions import read_csv_file, read_excel_file


@pytest.fixture
def df_data():
    return pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': [30, 25]
    })


def test_read_csv_file_success(df_data):
    mock_df = df_data

    with patch('src.reading_transactions.pd.read_csv', return_value=mock_df) as mock_read:
        df = read_csv_file("test.csv")

        mock_read.asser_called_once_with('operations.csv', sep=';', encoding='utf-8')
        assert df.shape == (2, 2)
        assert list(df.columns) == ["name", 'age']
        assert df['age'].tolist() == [30, 25]

def test_read_csv_file_parser_error():
    with patch('src.reading_transactions.pd.read_csv', side_effect=pd.errors.ParserError('bad CSV')):
        with pytest.raises(ValueError) as exc_info:
            read_csv_file('bad.csv')

        assert 'Ошибка парсинга CSV-файла' in str(exc_info.value)

def test_read_csv_file_unicode_error():
    with patch(
            'src.reading_transactions.pd.read_csv', side_effect=UnicodeDecodeError(
                "utf-8", b"", 0, 1, "bad encoding"
            )):
        with pytest.raises(ValueError) as exc_info:
            read_csv_file("ops.csv", encoding='utf-8')

        assert "Ошибка кодировки при чтении" in str(exc_info.value)

def test_read_excel_file_success(df_data):
    mock_df = df_data

    with patch('src.reading_transactions.pd.read_excel', return_value=mock_df) as mock_read:
        df = read_excel_file('test.xlsx')

        mock_read.assert_called_once_with('test.xlsx', engine='openpyxl')
        assert df.shape == (2, 2)
        assert list(df.columns) == ["name", 'age']
        assert df['age'].tolist() == [30, 25]

def test_read_excel_file_general_exception():
    with patch("src.reading_transactions.pd.read_excel", side_effect=RuntimeError("Excel engine failed")):
        with pytest.raises(ValueError) as exc_info:
            read_excel_file("broken.xlsx")

        assert "Не удалось прочитать Excel-файл" in str(exc_info.value)

def test_read_excel_file_notfound():
    with patch('src.reading_transactions.pd.read_excel', side_effect=FileNotFoundError('file not found')):
        with pytest.raises(FileNotFoundError) as exc_info:
            read_csv_file('bad.xlsx')

        assert 'Файл не найден' in str(exc_info.value)
