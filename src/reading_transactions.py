import pandas as pd


def read_csv_file(file_path: str, sep: str = ";", encoding: str = "utf-8") -> pd.DataFrame:
    """функция для считывания csv файла с указанным разделителем и кодировкой"""
    try:
        return pd.read_csv(file_path, sep=sep, encoding=encoding)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except pd.errors.ParserError as e:
        raise ValueError(f"Ошибка парсинга CSV-файла {file_path}: {e}") from e
    except UnicodeDecodeError as e:
        raise ValueError(
            f"Ошибка кодировки при чтении {file_path}: попробуйте другую кодировку (например, cp1251)."
        ) from e


def read_excel_file(file_path: str) -> pd.DataFrame:
    """функция для считывания excel-файла (.xlsx, .xls)"""
    try:
        return pd.read_excel(file_path, engine="openpyxl")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise ValueError(f"Не удалось прочитать Excel-файл '{file_path}': {e}") from e
