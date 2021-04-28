from storage_cell import StorageCell


class Storage:

    def __init__(self, size: int):
        self.__size = size if size > 0 else 0
        self.__storage = [StorageCell(i) for i in range(1, size + 1)]

    @property
    def size(self):
        return self.__size

    @property
    def storage(self):
        return self.__storage if self.__size > 0 else None



