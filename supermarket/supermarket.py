# -*- coding: utf-8 -*-

#  pip install pymysql --proxy http://proxy1.xx.xx:8080 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

import sys, json, xlrd, pinyin, pymysql

class Supermarket(object):
	def __init__(self, env):
		super(Supermarket, self).__init__()
		with open('configs/config-' + env + '.json', encoding = 'utf-8') as f:
			config = json.load(f)
			self.jdbc = config['jdbc']
			self.action = config['action']

	def run(self):
		self.load()
		# print(self.categorys())

	def load(self):
		wb = xlrd.open_workbook('sources/data-2019.10.31.xlsx')
		for si in range(wb.nsheets):
			sh = wb.sheet_by_index(si)
			# jiushui, liangyou, niunai, roudan, sushi
			print(sh.name, len(sh.name), pinyin.get(sh.name, format = 'strip'))

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

	def upload(self):
		pass

	def save(self):
		pass

if __name__ == '__main__':
	env = sys.argv[1:]
	if env:
		env = env[0]
	else:
		env = 'test'

	print('The data import environment is: %s' % env)

	Supermarket(env).run()
