import csv
from typing import IO, List, Dict

from src.csv_utils.consts import EMPTY_CSV_ROW
from src.flight_file_process.time_utils import get_minutes_from_midnight

# TODO consider using a more oop structure, e.g. csv reader inherits from io reader, e.g. class that represents column


def get_file_line_dicts(file: IO) -> List[Dict]:
    file_dict = read_csv(file)
    sort_file_dict(file_dict)
    return file_dict


def sort_file_dict(file_dict: List[Dict]):
    file_dict.sort(key=lambda row: get_minutes_from_midnight(row[' Arrival']))
    return file_dict


def read_csv(file: IO) -> List[Dict]:
    reader = csv.DictReader(file)
    return [row for row in reader]


def write_list_to_csv(csv_list: List[Dict], file: IO):
    writer = csv.DictWriter(file, EMPTY_CSV_ROW.keys())
    writer.writeheader()
    writer.writerows(csv_list)