from pathlib import Path

CSV_NAME = 'flights.csv'
CSV_FOLDER = 'flights'
FLIGHT_ID_COLUMN = 'flight ID'
ARRIVAL_COLUMN = ' Arrival'
DEPARTURE_COLUMN = ' Departure '
SUCCESS_COLUMN = ' success'
EMPTY_CSV_ROW = {FLIGHT_ID_COLUMN: None, ARRIVAL_COLUMN: None, DEPARTURE_COLUMN: None, SUCCESS_COLUMN: None}
CSV_PATH = Path(__file__).resolve().parent / CSV_FOLDER / CSV_NAME
