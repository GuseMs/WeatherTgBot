import re


def extract_temperature(temperaturestr):
    match = re.search(r'(-?\d+)', temperaturestr)
    return int(match.group(1)) if match else None