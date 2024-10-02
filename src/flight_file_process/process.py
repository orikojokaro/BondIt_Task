from pathlib import Path
from typing import IO, Dict, List
import csv
CSV_NAME = 'flights.csv'
CSV_FOLDER = 'flights'
ARRIVAL_COLUMN = ' Arrival' # TODO fix these
DEPARTURE_COLUMN = ' Departure' # TODO consider using the field names from the csv file directly
SUCCESS_COLUMN = ' Success'
ARRIVAL_DEPARTURE_GAP_FOR_SUCCESS = 180
MAX_SUCCESS = 20  # TODO reorgenize consts
SUCCESS = 'success'
FAIL = 'fail'
def get_file_line_dicts(file: IO) -> List[Dict]:
    file_dict = read_csv(file)
    sort_file_dict(file_dict)
    return file_dict
def sort_file_dict(file_dict: List[Dict]):
    # TODO consider to use pandas or datetime
    file_dict.sort(key=lambda row: get_minutes_from_midnight(row[' Arrival'].strip()))
    return file_dict
def get_minutes_from_midnight(daytime: str):
    return int(daytime[0:2]) * 60 + int(daytime[3:])

def read_csv(file: IO) -> List[Dict]:
    return [row for row in csv.DictReader(file)]


def add_success_column(file: IO):
    file_dict = get_file_line_dicts(file)
    file_dict = _add_success_column_in_memory(file_dict)

def _add_success_column_in_memory(file_dict: List[Dict]) -> List[Dict]:
    num_success = 0
    for flight in file_dict:
        arrival = get_minutes_from_midnight(flight[ARRIVAL_COLUMN])
        departure = get_minutes_from_midnight(flight[DEPARTURE_COLUMN])
        if departure - arrival >= ARRIVAL_DEPARTURE_GAP_FOR_SUCCESS and num_success < MAX_SUCCESS:
            num_success += 1
            flight[SUCCESS_COLUMN] = SUCCESS
        else:
            flight[SUCCESS_COLUMN] = FAIL
    return file_dict

def handle_file(file_path: Path):
    with file_path.open() as f:
        add_success_column(f)


if __name__ == '__main__':
    handle_file(Path().absolute().parent.parent / CSV_FOLDER / CSV_NAME)