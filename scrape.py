import os
import json
import gspread
import pandas as pd
import requests
from google.oauth2.service_account import Credentials

def main():
    # Ambil creds dari GitHub Secrets
    creds_dict = json.loads(os.environ['GSHEET_CREDS'])
    sheet_url = os.environ['SHEET_URL']

    # Scope Google Sheets
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Buat credential (VERSI BARU)
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=scope
    )

    # Authorize gspread
    client = gspread.authorize(creds)

    # Akses sheet
    sheet = client.open_by_url(sheet_url).sheet1

    # Test update
    sheet.update('A1', [['Bot is connected!']])

    print("✅ Google Sheet connected successfully")

if __name__ == "__main__":
    main()
