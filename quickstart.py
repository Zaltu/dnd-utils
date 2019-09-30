from pprint import pprint as pp
import json
import gspread

from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)


gc = gspread.authorize(CREDENTIALS)

wrksht = gc.open("DriveTest").sheet1

lis = wrksht.col_values(1)

pp(lis)
