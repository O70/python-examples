# -*- coding: utf-8 -*-

#  pip install pymysql --proxy http://proxy1.xx.xx:8080 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

import sys, json, pymysql

env = sys.argv[1:]
if env:
	env = env[0]
else:
	env = 'test'

config = None
with open('configs/config-' + env + '.json', encoding = 'utf-8') as f:
	config = json.load(f)

connect = pymysql.connect(**config['jdbc'][0])

cursor = connect.cursor()

cursor.execute("SELECT id, name FROM base_dict WHERE PARENT_ID = \
	(SELECT id FROM base_dict WHERE code = 'SPLB') ORDER BY level_code")

categorys = {}
for row in cursor.fetchall():
	categorys[row[1]] = row[0]
print(categorys)

connect.close()
