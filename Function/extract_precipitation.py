import re

def extract_precipitation(s):
    match = re.search(r'(-?\d+(\.\d+)?)', s)
    return float(match.group(1)) if match else float(0)