# -*- coding: utf-8 -*-

import requests, json

# API_PREFIX = 'http://11.8.42.56/cgi-bin'
# GET_TOKEN = '%s/gettoken?corpid=wl6e538311bc&corpsecret=an7DNwBzOTITHiccIkLQxoKG8PFNdT-OAkJwN4OpVbA' % API_PREFIX

# # print(API_PREFIX)
# # print(GET_TOKEN)
# access_token = requests.get(GET_TOKEN)
# print(access_token)
# print(access_token.encoding)
# print(access_token.text)
# print(type(access_token.text))
# print(access_token.json())
# print(type(access_token.json()))
# print(7200 / 60 / 60)
# print(access_token.raw)

host = 'http://localhost'
api_gettoken = '%s/cgi-bin/gettoken' % host
api_send = '%s/cgi-bin/message/send' % host
api_revoke = '%s/cgi-bin/message/revoke' % host

params_gettoken = {
	'corpid': 'wl6e538311bc',
	'corpsecret': 'an7DNwBzOTITHiccIkLQxoKG8PFNdT-OAkJwN4OpVbA'
}

res_token = requests.get(api_gettoken, params = params_gettoken)
print(res_token)
res_token_json = res_token.json()
print(res_token_json)


# print()

# res = requests.get('%s/cgi-bin/user/get' % host, params = {
# 	'access_token': res_token_json['access_token'],
# 	'userid': '362330199011185012'
# })
# print(res)
# print(res.json())

print()

# headers = { 'content-type': 'application/json' }
# headers = { 'content-type': 'application/x-www-form-urlencoded' }
params_send = {
	'access_token': res_token_json['access_token']
}
data_send = {
	'touser': '5734',
	'msgtype': 'text',
	'agentid': '1000285',
	'text': {
		'content': 'Send test'
	}
}

# # res_send = requests.post(api_send, headers = headers, params = params_send, data = data_send)
# res_send = requests.post(api_send, params = params_send, data = json.dumps(data_send))
# # res_send = requests.post(api_send, headers = headers, params = params_send, data = data_send)
# # res_send = requests.post(api_send + '?access_token='+res_token_json['access_token'], headers = headers, 
# 	# params = data_send)
# print(res_send)
# print(res_send.headers)
# res_send_json = res_send.json()
# print(res_send_json)

revoke_data = { 'jobid': '4_1612666843_917916' }
res_revoke = requests.post(api_revoke, params = params_send, data = json.dumps(revoke_data))
# res_revoke = requests.post(api_revoke, params = params_send, data = revoke_data)
print(res_revoke)
print(res_revoke.json())
