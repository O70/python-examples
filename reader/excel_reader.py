# -*- coding: utf-8 -*-

import xlrd, pinyin, uuid, json, re, requests, os, zipfile

import xml.dom.minidom as xmldom

sql_prefix = 'INSERT INTO base_dict (id, code, name, parent_id, enabled, remark, deleted, spell, initials, level_code) VALUE'

# ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

def read_building():
	wb = xlrd.open_workbook('temp/building.xlsx')
	sh = wb.sheet_by_index(0)

	rid = str(uuid.uuid1()).replace('-', '')
	rname = '院区建筑'
	rcode = '000001000088'

	print(sql_prefix)
	print('(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\'){}'.format(
		rid, pinyin.get_initial(rname, '').upper(), 
		rname, '402881e6415444f6014154db5e150000', '1', rname, '0', 
		pinyin.get(rname, format = 'strip'), pinyin.get_initial(rname, ''), rcode, ','))

	for rx in range(2, sh.nrows):
		cname = sh.cell_value(rx, 1)
		clay = int(sh.cell_value(rx, 3))
		remark = '共%d层' % clay
		if sh.row(rx)[2].ctype != 0:
			remark = '%s[%s]' % (sh.row(rx)[2].value, remark)

		print('(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\'),'.format(
			str(uuid.uuid1()).replace('-', ''), pinyin.get_initial(cname, '').upper(), 
			cname, rid, '1', remark, '0', pinyin.get(cname, format = 'strip'), 
			pinyin.get_initial(cname, ''), rcode + ('%06d' % (rx - 1))))

def read_category():
	wb = xlrd.open_workbook('temp/goods-list.xlsx')

	rid = str(uuid.uuid1()).replace('-', '')
	rname = '商品类别'
	rcode = '000001000089'

	print(sql_prefix)
	print('(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\'){}'.format(
		rid, pinyin.get_initial(rname, '').upper(), 
		rname, '402881e6415444f6014154db5e150000', '1', rname, '0', 
		pinyin.get(rname, format = 'strip'), pinyin.get_initial(rname, ''), rcode, ','))

	for s in range(wb.nsheets):
		sh = wb.sheet_by_index(s)
		print('(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\'),'.format(
			str(uuid.uuid1()).replace('-', ''), pinyin.get_initial(sh.name, '').upper(), 
			sh.name, rid, '1', sh.name, '0', pinyin.get(sh.name, format = 'strip'), 
			pinyin.get_initial(sh.name, ''), rcode + ('%06d' % (s + 1))))

# read_building()
# read_category()

lists = []
def read_goods():
	categorys = { 
		'商品类别': '3e241446adb611e98258000ec6c11a0e', 
		'水果': '3e24b09eadb611e98196000ec6c11a0e', 
		'粮油副食': '3e24b09fadb611e9b163000ec6c11a0e', 
		'成品菜': '3e24b0a0adb611e994da000ec6c11a0e', 
		'肉蛋水产': '3e24b0a1adb611e9ae17000ec6c11a0e', 
		'速食零食': '3e24b0a2adb611e9b7e3000ec6c11a0e', 
		'牛奶冰品': '3e24b0a3adb611e9984b000ec6c11a0e', 
		'酒水饮料': '3e24b0a4adb611e9a1c7000ec6c11a0e' 
	}

	datas = {}

	wb = xlrd.open_workbook('temp/goods-list.xlsx')
	for i in range(wb.nsheets):
		sh = wb.sheet_by_index(i)
		datas[sh.name] = []
		numer_perfix = pinyin.get_initial(sh.name, '').upper()

		for rx in range(2, sh.nrows):
			if sh.row(rx)[0].ctype != 0:
				# if sh.ncols > 4 and sh.row(rx)[4].ctype != 0:
				# if sh.ncols > 4:
				# 	print(sh.cell_value(rx, 1) + ', ' + str(sh.row(rx)[4].ctype))

				price = sh.cell_value(rx, 3)
				unit = sh.cell_value(rx, 2)

				if sh.row(rx)[3].ctype == 1 and '/' in price:
					specs = price
					price = re.findall('\d+\.?\d*', sh.cell_value(rx, 3))[0]
					# print(sh.name + ',' + sh.cell_value(rx, 1) + ', ' + sh.cell_value(rx, 3))
				else:
					specs = '%.2f元/%s' % (price, unit)

				img = sheet_images.get('%d_%d' % (i, rx))
				# if not img is None:
				# if i == 6 and rx == 32:
				# 	print('%s %d_%d' % (sh.cell_value(rx, 1), i, rx))
				item = {
					'numeration': '%s%s' % (numer_perfix, (str(rx - 1)).zfill(6)),
					'name': sh.cell_value(rx, 1),
					'img': img,
					'price': price,
					'unit': unit,
					'specs': specs,
					'amount': 50,
					'category': categorys[sh.name],
					'enabled': 1
				}
				datas[sh.name].append(item)

				lists.append(item)

	with open('temp/goods.json', 'w', encoding = 'utf-8') as f:
		json.dump(datas, f, indent = 2, ensure_ascii = False)

