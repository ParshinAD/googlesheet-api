from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
from typing import NamedTuple


class test_data(NamedTuple):
    id: int
    order_num: int
    price_usd: float
    delivery_date: str
    price_rub: float


def load_sheet():
    '''
    Downloads data from a google spreadsheet, adds a column "cost in rubles" and returns data and indexes
    :return: tuple(list, list)
    '''
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = 'keys.json'

    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1nwKGU-Dve1YzQIRV2bhRZ--1n5oDT_IjW15zH-61fcs'

    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Лист1!A1:D').execute()
    values = result.get('values', [])
    values, indexes = process_data(values)

    return values, indexes


def process_data(values):
    '''
    Parse dollar exchange rate, add a column "cost in rubles" and returns data and indexes
    :param values: data from google spreadsheet
    :return: tuple(list, list)
    '''
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    usd = data['Valute']['USD']['Value']
    values = tuple(test_data(*x, round(float(x[2]) * usd, 2)) for x in values[1:])
    indexes = tuple(map(lambda x: x[0], values))
    return values, indexes
