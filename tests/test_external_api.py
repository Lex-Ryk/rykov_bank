from unittest.mock import patch

from src.external_api import get_amount_transaction


@patch("src.external_api.requests.get")
def test_get_amount_transaction_successful(mocked_get):
    """Проверка корректного вызова"""
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": 1000}}
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"result": 1000.0}
    result = get_amount_transaction(transaction)
    assert result == 1000.0


@patch("src.external_api.requests.get")
def test_get_amount_transaction_not_transaction(mocked_get):
    """Проверка вызова с пустым словарем"""
    transaction = {}
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"result": 1000.0}
    result = get_amount_transaction(transaction)
    assert result == False


@patch("src.external_api.requests.get")
def test_get_amount_transaction_rub(mocked_get):
    """Проверка вызова с рублями"""
    transaction = {"operationAmount": {"currency": {"code": "RUB"}, "amount": 1000}}
    result = get_amount_transaction(transaction)
    assert result == 1000.0


@patch("src.external_api.requests.get")
def test_get_amount_transaction_status_code_error(mocked_get):
    """Проверка вызова с некорректным статус кодом"""
    transaction = {"operationAmount": {"currency": {"code": "EUR"}, "amount": 1000}}
    mocked_get.return_value.status_code = 100
    mocked_get.return_value.json.return_value = {"result": 1000.0}
    result = get_amount_transaction(transaction)
    assert result == False


@patch("src.external_api.requests.get")
def test_get_amount_transaction_not_amount(mocked_get):
    """Проверка вызова без amount"""
    transaction = {
        "operationAmount": {
            "currency": {"code": "EUR"},
        }
    }
    result = get_amount_transaction(transaction)
    assert result == False


@patch("src.external_api.requests.get")
def test_get_amount_transaction_not_code(mocked_get):
    """Проверка вызова без кода"""
    transaction = {"operationAmount": {"amount": 1000}}
    result = get_amount_transaction(transaction)
    assert result == False


@patch("src.external_api.requests.get")
def test_get_amount_transaction_headers_included(mocked_get):
    """Проверка корректного формирования заголовка"""
    with patch("os.getenv", return_value="TEST_KEY") as mocked_getenv:
        transaction = {"operationAmount": {"currency": {"code": "EUR"}, "amount": 1000}}
        get_amount_transaction(transaction)
        mocked_getenv.assert_called_once_with("API_KEY")
        mocked_get.assert_called_once()
        _, kwargs = mocked_get.call_args
        assert kwargs["headers"] == {"apikey": "TEST_KEY"}
        assert kwargs["params"] == {"amount": 1000, "from": "EUR", "to": "RUB"}


@patch("src.external_api.requests.get")
def test_get_amount_transaction_headers_empty_when_missing_api_key(mocked_get):
    with patch("os.getenv", return_value=""):
        transaction = {"operationAmount": {"currency": {"code": "EUR"}, "amount": 1000}}

        get_amount_transaction(transaction)

        _, kwargs = mocked_get.call_args
        assert kwargs["headers"] == {"apikey": ""}
