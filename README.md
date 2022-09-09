# googlesheet-api

googlesheet-api is a Python app for parsing data from google sheet into PostgresSQL. Data form database then used by django in its single page web application.

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

1) edit username, password and database_name from your PostgreSQL
2) edit telegram api_id, api_hash: https://core.telegram.org/api/obtaining_api_id

## Start main program

```bash
python main.py
```


django link:
http://localhost:8000/gsapi/test2/
