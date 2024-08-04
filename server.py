from flask import Flask, jsonify
import pandas as pd
import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = Flask(__name__)

# Google Sheets API setup
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'  # Update this path
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of the spreadsheet.
SPREADSHEET_ID = 'your-spreadsheet-id'  # Update with your spreadsheet ID
RANGE_NAME = 'Sheet1!A1:Z1000'

service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

# Fetch data from Google Sheets
def fetch_data():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        return []

    df = pd.DataFrame(values[1:], columns=values[0])
    return df.to_dict(orient='records')

@app.route('/players', methods=['GET'])
def get_players():
    players = fetch_data()
    return jsonify(players)

if __name__ == '__main__':
    app.run(debug=True)
