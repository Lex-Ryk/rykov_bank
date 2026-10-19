from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_data_transactions


print(get_data_transactions('data/operation.json'))
get_mask_card_number('35645365367')
get_mask_account('sf4655757')
