import psycopg2
from databasefunc import create_table_test, insert_new_data_test, drop_table_test, get_all_test, update_value_test, get_single_value, delete_value_test
from telegram_notice import order_to_notice, create_telegram_csv
from datetime import datetime
from Gsheets import load_sheet


def main_cycle(connection):
    '''
    Endless cycle to provide online data updates
    :param connection: psycopg2.extensions.connection
    :param data: tuple from load_data() func
    :param indexes:
    :return: None
    '''
    print('[INFO] start cycle')
    while True:
        data, indexes = load_sheet()
        # Checking for deleted fields
        db_indexes = (str(x[0]) for x in get_all_test(connection, 'id'))
        indexes_to_del = rows_to_del(indexes, db_indexes)

        if indexes_to_del:
            print('[INFO] Indexes to delete', indexes_to_del)
            delete_value_test(connection, indexes_to_del)

        # Checking for update and create fields
        update_and_create_rows(connection, data)

        # Order check for notifications
        order_to_notice(data)

        print('[INFO] Next iter')


def first_create(connection):
    '''
    Drop test table if exist and create new one
    :param connection: psycopg2.extensions.connection
    :return: None
    '''
    data, indexes = load_sheet()

    drop_table_test(connection)
    create_table_test(connection)

    # Create file for save already sent notifications
    create_telegram_csv()

    insert_new_data_test(connection, data)


def update_and_create_rows(connection, data):
    '''
    Checking the google sheet for updates or additions of data and save them in database
    :param connection: psycopg2.extensions.connection
    :param data: data list from google sheet
    :return:
    '''
    for value in data:
        # Query and compare one row for similarity and update it if something is different
        db_value = get_single_value(connection, value.id)
        if db_value:
            for i in [1, 2, 4]:
                if float(value[i]) != float(db_value[i]):
                    print(f'[INFO] change {value[i]} on {db_value[i]}')
                    update_value_test(connection, value)
            delivery_date = datetime.strptime(value.delivery_date, '%d.%m.%Y').date()
            if delivery_date != db_value[3]:
                print(f'[INFO] change {delivery_date} on {db_value[3]}')
                update_value_test(connection, value)
        else:
            # Or insert a line if it is new
            insert_new_data_test(connection, [value], skip_first_row=False)


def rows_to_del(sheet_indexes, db_indexes):
    '''
    Finds deleted lines
    :param sheet_indexes: list[str] indexes from google sheet
    :param db_indexes: generator[str] indexes from database
    :return: set[str]
    '''
    result = set(db_indexes) - set(sheet_indexes)
    return result
