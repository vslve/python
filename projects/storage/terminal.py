import time
import re

from storage import Storage


class StorageTerminal:

    def __init__(self, storage: Storage, input_time_format: str, storage_time_format: str):
        self.__storage = storage
        self.__input_time_format = input_time_format
        self.__storage_time_format = storage_time_format

    @property
    def storage(self) -> Storage:
        return self.__storage

    @storage.setter
    def storage(self, storage: Storage):
        self.__storage = storage

    @property
    def input_time_format(self):
        return self.__input_time_format

    @input_time_format.setter
    def input_time_format(self, time_format: str):
        self.__input_time_format = time_format

    @property
    def storage_time_format(self):
        return self.__storage_time_format

    @storage_time_format.setter
    def storage_time_format(self, time_format: str):
        self.__storage_time_format = time_format

    def check_time_format(self, u_time: str) -> bool:
        return re.fullmatch(self.__input_time_format, u_time) and \
               0 <= int(u_time[:2]) <= 23 and 0 <= int(u_time[3:]) <= 59

    def check_time(self, start_time: str, end_time: str) -> bool:
        return self.check_time_format(start_time) and self.check_time_format(end_time) \
               and self.transform_to_storage_time_format(start_time) < self.transform_to_storage_time_format(end_time)

    def transform_to_storage_time_format(self, datetime: str) -> time.struct_time:
        return time.strptime(datetime, self.__storage_time_format)

    def run_storage(self):
        while True:
            last_name, start_time, end_time = self.get_client_data()

            if not self.storage.reserve_cell(
                    last_name,
                    self.transform_to_storage_time_format(start_time),
                    self.transform_to_storage_time_format(end_time)
            ):
                print("There are no empty cells in storage in this time. Choose another time")

    def get_client_data(self) -> tuple:
        while True:
            try:
                last_name, start_time, end_time = re.split(r'\s+', input(
                    "To reserve storage cell enter last name, 'from' time and 'to' time (lastname hh:mm hh:mm):\n"
                ))
            except ValueError:
                print('Incorrect input')
                continue
            if not self.check_last_name_format(last_name):
                print('Incorrect last name format')
                continue
            if not self.check_time(start_time, end_time):
                print('Incorrect time')
                continue
            return last_name, start_time, end_time

    @staticmethod
    def check_last_name_format(last_name: str) -> bool:
        return not (' ' in last_name or len(last_name) > 20)

    @staticmethod
    def get_cell_count() -> int:
        while True:
            try:
                count = int(input('Enter storage cell count:\n'))
                if count < 1:
                    raise ValueError
            except ValueError:
                print('Incorrect value')
                continue
            return count








