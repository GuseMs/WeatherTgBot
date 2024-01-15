from datetime import datetime, timedelta


def generate_date_list(start, num_days: int):
    date_format = '%d-%m-%Y'

    start_datetime = datetime.strptime(start, date_format)

    date_list = [start_datetime + timedelta(days=i) for i in range(num_days)]

    formatted_date_list = [date.strftime(date_format) for date in date_list]

    return formatted_date_list