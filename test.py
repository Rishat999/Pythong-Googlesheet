#!/usr/bin/python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('sheets-api.json', scope)

gc = gspread.authorize(credentials)








sh = gc.open_by_key('1Vs_NHVBPpHcWayKXalUY-gthJheOdx4WwgvMTz-TpD0')


worksheet = sh.worksheet("googleusers")

val = worksheet.acell('A1').value

print val

#worksheet.update_acell('H1', 'Bingo!')


#worksheet = sh.Users

#wks = gc.open("Cyber Risk - Template").Users

#wks.update_acell('H2', "it's down there somewhere, let me take another look.")

#val = worksheet.acell('G2').value


