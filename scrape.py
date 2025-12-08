import os, gspread, pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import requests

def main():
    creds = json.loads(os.environ['GSHEET_CREDS'])
    sheet_url = os.environ['SHEET_URL']

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_dict(creds, scope))
    sheet = client.open_by_url(sheet_url).sheet1

    sheet.update('A1', 'Bot is connected!')
if __name__=='__main__':
    main()
