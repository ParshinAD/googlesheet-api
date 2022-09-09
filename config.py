# database config

# set True if you use PostgreSQL on your local machine, or false if you use PostgreSQL on docker with Web UI
local_db = True
docker_web_db = not local_db

if local_db:
    host = '127.0.0.1'
elif docker_web_db:
    host = '192.168.99.100' # ip my virtual box ip.  Maybe you can use '0.0.0.0'

user = 'postgres'
password = '4RYmCKKF'
db_name = 'test' #test

# get your api_id, api_hash, token
# from telegram as described above
api_id = '14639662'
api_hash = 'fb9d92c11cd69484e8b6f4fde42cb95b'
token = '5779514133:AAExiEfFZXUsKWTdKKqKvBB84k0qc7j5LfE'
phone = '+79258031664'
