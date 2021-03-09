# -*- coding: utf-8 -*-

import json, functools

with open('tmp.flow.json') as f:
	flows = json.load(f)
	totals = []
	steps = []
	for item in flows['data']:
		# print((item.keys()))
		for ty in item.keys():
			print(ty)
			# print(ty.items())
			for a in item[ty].values():
				print(a)
				for b in a:
					s = int(b) * a[b]
					totals.append(a[b])
					steps.append(int(b) * a[b])
					print(b, '*', a[b], '=', int(b) * a[b])
				# for k, v in a.items():
				# 	print(a, v)

		print('----------------------------')

	print(totals)
	print(steps)
	print(functools.reduce(lambda x, y: x + y, totals))
	print(functools.reduce(lambda x, y: x + y, steps))
