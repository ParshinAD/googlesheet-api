# googlesheet-api

googlesheet-api is a Python app for parsing data from google sheet into PostgresSQL. Data form database then used by django in its single page web application.

Main script start two proccess in parallel.
  
  1) parser from google sheet into PostgresSQL.
  
  2) start small djago app.
  
google sheet link:

https://docs.google.com/spreadsheets/d/1nwKGU-Dve1YzQIRV2bhRZ--1n5oDT_IjW15zH-61fcs/edit#gid=0

**django link**:

http://localhost:8000/gsapi/test2/


## Downloading

Use the git manager to download googlesheet-api.

```bash
git clone https://github.com/ParshinAD/googlesheet-api.git
```

download all packages

```bash
cd googlesheet-api
pip install -r requirements.txt
```

### edit config.py

1) edit username, password, port and database_name from your PostgreSQL.

    a. db_name: the name of the database that you want to connect.

    b. user: the username used to authenticate.

    c. password: password used to authenticate.

    d. host: database server address e.g., localhost or an IP address. default = '127.0.0.1'

    e. port: the port number. Default = 5432.

2) edit telegram api_id, api_hash: https://core.telegram.org/api/obtaining_api_id

and user_id: https://www.alphr.com/telegram-find-user-id/

## Start main program

```bash
python main.py
```

## telegram notification

if an entry with today appears in the table, you will receive a telegram notification.

# Contacts

with all questions write to the mail: aparshin01@mail.ru
