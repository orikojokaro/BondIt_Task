from pathlib import Path

CSV_NAME = 'flights.csv'
CSV_FOLDER = 'flights'
FLIGHT_ID_COLUMN = 'flight ID'
ARRIVAL_COLUMN = ' Arrival' # TODO fix these
DEPARTURE_COLUMN = ' Departure ' # TODO consider using the field names from the csv file directly, or have a quick way to add more
SUCCESS_COLUMN = ' success'
CSV_PATH = Path().absolute().parent.parent / CSV_FOLDER / CSV_NAME