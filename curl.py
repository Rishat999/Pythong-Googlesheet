import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
import re, sys
import logging
import json
import xml.etree.ElementTree as ET

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)

# get spreadsheet from url
# sht1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Vs_NHVBPpHcWayKXalUY-gthJheOdx4WwgvMTz-TpD0')
# get spreadsheet form key
sht1 = gc.open_by_key('1Vs_NHVBPpHcWayKXalUY-gthJheOdx4WwgvMTz-TpD0')

if sys.argv[-1] == "bamboo" :		
	users = os.popen('curl -i -u "7ad1796799cb0fd6465178a661bb70e2f18aa449:x" "https://api.bamboohr.com/api/gateway.php/grovecollab/v1/employees/directory"').read()
		
	xml_data = users.split('<?xml version="1.0"?>')
	tree = ET.fromstring(xml_data[1])
	#logging.basicConfig(filename="logfilename.log", level=logging.INFO)
	#logging.info(xml_data[1])
	employees =[]
	fieldset = tree.find("fieldset")
	field = ['Employee ID']
	
	field.append(fieldset[0].text)	
	field.append(fieldset[1].text)	
	field.append(fieldset[2].text)	
	field.append(fieldset[3].text)	
	field.append(fieldset[4].text)	
	field.append(fieldset[5].text)	
	field.append(fieldset[6].text)	
	field.append(fieldset[7].text)	
	field.append(fieldset[8].text)	
	field.append(fieldset[9].text)	
	employees.append(field)

	root = tree.findall("*/employee")	
	
	for elem in root:
		employee = []  
		employee.append( elem.attrib['id'] )
		employee.append( elem[0].text )
		employee.append( elem[1].text )
		employee.append( elem[2].text )
		employee.append( elem[3].text )
		employee.append( elem[4].text )
		employee.append( elem[5].text )
		employee.append( elem[6].text )
		employee.append( elem[7].text )
		employee.append( elem[8].text )
		employee.append( elem[9].text )
		employees.append(employee)
	
	sheet_name = "bamboo"

	sht1.values_update(
		sheet_name+'!A1', 
		params={'valueInputOption': 'RAW'}, 
		body={'values': employees}
	)
	print("Added Successfully")		
								
else :
	print("wrong argument")
