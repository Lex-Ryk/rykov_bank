from src.external_api import get_amount_transaction
from src.utils import get_data_transactions


transactions = get_data_transactions('data/operations.json')

print(get_amount_transaction(transactions[2]))
