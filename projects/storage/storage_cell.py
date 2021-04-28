import time


class StorageCell:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self, cell_id: int = count):
        self.__cell_id = cell_id
        self.__holder_last_name = None
        self.__start_time = None
        self.__end_time = None

    def is_free(self, start_time: str) -> bool:
        return self.__end_time is None or self.__end_time < time.strptime(start_time, '%H:%M')

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time: str):
        try:
            self.__start_time = time.strptime(start_time, '%H:%M')
        except ValueError:
            self.__start_time = None

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time: str):
        try:
            end_time = time.strptime(end_time, '%H:%M')
        except ValueError:
            self.__end_time = None
            return
        if self.__start_time is not None and self.__start_time < end_time:
            self.__end_time = end_time

    @property
    def holder_last_name(self):
        return self.__holder_last_name

    @holder_last_name.setter
    def holder_last_name(self, holder_last_name: str):
        self.__holder_last_name = holder_last_name

    @property
    def cell_id(self):
        return self.__cell_id
