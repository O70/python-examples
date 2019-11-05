# -*- coding: utf-8 -*-

#  pip install pymysql --proxy http://proxy1.xx.xx:8080 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

import sys, os, json, xlrd, pinyin, uuid, datetime, pymysql

class Supermarket(object):
	def __init__(self, env):
		super(Supermarket, self).__init__()
		with open('configs/config-' + env + '.json', encoding = 'utf-8') as f:
			config = json.load(f)
			self.jdbc = config['jdbc']
			self.action = config['action']

	def run(self):
		imgs = self.loadImage()
		categorys = self.categorys()
		rows = self.assembly(imgs, categorys)
		self.inserts(rows)

	def loadImage(self):
		# jiushui, liangyou, niunai, roudan, sushi

		print('Start loading images...')

		results = {}
		dirpath = 'sources/imgs/'
		imgs = os.listdir(dirpath)
		print('Total images: %d.' % len(imgs))

		for img in imgs:
			results[img.split('_')[0]] = '%s%s' % (dirpath, img)

		print('End of image loading.')

		return results

	def assembly(self, imgs, categorys):
		print('Assembly data begins...')

		results = []

		wb = xlrd.open_workbook('sources/data-2019.10.31.xlsx')
		total = 0
		for si in range(wb.nsheets):
			sh = wb.sheet_by_index(si)
			rows = sh.nrows - 2
			total += rows

			category = categorys[sh.name]
			prefix = pinyin.get_initial(sh.name, '').upper()

			print('************* %s: %drows *************' % (sh.name, rows))
			for ri in range(2, sh.nrows):
				ind = int(sh.cell_value(ri, 0))
				name = sh.cell_value(ri, 1).strip()
				unit = sh.cell_value(ri, 2).strip()

				price = sh.cell_value(ri, 3)
				ptype = sh.row(ri)[3].ctype
				if ptype == 1:
					price = price.strip()
					yind = price.find('元')
					if yind != -1:
						price = float(price[:yind])
					else:
						price = 0.0
				elif ptype == 0:
					price = 0.0

				imgpath = None
				try:
					imgpath = imgs['%s%d' % (pinyin.get(sh.name[:2], format = 'strip'), ind)]
				except Exception as e:
					print('Image not found: %s(%s)' % (name, e))

				row = {
					'id': str(uuid.uuid1()).replace('-', ''),
					'numeration': '%s%06d' % (prefix, ind),
					'name': name,
					'img': imgpath,
					'price': price,
					'unit': unit,
					'specs': '%.2f/%s' % (price, unit),
					'amount': 0,
					'category': category,
					'enabled': 1,
					'create_by': 'admin',
					'create_time': datetime.datetime.now()
				}
				results.append(row)

		print('End of assembly data. Total: %d rows.' % total)

		return results

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

	def inserts(self, rows):
		isql = ('INSERT INTO tbl_goods (id, numeration, name, img, price, unit, '
			'specs, amount, category, enabled, create_by, create_time) VALUES '
			'(%(id)s, %(numeration)s, %(name)s, %(img)s, %(price)s, %(unit)s, %(specs)s, '
			'%(amount)s, %(category)s, %(enabled)s, %(create_by)s, %(create_time)s)')

		connect = pymysql.connect(**self.jdbc[1])
		cursor = connect.cursor()

		try:
			self.cleaning(cursor)

			ir = cursor.executemany(isql, rows)
			print('Insert %d rows.' % ir)
			connect.commit()
		except Exception as e:
			connect.rollback()
			print('Insert failed: ', e)

		connect.close()

	def cleaning(self, cursor):
		print('Start cleaning old data...')

		tables = ['tbl_goods', 'tbl_goods_cart', 'tbl_goods_order', 'tbl_goods_snapshot']

		for t in tables:
			c = cursor.execute('DELETE FROM %s' % t)
			print('Table[%s] has %d rows.' % (t, c))

		print('Clear end.')

if __name__ == '__main__':
	env = sys.argv[1:]
	if env:
		env = env[0]
	else:
		env = 'test'

	print('The data import environment is: %s' % env)

	Supermarket(env).run()
