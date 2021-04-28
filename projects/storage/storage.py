import time


class Storage:

    def __init__(self, size: int):
        self.__size: int = size if size > 0 else 0
        self.__storage: list = [Storage.StorageCell(i) for i in range(1, size + 1)]

    @property
    def size(self) -> int:
        return self.__size

    @property
    def storage(self) -> list:
        return self.__storage if self.__size > 0 else None

    class StorageCell:
        count = 0

        def __new__(cls, *args, **kwargs):
            cls.count += 1
            return super().__new__(cls)

        def __init__(self, cell_id: int = count):
            self.__cell_id: int = cell_id
            self.__holder_last_name: str or None = None
            self.__start_time: time.struct_time or None = None
            self.__end_time: time.struct_time or None = None

        def is_free(self, start_time: time.struct_time) -> bool:
            return self.__end_time is None or self.__end_time < start_time

        @property
        def start_time(self) -> time.struct_time:
            return self.__start_time

        @start_time.setter
        def start_time(self, start_time: time.struct_time):
            self.__start_time = start_time

        @property
        def end_time(self) -> time.struct_time:
            return self.__end_time

        @end_time.setter
        def end_time(self, end_time: time.struct_time):
            if self.__start_time is not None and self.__start_time < end_time:
                self.__end_time = end_time
            else:
                self.__end_time = None

        @property
        def holder_last_name(self) -> str:
            return self.__holder_last_name

        @holder_last_name.setter
        def holder_last_name(self, holder_last_name: str):
            self.__holder_last_name = holder_last_name

        @property
        def cell_id(self) -> int:
            return self.__cell_id
