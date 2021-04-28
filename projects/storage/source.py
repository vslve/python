import time
import re


def check_last_name_format(last_name: str) -> bool:
    return not (' ' in last_name or len(last_name) > 20)


def check_time_format(u_time: str) -> bool:
    return re.fullmatch(r'\d{2}:\d{2}', u_time) and \
            0 <= int(u_time[:2]) <= 23 and 0 <= int(u_time[3:]) <= 59


def check_time(start_time: str, end_time: str) -> bool:
    return check_time_format(start_time) and check_time_format(end_time) \
           and transform_to_datetime(start_time) < transform_to_datetime(end_time)


def get_cell_count() -> int:
    while True:
        try:
            count = int(input('Enter storage cell count:\n'))
        except ValueError:
            print('Incorrect value')
            continue
        return count


def get_client_data() -> tuple:
    while True:
        try:
            last_name, start_time, end_time = re.split(r'\s+', input(
                "To reserve storage cell enter last name, 'from' time and 'to' time (lastname hh:mm hh:mm):\n"
            ))
        except ValueError:
            print('Incorrect input')
            continue
        if not check_last_name_format(last_name):
            print('Incorrect last name format. Enter correct last name')
            continue
        if not check_time(start_time, end_time):
            print('Incorrect time format')
            continue
        return last_name, start_time, end_time


def transform_to_datetime(datetime: str) -> time.struct_time:
    return time.strptime(datetime, "%H:%M")


def reserve_storage_cell(storage: list, last_name: str, start_time: time.struct_time, end_time: time.struct_time) -> bool:
    reserved = False
    for cell in storage:
        if cell.is_free(start_time):
            cell.start_time = start_time
            cell.end_time = end_time
            cell.holder_last_name = last_name
            reserved = True
            print(f'{cell.holder_last_name} {cell.cell_id}')
            break
    return reserved
