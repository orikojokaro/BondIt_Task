from pathlib import Path
from typing import Dict, List, Union
from src.csv_utils.consts import SUCCESS_COLUMN, ARRIVAL_COLUMN, DEPARTURE_COLUMN, CSV_PATH
from src.csv_utils.csv_utils import get_file_line_dicts, write_list_to_csv
from src.flight_file_process.consts import SUCCESS, FAIL, ARRIVAL_DEPARTURE_GAP_FOR_SUCCESS, MAX_SUCCESS
from src.flight_file_process.time_utils import get_minutes_from_midnight


def handle_file_path(file_path: Path, csv_list: Union[None, List[Dict]]=None) -> List[Dict]:
    """
    Read the csv, sort it, set the success values, overwrite the result
    :param csv_list: optional, instead of reading the csv list from the file_path,
        use the given csv_list and update the file_path
    """
    if csv_list is None:
        with file_path.open() as file:
            csv_list = get_file_line_dicts(file)
    csv_list = _add_success_column(csv_list)
    with file_path.open('w') as file:
        write_list_to_csv(csv_list, file)
    return csv_list


def _add_success_column(file_dict: List[Dict]) -> List[Dict]:
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


if __name__ == '__main__':
    handle_file_path(CSV_PATH)