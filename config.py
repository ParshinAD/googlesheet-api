# database config

user = 'user'
password = 'password'
db_name = 'db_name'
port = '5432'

# get your api_id, api_hash, token
# from telegram as described above
api_id = 'api_id'
api_hash = 'api_hash'
token = 'token'
phone = 'phone'
user_id = 'user_id'

# set True if you use PostgreSQL on your local machine, or false if you use PostgreSQL on docker with Web UI
# better use local_db = True
local_db = True
docker_web_db = not local_db

if local_db:
    host = '127.0.0.1'
elif docker_web_db:
    host = '192.168.99.100' # ip my virtual box ip.  Maybe you can use '0.0.0.0'

