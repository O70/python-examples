# -*- coding: utf-8 -*-

import xlrd, pinyin, uuid

sql_prefix = 'INSERT INTO base_dict (id, code, name, parent_id, enabled, remark, deleted, spell, initials, level_code) VALUE'

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
	wb = xlrd.open_workbook('temp/goods-list.xlsx')
	for i in range(wb.nsheets):
		sh = wb.sheet_by_index(i)
		print('***************************')
		print('{0} {1} {2} {3}'.format(sh.name, pinyin.get_initial(sh.name, '').upper(), sh.nrows, sh.ncols))
		print('---------------------------')
		for rx in range(2, sh.nrows):
			if sh.row(rx)[0].ctype != 0:
				# print('%s %s %s %s' % ((str(rx-1)).zfill(6), sh.row(rx)[1].value, sh.row(rx)[2].value, sh.row(rx)[3].value))
				print('%s %s %s %s' % ('%06d' % (rx - 1), sh.row(rx)[1].value, sh.row(rx)[2].value, sh.row(rx)[3].value))
		print('***************************')		

# read_building()
read_category()
# read_goods()
