import json
from typing import List, Dict, Union

from flask import Flask, request

from src.csv_utils.consts import CSV_PATH, FLIGHT_ID_COLUMN, ARRIVAL_COLUMN, DEPARTURE_COLUMN, SUCCESS_COLUMN
from src.flight_file_process.process import handle_file_path

app = Flask(__name__)
# TODO consider re-reading every time instead of global var, e.g. to allow easy recovery if one update call fails in the middle
csv_list: List[Dict] = handle_file_path(CSV_PATH)


@app.get("/info/<string:flight_id>")
def get_flight_info(flight_id: str) -> Dict:
    return _get_flight_info(flight_id)


@app.post("/update")
def update_flights():
    # TODO consider performing input checks, e.g. valid json, valid schema, valid values
    flight_data: List[Dict] = request.json['flight_info']
    _update_flights(flight_data)
    return {'status': 'success'}


def _get_flight_info(flight_id: str) -> Dict[str, Union[str, None]]:
    """
    :return: A dict flight ifno, if flight_Id not found, values will be set to None
    """
    result_flight = {FLIGHT_ID_COLUMN: None, ARRIVAL_COLUMN: None, DEPARTURE_COLUMN: None, SUCCESS_COLUMN: None}
    for flight in csv_list:
        if flight[FLIGHT_ID_COLUMN] == flight_id:
            result_flight = flight
            break
    return result_flight


def _update_flights(flight_data: List[Dict]):
    global csv_list
    # TODO consider performing input check, e.g. arrival before departure
    csv_list.extend(flight_data)
    csv_list = handle_file_path(CSV_PATH, csv_list)


if __name__ == "__main__":
    app.run(debug=False)