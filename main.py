from src import masks

card_number: str = input()
account_number: str = input()

print(masks.get_mask_card_number(card_number))
print(masks.get_mask_account(account_number))
