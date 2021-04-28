from storage import Storage
import source as s


def main():
    cell_count = s.get_cell_count()
    storage = Storage(cell_count).storage

    while True:
        last_name, start_time, end_time = s.get_client_data()

        if not s.reserve_storage_cell(
                storage,
                last_name,
                s.transform_to_datetime(start_time),
                s.transform_to_datetime(end_time)
        ):
            print("There are no empty cells in storage in this time. Choose another time")


if __name__ == '__main__':
    main()
