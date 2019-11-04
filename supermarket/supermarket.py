# -*- coding: utf-8 -*-

#  pip install pymysql --proxy http://proxy1.xx.xx:8080 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

import sys, json, pymysql

# env = sys.argv[1:]
# if env:
# 	env = env[0]
# else:
# 	env = 'test'

# config = None
# with open('configs/config-' + env + '.json', encoding = 'utf-8') as f:
# 	config = json.load(f)

# connect = pymysql.connect(**config['jdbc'][0])

# cursor = connect.cursor()

# cursor.execute("SELECT id, name FROM base_dict WHERE PARENT_ID = \
# 	(SELECT id FROM base_dict WHERE code = 'SPLB') ORDER BY level_code")

# categorys = {}
# for row in cursor.fetchall():
# 	categorys[row[1]] = row[0]
# print(categorys)

# connect.close()

class Supermarket(object):
	def __init__(self, env):
		super(Supermarket, self).__init__()
		with open('configs/config-' + env + '.json', encoding = 'utf-8') as f:
			config = json.load(f)
			self.jdbc = config['jdbc']
			self.action = config['action']

	def categorys(self):
		connect = pymysql.connect(**self.jdbc[0])

		cursor = connect.cursor()

		cursor.execute("SELECT id, name FROM base_dict WHERE PARENT_ID = \
			(SELECT id FROM base_dict WHERE code = 'SPLB') ORDER BY level_code")

		categorys = {}
		for row in cursor.fetchall():
			categorys[row[1]] = row[0]

		connect.close()

		return categorys

if __name__ == '__main__':
	env = sys.argv[1:]
	if env:
		env = env[0]
	else:
		env = 'test'

	print('The data import environment is:', env)

	sm = Supermarket(env)
	print(sm.__class__)
	print(sm.__dict__)
	print(sm.categorys())
