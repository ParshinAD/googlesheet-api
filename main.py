import psycopg2
from config import host, user, password, db_name
from cycle import main_cycle, first_create


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