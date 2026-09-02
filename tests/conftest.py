import pytest


@pytest.fixture
def info_cards():
    return [
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
        ('Счет 64686473678894779589', 'Счет **9589'),
        ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
        ('Счет 35383033474447895560', 'Счет **5560'),
        ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
        ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
        ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
        ('Счет 73654108430135874305', 'Счет **4305'),
        ('Счет 35805', 'Счет **5805')
    ]


@pytest.fixture
def invalid_info_cards():
    return [
        'Visa Gold Platinum 5999414228426353',
        '565432987',
        'Счет',
        ''
    ]


@pytest.fixture
def correct_format_dates():
    return [
        ("2024-03-11T02:26:18.671407", '11.03.2024'),
        ("1010-12-31T02:26:18", '31.12.1010'),
        ("0001-01-01T00:00:00", '01.01.0001'),
        ("9999-12-31T23:59:59", '31.12.9999')
        ]


@pytest.fixture
def data_dictionaries():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def data_dictionaries_sort_by_data_revers():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def data_dictionaries_with_same_date():
    return [
        {'id': 234567654, 'state': 'CANCELED', 'date': '2020-07-03T18:35:29.512364'},
        {'id': 88765433, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.fixture
def data_dictionaries_sort_by_date_with_same_date():
    return [
        {'id': 234567654, 'state': 'CANCELED', 'date': '2020-07-03T18:35:29.512364'},
        {'id': 88765433, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def data_dictionaries_sort_by_date_with_same_date_revers():
    return [
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2019-07-03T18:35:29.512364', 'id': 88765433, 'state': 'EXECUTED'},
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2020-07-03T18:35:29.512364', 'id': 234567654, 'state': 'CANCELED'}
    ]
