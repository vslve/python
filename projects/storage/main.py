from storage import Storage
from terminal import StorageTerminal


def main():

    terminal = StorageTerminal(
        Storage(StorageTerminal.get_cell_count()),
        r'\d{2}:\d{2}',
        "%H:%M"
    )
    terminal.run_storage()


if __name__ == '__main__':
    main()
