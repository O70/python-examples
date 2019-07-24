# -*- coding: utf-8 -*-

import xlrd, pinyin, uuid, json, re

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
				price = sh.cell_value(rx, 3)
				unit = sh.cell_value(rx, 2)

				if sh.row(rx)[3].ctype == 1 and '/' in price:
					specs = price
					price = re.findall('\d+\.?\d*', sh.cell_value(rx, 3))[0]
					print(sh.name + ',' + sh.cell_value(rx, 1) + ', ' + sh.cell_value(rx, 3))
				else:
					specs = '%.2f元/%s' % (price, unit)

				datas[sh.name].append({
					'numeration': '%s%s' % (numer_perfix, (str(rx-1)).zfill(6)),
					'name': sh.cell_value(rx, 1),
					'img': None,
					'price': price,
					'unit': unit,
					'specs': specs,
					'amount': 100,
					'category': categorys[sh.name],
					'enabled': 1
				})

		# print('***************************')
		# print('{0} {1} {2} {3}'.format(sh.name, pinyin.get_initial(sh.name, '').upper(), sh.nrows, sh.ncols))
		# print('---------------------------')
		# for rx in range(2, sh.nrows):
		# 	if sh.row(rx)[0].ctype != 0:
		# 		# print('%s %s %s %s' % ((str(rx-1)).zfill(6), sh.row(rx)[1].value, sh.row(rx)[2].value, sh.row(rx)[3].value))
		# 		print('%s %s %s %s' % ('%06d' % (rx - 1), sh.row(rx)[1].value, sh.row(rx)[2].value, sh.row(rx)[3].value))
		# print('***************************')		

	with open('temp/goods.json', 'w', encoding = 'utf-8') as f:
		json.dump(datas, f, indent = 2, ensure_ascii = False)

# read_building()
# read_category()
read_goods()
