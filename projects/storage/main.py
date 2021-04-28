import re
import time

from storage import Storage


def check_last_name_format(last_name: str) -> bool:
    if ' ' in last_name or len(last_name) > 20:
        return False
    return True


def check_time_format(time: str) -> bool:
    if re.fullmatch(r'\d{2}:\d{2}', time) is None or 0 >= int(time[:2]) >= 23 or 0 >= int(time[3:]) >= 59:
        return False
    return True


def check_time(start_time: str, end_time: str) -> bool:
    return check_time_format(start_time) and check_time_format(end_time) \
           and time.strptime(start_time, '%H:%M') < time.strptime(end_time, '%H:%M')


def main():
    cell_count = int(input('Enter storage cell count:\n'))
    storage = Storage(cell_count).storage

    while True:
        while True:
            try:
                last_name, start_time, end_time = input('Enter last name and time(lastname hh:mm hh:mm):\n').split(' ')
            except ValueError:
                last_name, start_time, end_time = None, None, None
                print('Incorrect input')
                continue
            if not check_last_name_format(last_name):
                print('Incorrect last name format. Enter correct last name')
                continue
            if not check_time(start_time, end_time):
                print('Incorrect time format')
                continue
            break

        filled = False
        for cell in storage:
            if cell.is_free(start_time):
                cell.start_time = start_time
                cell.end_time = end_time
                cell.holder_last_name = last_name
                filled = True
                print(f'{cell.holder_last_name} {cell.cell_id}')
                break

        if not filled:
            print("There are no empty cells in storage in this time. Choose another time")


if __name__ == '__main__':
    main()
