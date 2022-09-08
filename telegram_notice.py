# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from datetime import date, datetime, timedelta
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from config import api_id, api_hash, token
import csv


def order_to_notice(data):
    '''
    Sends a telegram notification if a new order is overdue
    :param data: data list from google sheet
    :return: None
    '''
    for row in data:
        today = date.today()
        row_date = datetime.strptime(row[3], '%d.%m.%Y')
        if today == row_date.date():

            # Read already sended notifications
            with open('already_send.csv', 'r', encoding='utf8') as file:
                reader = csv.DictReader(file)
                id_dates = {val['id']: datetime.strptime(val['date'], '%d.%m.%Y') for val in reader}

            # check if a notification has been sent for this order yet, or if its date has changed to a newer one
            if (row[0] not in id_dates) or (id_dates[row[0]].date() != row_date.date()):
                send_telegram_notice(row[0])

                with open('already_send.csv', 'a', encoding='utf8') as file:
                    file.write(f'{row[0]},{row[3]}\n')


def send_telegram_notice(pk):
    '''
    send message on Telegram with f"overdue order №{pk}" text
    :param pk: int, order id
    :return: None
    '''
    message = f"overdue order №{pk}"

    # your phone number
    phone = '+79258031664'

    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient('session', api_id, api_hash)

    # connecting and building the session
    client.connect()

    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():
        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input('Enter the code: '))

    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        receiver = InputPeerUser(338994363, 0)

        # sending message using telegram client
        client.send_message(receiver, message, parse_mode='html')
    except Exception as e:

        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e)

    # disconnecting the telegram session
    client.disconnect()


def create_telegram_csv():
    with open('already_send.csv', 'w', encoding='utf8') as file:
        file.write(f'id,date\n')
