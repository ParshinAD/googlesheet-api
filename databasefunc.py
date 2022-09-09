import psycopg2


# create table if not exist
def create_table_test(connection):
    '''
    Create test table in current connection
    :param connection: psycopg2.extensions.connection
    :return: None
    '''
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE test(
                   id SMALLINT PRIMARY KEY,
                   order_num numeric(16,0),
                   price_usd numeric(16,2),
                   delivery_date date,
                   price_rub numeric(16,2));'''
            )
            connection.commit()
            print('[INFO] Table created successfully')
    except psycopg2.errors.DuplicateTable:
        print('[INFO] Table already exist')


def insert_new_data_test(connection, data, skip_first_row=True):
    '''
    Insert rows to test table
    :param connection: psycopg2.extensions.connection
    :param data: list[list(id, order_num, price_usd, delivery_date, price_rub)] to insert
    :param skip_first_row: bool param to skip first row in data
    :return: None
    '''
    with connection.cursor() as cursor:
        for value in data[skip_first_row:]:
            cursor.execute(
                f"""INSERT INTO test (id, order_num, price_usd, delivery_date, price_rub) VALUES
                ({value.id}, {value.order_num}, {value.price_usd}, '{value.delivery_date}', {value.price_rub});"""
            )
            connection.commit()
        print('[INFO] Successful insert')


def drop_table_test(connection):
    '''
    drop test table
    :param connection: psycopg2.extensions.connection
    :return: None
    '''
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS test")
        connection.commit()
        print("[INFO] Table dropped... ")


def get_all_test(connection, fields='*'):
    '''
    Returns all rows of the given fields
    :param connection: psycopg2.extensions.connection
    :param fields: fields to select, '*' by default
    :return: list[list]
    '''
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT {fields} from test ORDER BY id;"""
        )
        return cursor.fetchall()


def get_single_value(connection, pk):
    '''
    Returns single rows from test table with id=pk
    :param connection: psycopg2.extensions.connection
    :param pk: int|str, object primary key
    :return: list
    '''
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT * 
                FROM test 
                WHERE id = {pk};"""
        )
        return cursor.fetchone()


def update_value_test(connection, row):
    '''
    Update row in test table
    :param connection: psycopg2.extensions.connection
    :param row: list, data to update
    :return: None
    '''
    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE test
                SET order_num = {row.order_num},
                    price_usd = {row.price_usd},
                    delivery_date = '{row.delivery_date}',
                    price_rub = {row.price_rub}
                WHERE id = {row.id};"""
        )
        connection.commit()
        print('[INFO] Update Successfully')


def delete_value_test(connection, key_list):
    '''
    Delete keys from test table
    :param connection: psycopg2.extensions.connection
    :param key_list: list[int|str] to delete
    :return: None
    '''
    with connection.cursor() as cursor:
        if len(key_list) == 1:
            cursor.execute(
                f'''DELETE FROM test
                        WHERE id = {list(key_list)[0]};'''
            )
        else:
            cursor.execute(
                f'''DELETE FROM test
                        WHERE id in {tuple(key_list)};'''
            )
        print('[INFO] DELETE Successfully')
        connection.commit()