import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
import re, sys

string = 'tempsnv@grove.co,Temp NV Group,,True,02s8eyo10ia4o8b,,,10,"arendich@grove.co \n bsmith@grove.co \n dreifschneider@grove.co \n ",0,,0,,NONE,NONE,false,NONE,OWNERS_AND_MANAGERS,NONE,CAN_REQUEST_TO_JOIN,NONE,NONE,NONE,OWNERS_AND_MANAGERS,,NONE,ALL_IN_DOMAIN_CAN_VIEW,false,NONE,false,ALL_MEMBERS_CAN_DISCOVER,NONE,,true,false,NONE,NONE,true,false,NONE,true,NONE,NONE,false,NONE,REPLY_TO_IGNORE,,MODERATE_NONE,false,ANYONE_CAN_CONTACT,DEFAULT_FONT,ALL_MEMBERS_CAN_LEAVE,ALL_MANAGERS_CAN_ADD,NONE,ANYONE_CAN_POST,NONE,NONE,ALL_MANAGERS_CAN_INVITE,ALL_MANAGERS_CAN_APPROVE,MODERATE,false,OWNERS_AND_MANAGERS,NONE,ALL_IN_DOMAIN_CAN_VIEW,false,NONE,26214400,,false,NONE \n tempspa@grove.co,Grove Temp PA Group,,True,026in1rg4br6xt8,,,10,"arendich@grove.co \n hwong@grove.co \n ",0,,0,,NONE,NONE,false,NONE,OWNERS_AND_MANAGERS,NONE,CAN_REQUEST_TO_JOIN,NONE,NONE,NONE,OWNERS_AND_MANAGERS,,NONE,ALL_IN_DOMAIN_CAN_VIEW,false,NONE,false,ALL_MEMBERS_CAN_DISCOVER,NONE,,true,false,NONE,NONE,true,false,NONE,true,NONE,NONE,false,NONE,REPLY_TO_IGNORE,,MODERATE_NONE,false,ANYONE_CAN_CONTACT,DEFAULT_FONT,ALL_MEMBERS_CAN_LEAVE,ALL_MANAGERS_CAN_ADD,NONE,ANYONE_CAN_POST,NONE,NONE,ALL_MANAGERS_CAN_INVITE,ALL_MANAGERS_CAN_APPROVE,MODERATE,false,OWNERS_AND_MANAGERS,NONE,ALL_IN_DOMAIN_CAN_VIEW,false,NONE,26214400,,false,NONE'

matches = re.findall(r'\"(.+?)\"',string)  # match text between two quotes
print(matches)
for m in matches:
  string = string.replace('\"%s\"' % m, '%s\"%s\"%s' % ('"', m.replace("\n",":") , '"'))  # override text to include tags


print( string )
# group_rows = string.splitlines()
# print( group_rows )
sys.exit()

if sys.argv[-1] == 'tab':
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

	gc = gspread.authorize(credentials)

	# get spreadsheet from url
	# sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Vs_NHVBPpHcWayKXalUY-gthJheOdx4WwgvMTz-TpD0')
	# get spreadsheet form key
	sht1 = gc.open_by_key('1Vs_NHVBPpHcWayKXalUY-gthJheOdx4WwgvMTz-TpD0')

	if sys.argv[-2] == "googleusers" :	

		users = os.popen('./gam print users allfields').read()

		users_rows = users.splitlines()

		users_cell =[]
		for row in users_rows:
		    users_cell.append(row.split(","))

		sheet_name = "googleusers"

		sht1.values_update(
		    sheet_name+'!A1', 
		    params={'valueInputOption': 'RAW'}, 
		    body={'values': users_cell}
		)
		print("Added Successfully")		
	if sys.argv[-2] == "googleadmin" :

		admins = os.popen('./gam print admins').read()

		admin_rows = admins.splitlines()

		admin_cell =[]
		for row in admin_rows:
		    admin_cell.append(row.split(","))

		sheet_name = "googleadmins"

		sht1.values_update(
		    sheet_name+'!A1', 
		    params={'valueInputOption': 'RAW'}, 
		    body={'values': admin_cell}
		)
		print("Added Successfully")		
	if sys.argv[-2] == "googleloginfailures" :

		login_failure = os.popen('./gam report login | grep login_failure').read()

		login_failure_rows = login_failure.splitlines()

		login_failure_cell =[]
		for row in login_failure_rows:
		    login_failure_cell.append(row.split(","))

		sheet_name = "googleloginfailures"

		sht1.values_update(
		    sheet_name+'!A1', 
		    params={'valueInputOption': 'RAW'}, 
		    body={'values': login_failure_cell}
		)
		print("Added Successfully")		
	if sys.argv[-2] == "googlegroups" :

		groups = os.popen('./gam print groups name description admincreated id aliases members owners managers settings').read()

		group_rows = groups.splitlines()

		group_cell =[]
		for row in group_rows:
		    group_cell.append(row.split(","))

		sheet_name = "googlegroups"

		sht1.values_update(
		    sheet_name+'!A1', 
		    params={'valueInputOption': 'RAW'}, 
		    body={'values': group_cell}
		)
		print("Added Successfully")									
else :
	print("wrong argument")
