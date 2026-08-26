def filter_by_state(list_dicts: list[dict], state: str='EXECUTED') -> list[dict]:
    new_list_dicts = []

    for one_dict in list_dicts:
        if one_dict['state'] == state:
            new_list_dicts.append(one_dict)

    return new_list_dicts
