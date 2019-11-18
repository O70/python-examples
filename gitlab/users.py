# -*- coding: utf-8 -*-

import requests, json

# private_token

# 70 root
HEADERS = { 'PRIVATE-TOKEN': 'TEoi3qgzkem7E4Gx4JE1' }
# 70 Guiwang
# HEADERS = { 'PRIVATE-TOKEN': 'yutBj4yFUJKDdKs7kKxZ' }

# 77 root
# HEADERS = { 'PRIVATE-TOKEN': '9abAzt2BGy_-T5ev_BW8' }

# 50 root
# HEADERS = { 'PRIVATE-TOKEN': '9ysgzsRULvzMEYdB5p_g' }

class Users(object):
	def __init__(self):
		super(Users, self).__init__()

	def run(self):
		# sort/order_by当前版本不提供
		# params = {
		# 	'sort': 'asc',
		# 	'order_by': 'id',
		# 	'per_page': 50
		# }
		url = 'http://10.27.213.70/api/v4/users'
		# url = 'http://10.122.163.77/api/v4/users'
		# url = 'http://11.11.141.50/api/v4/users'
		resp = requests.get(url, headers = HEADERS, params = { 'per_page': 50 })

		users = sorted(resp.json(), key = lambda x:x['id'], reverse = False)

		# for user in users:
		# 	print(user.get('id'), user.get('username'), user.get('name'))

		print('Total: ', len(users))

		with open('tmp/users.json', 'w', encoding = 'UTF-8') as f:
			json.dump(users, f, sort_keys = False, indent = 2, ensure_ascii = False)

		gw = users[1]
		print((gw.get('is_admin')))
		print(type(gw.get('is_admin')))
		data = {
			'email': gw.get('email'),
			'password': '11111111',
			'username': gw.get('username'),
			'name': gw.get('name'),
			'skype': gw.get('skype'),
			'linkedin ': gw.get('linkedin '),
			'twitter': gw.get('twitter'),
			'website_url': gw.get('website_url'),
			'organization': gw.get('organization'),
			'bio': gw.get('bio'),
			'location': gw.get('location'),
			'admin': gw.get('is_admin'),
			'skip_confirmation': True
		}

		resp2 = requests.delete('http://10.122.163.77/api/v4/users/12?hard_delete=true',
			headers = { 'PRIVATE-TOKEN': '9abAzt2BGy_-T5ev_BW8' })
		print(resp2.text)

		# resp1 = requests.post('http://10.122.163.77/api/v4/users', 
		# 	headers = { 'PRIVATE-TOKEN': '9abAzt2BGy_-T5ev_BW8' }, data = data)
		# print(resp1.text)

if __name__ == '__main__':
	Users().run()