sheet_images = {}
def process_img():
	fpath = 'temp/goods-list-img.zip'
	ext_dir = 'temp/extracts'

	fzip = zipfile.ZipFile(fpath, 'r')
	for f in fzip.namelist():
		fzip.extract(f, ext_dir)
	fzip.close()

	sheet_rels_path = '%s/xl/worksheets/_rels' % ext_dir

	for file in os.listdir(sheet_rels_path):
		sheet_index = int(re.findall('\d', file)[0]) - 1

		rs_xml = xmldom.parse(os.path.join(sheet_rels_path, file))
		relationship = rs_xml.documentElement.getElementsByTagName('Relationship')[0]

		dr_path = relationship.getAttribute('Target').replace('..', '%s/xl' % ext_dir)
		dr_rels_path = '%s.rels' % dr_path.replace('/drawings/', '/drawings/_rels/')

		dr_xml = xmldom.parse(dr_path)
		dr_xml_rels = xmldom.parse(dr_rels_path)

		dr_cell_anchors = dr_xml.documentElement.getElementsByTagName('xdr:twoCellAnchor')
		dr_rs = dr_xml_rels.documentElement.getElementsByTagName('Relationship')

		img_dict = {}
		for dr in dr_rs:
			img_dict[dr.getAttribute('Id')] = dr.getAttribute('Target')

		for ca in dr_cell_anchors:
			row = int(ca.getElementsByTagName('xdr:row')[0].firstChild.data)

			sheet_images['%d_%d' % (sheet_index, row)] = img_dict[ca.getElementsByTagName('a:blip')[0].getAttribute('r:embed')].replace('..', '%s/xl' % ext_dir)

		# print('%d %d' % (len(dr_cell_anchors), len(dr_rs)))

	with open('temp/sheet_images.json', 'w', encoding = 'utf-8') as f:
		json.dump(sheet_images, f, indent = 2, ensure_ascii = False)

def upload_image(goods):
	path = goods.get('img')
	name = '%s%s' % (goods.get('name'), os.path.splitext(path)[1])

	data = {
		'appName': 'esp-food',
		'dirPath': 'images'
	}

	files = { 'file': (name, open(path, 'rb'), 'image/jpeg', {}) }
	res = requests.post('http://10.122.163.75:8031/file/upload', data = data, files = files)
	goods['img'] = json.loads(res.text).get('data').get('filePath')

def save_goods():
	process_img()
	print('Images: %d' % len(sheet_images))
	read_goods()
	print('Total: %d' % len(lists))

	sc = 0
	for l in lists:
		if not l.get('img') is None:
			upload_image(l)
			sc += 1
			# print('%s %s' % (l.get('name'), l.get('img')))

	print('Saved images: %d' % sc)

	requests.post('http://10.122.163.75:8030/supermarket/goods/save/init', 
		data = { 'goods': json.dumps(lists, ensure_ascii = False) })

save_goods()
