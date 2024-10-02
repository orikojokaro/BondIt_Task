MINUTES_IN_HOUR = 60

def get_minutes_from_midnight(daytime: str) -> int:
    daytime = daytime.strip()
    return int(daytime[0:2]) * MINUTES_IN_HOUR + int(daytime[3:])
