# -*- coding: utf-8 -*-

import xlrd, json

wb = xlrd.open_workbook('tmp/yanxin_label.xlsx')
sheet = wb.sheet_by_index(0)

labels = []
for rx in range(1, sheet.nrows):
	if sheet.cell_value(rx, 0):
		labels.append({ 'label': sheet.cell_value(rx, 0), 'children': [] })

	labels[-1]['children'].append({
		'value': rx - 1,
		'label': sheet.cell_value(rx, 1),
		'describe': sheet.cell_value(rx, 2)
	})

with open('tmp/labels.json', 'w', encoding = 'utf-8') as f:
		json.dump(labels, f, indent = 4, ensure_ascii = False)
