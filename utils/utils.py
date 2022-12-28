import os
import json
import torch
import platform
from typing import List
from typing import Union
from csv import DictReader
from constants import FileKeys


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def get_text_list(data: List[dict]) -> List[str]:
    return [item[FileKeys.text_key] for item in data]


def load_json(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        data = json.load(f)
    return data


def load_text(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        data = f.read()
    return data


def save_json(
        file_path,
        data: Union[dict, list],
        encoding='utf-8'
        ) -> None:
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f)


def save_text(
        file_path,
        data: str,
        encoding='utf-8'
        ) -> None:
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(data)


def load_csv(
        file_path,
        encoding='utf-8',
        sep=','
        ):
    with open(file_path, 'r', encoding=encoding) as f:
        data = [*DictReader(f, delimiter=sep)]
    return data


def get_pad_mask(seq_len: int, pad_len: int):
    mask = [i < seq_len for i in range(seq_len + pad_len)]
    return torch.BoolTensor(mask)
