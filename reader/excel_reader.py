# -*- coding: utf-8 -*-

import xlrd, pinyin

def read_excel():
	wb = xlrd.open_workbook('temp/goods-list.xlsx')
	for i in range(wb.nsheets):
		sh = wb.sheet_by_index(i)
		print('***************************')
		print('{0} {1} {2} {3}'.format(sh.name, pinyin.get_initial(sh.name, '').upper(), sh.nrows, sh.ncols))
		print('---------------------------')
		for rx in range(2, sh.nrows):
			if sh.row(rx)[0].ctype != 0:
				print('%s %s %s' % (sh.row(rx)[1].value, sh.row(rx)[2].value, sh.row(rx)[3].value))
		print('***************************')		

read_excel()
