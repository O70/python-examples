# -*- coding: utf-8 -*-

import xlrd, pinyin, requests

wb = xlrd.open_workbook('./users.xlsx')
sh = wb.sheet_by_index(0)

users = []
for rx in range(1, sh.nrows):
	name = sh.cell_value(rx, 0)
	email = sh.cell_value(rx, 1)
	card = sh.cell_value(rx, 2)
	username = pinyin.get(name, format = 'strip')
	password = username + card[-4:]
	print(name, username, email, card, password)
	users.append({
		'email': email,
		'username': username,
		'name': name,
		'password': password,
		'skip_confirmation': True	
	})

# curl -X POST --header 'Content-Type: application/json' 
# -d '{ "email": "xxx@yy.com", "username": "guiwang1", "name": "鬼王1", 
# "password": "11111111", "skip_confirmation": true }' 
# --header "PRIVATE-TOKEN: t7457anqRDFXQjj-fY8f" http://gitlab.riped.com/api/v4/users

for user in users:
	print(user)
	resp = requests.post('http://gitlab.riped.com/api/v4/users', 
		headers = { 'PRIVATE-TOKEN': 't7457anqRDFXQjj-fY8f' },
		data = user)
	print(resp)
	print('************************')
