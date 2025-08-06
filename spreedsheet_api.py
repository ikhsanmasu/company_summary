from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from time import sleep

class SpreadsheetAPI:
    def __init__(self, spreadsheet_id = None, creds = None):
        self.spreadsheet_id = spreadsheet_id
        self.creds = creds

    def get_values(self, range_name):
        try:
            attempt = 5
            rows_result = ""

            while attempt and rows_result == "":
                print(f"get value from spreedsheet {range_name} attempt: {6 - attempt}")
                service = build("sheets", "v4", credentials=self.creds)
                result = service.spreadsheets().values().get(
                    spreadsheetId=self.spreadsheet_id,
                    range=range_name).execute()
                rows_result = result.get("values", [])
                # print(f"attempt: {6 - attempt} result: {rows_result}")
                attempt -= 1
                sleep(1)  # Wait for 1 second before retrying
            return [row[0] for row in rows_result]
        except HttpError as error:
            print(f"An error occurred: {error}")

    def write_value(self, range_name, value):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            body = {"values": [[value]]}
            result = service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption="USER_ENTERED",
                body=body,
            ).execute()

            print(f"Updated range: {result['updatedRange']}")
        except HttpError as error:
            print(f"An error occurred: {error}")
