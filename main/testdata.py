import datetime


def_time = '21:11:2022 09:23'

datasets_short = [
    {'id': 0, 'name': 'some_dataset', 'quality': 100, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 1, 'name': 'some_dataset', 'quality': 50, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 2, 'name': 'some_dataset', 'quality': 70, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 3, 'name': 'some_dataset', 'quality': 100, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 4, 'name': 'some_dataset', 'quality': 100, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 5, 'name': 'some_dataset', 'quality': 100, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 6, 'name': 'some_dataset', 'quality': 32, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
    {'id': 7, 'name': 'some_dataset', 'quality': 90, 'actuality': 34, 'value': 50, 'row_count': 34, 'field_count': 3, 'last_load': def_time, 'tags': ['factory', 'vtb']},
]

datasets = [
    {'Quality': 100, 
    'Actuality': 34, 
    'value': 50, 
    'row_count': 34, 
    'field_count': 3, 
    'last_load': def_time,
    'tags': ['factory', 'vtb'], 
    'rows': [''],
    'structure': ['id', 'name', 'age', 'email'],
    'sample_data': [
            {'id': 1, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
            {'id': 2, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
            {'id': 3, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
            {'id': 4, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
            {'id': 5, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
            {'id': 6, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
            {'id': 7, 'name': 'Nikita', 'age': 18, 'email': 'nikita@email.com'},
        ],
    }
]
