# -*- coding: utf-8 -*-

import xlrd, xlwt

values = {
	'zcc': '62',
	'zmch': '93',
	'gaoshp': '105',
	'wangcaizhi': '254',
	'chunch': '255',
	'zhangsong09': '2329',
	'dazy': '315',
	'gyr2005': '344',
	'wangjianjun': '483',
	'sikwtj': '362',
	'houlh': '2532',
	'haodl': '1068',
	'xhx': '1472',
	'wjl': '1509',
	'zh_tao': '1523',
	'hanbin77120': '2308',
	'whj': '2356',
	'zhanghongyang': '2760',
	'xiewen': '2800',
	'zhangj': '2395',
	'yn': '2876',
	'wangfenglily': '2881',
	'zqc': '2893',
	'wangwy321': '2897',
	'zjz': '2905',
	'yangzhixiang': '2671',
	'lbz': '2789',
	'gxh2008': '2583',
	'zhangyu01': '2606',
	'fxf': '2860',
	'luojh': '2862',
	'ouyj': '2872',
	'yanjianwen': '3129',
	'zhaoliangdong': '3184',
	'ymzhanghj': '3195',
	'zhangna01': '184',
	'bilina': '2955',
	'zhangli-tz': '2966',
	'wangye.hr': '3253',
	'caidm': '2929',
	'liyongph': '3043',
	'yanghua': '2837',
	'yx0124': 'a9879c61-87d7-4d95-83a9-706015f87880',
	'zhuo': '3174',
	'tangping-gj': '3067',
	'zy87': '3068',
	'shily': '3069',
	'maoyajun': '6694',
	'yanzp': '079c5cc1-ccd9-4a6b-9292-ed128bc300ff',
	'chw': '0fc80d27-5c0b-4544-bf6f-28837c810cf9',
	'fm': '21',
	'yx0124': '9002',
	'wsf01': 'a9cdb2b6-0bc6-4486-91ab-099216512b58',
	'shenduanming': '7c0f4375-bdd7-4ae0-a26b-b3a032bd8fe5',
	'ningn': '6156582e-aba2-42e2-bb6d-4ede6dfc3051',
	'qiucp': '29139159-788e-4c11-97d3-8d1c3aa4fae0',
	'cfliu': '6ca952bb-3d97-4fa9-9047-e266070c4a73',
	'xiongwei69': 'aebe6c98-c66f-43e6-87c1-bae6e26f1670',
	'doujj69': 'afa584dc-5541-4894-94c6-dea4ee9b4c6c',
	'lijian69': 'baca894a-c0f4-4873-956b-1b92f20315af',
	'gbs_cq': '71626f57-6395-4007-a95d-98d0a4f4bc5f',
	'zhengwei69': '3c624caa-c16d-4f4c-ba78-c406222780c9',
	'sunfj69': 'b83e985b-073a-48a6-bb41-7778215ddeb7',
	'zqc69': 'bf754b2a-1dfa-444f-bf57-f2728f871dee'
}

wb = xlrd.open_workbook('~/Documents/meetings.xlsx')

sheets = wb.sheet_names()
sh = wb.sheet_by_index(0)

# for rx in range(1, sh.nrows):
# 	kk = sh.cell_value(rx, 2).replace('ptr\\', '')
# 	if not values.get(kk):
# 		print('Value does not exist: {}'.format(kk))
# 	else:
# 		print('{}, {}'.format(kk, values.get(kk)))
		# sh.cell_value(rx, 3) = values.get(kk)

nwb = xlwt.Workbook()
ws = nwb.add_sheet(sheets[0])
for rx in range(0, sh.nrows):
	for cx in range(0, 8):
		if rx > 0 and cx == 3:
			kk = sh.cell_value(rx, 2).replace('ptr\\', '')
			if not values.get(kk):
				print('Value does not exist: {}'.format(kk))
			else:
				# print('{}, {}'.format(kk, values.get(kk)))
				ws.write(rx, cx, values.get(kk))
		else:
			ws.write(rx, cx, sh.cell_value(rx, cx))

nwb.save('meetings1.xlsx')
