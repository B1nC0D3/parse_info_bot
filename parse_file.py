import os

import pandas as pd


def get_file_data(path: str) -> dict:
    if not os.path.isfile(path):
        raise FileNotFoundError('Файл не найден')
    file_data = pd.read_excel(path).to_dict()
    try:
        file_data['name']
        file_data['URL']
        file_data['xpath']
    except KeyError:
        raise KeyError('неправильное заполнение файла либо он пуст, '
                       'заполните по шаблону')
    return file_data
