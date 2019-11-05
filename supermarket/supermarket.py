# -*- coding: utf-8 -*-

#  pip install pymysql --proxy http://proxy1.xx.xx:8080 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

import sys, os, json, xlrd, pinyin, pymysql

class Supermarket(object):
	def __init__(self, env):
		super(Supermarket, self).__init__()
		with open('configs/config-' + env + '.json', encoding = 'utf-8') as f:
			config = json.load(f)
			self.jdbc = config['jdbc']
			self.action = config['action']

	def run(self):
		imgs = self.loadImg()
		self.loadData(imgs)

		# self.load()
		# print(self.categorys())

	def loadImg(self):
		# jiushui, liangyou, niunai, roudan, sushi

		results = {}
		dirpath = 'sources/imgs/'
		imgs = os.listdir(dirpath)
		print('Total images: %d.' % len(imgs))

		for img in imgs:
			results[img.split('_')[0]] = '%s%s' % (dirpath, img)

		return results

	def loadData(self, imgs):
		wb = xlrd.open_workbook('sources/data-2019.10.31.xlsx')
		total = 0
		for si in range(wb.nsheets):
			sh = wb.sheet_by_index(si)
			rows = sh.nrows - 2
			total += rows
			print('*********************** %s: %d rows ***********************' % (sh.name, rows))
			for ri in range(2, sh.nrows):
				ind = int(sh.cell_value(ri, 0))
				name = sh.cell_value(ri, 1).strip()
				imgpath = None
				try:
					imgpath = imgs['%s%d' % (pinyin.get(sh.name[:2], format = 'strip'), ind)]
				except Exception as e:
					print('Image not found: %s' % name)

				print(name, imgpath)

		print('Total: %d rows.' % total)

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
