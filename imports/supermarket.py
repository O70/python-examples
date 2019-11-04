# -*- coding: utf-8 -*-

#  pip install pymysql --proxy http://proxy1.xx.xx:8080 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

import json, pymysql

jdbc = None
with open('configs/jdbc-test.json', encoding = 'utf-8') as f:
	jdbc = json.load(f)

connect = pymysql.connect(**jdbc[0])

cursor = connect.cursor()

cursor.execute("SELECT id, name FROM base_dict WHERE PARENT_ID = \
	(SELECT id FROM base_dict WHERE code = 'SPLB') ORDER BY level_code")

categorys = {}
for row in cursor.fetchall():
	categorys[row[1]] = row[0]
print(categorys)

connect.close()
