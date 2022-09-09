import psycopg2
from config import host, user, password, db_name
from cycle import main_cycle, first_create
import os
import multiprocessing


def django_app():
    print('[INFO] Start django app')
    os.system("python django/django-postgres/postgresTest/manage.py runserver")


def main():
    print('[INFO] Start main app')
    # flag to drop table if exist and create new one
    create = True
    connection = ''

    try:
        # Connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
        )

        if create:
            first_create(connection)

        # Start endless cycle
        main_cycle(connection)

    except Exception as ex:
        print('Error while working', type(ex), ex)
        raise
    finally:
        if connection:
            connection.close()
            print('Connection closed')


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=django_app)
    process2 = multiprocessing.Process(target=main)
    # starting google sheet parser
    process2.start()
    # starting django app
    process1.start()
