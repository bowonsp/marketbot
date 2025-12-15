import os
import json
import gspread
from google.oauth2.service_account import Credentials

def main():
    creds_dict = json.loads(os.environ["GSHEET_CREDS"])
    sheet_url = os.environ["SHEET_URL"]

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url).sheet1
    sheet.update("A1", [["Bot is connected!"]])

if __name__ == "__main__":
    main()
