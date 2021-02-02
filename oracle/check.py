# -*- coding: utf-8 -*-

import os, time

with open('./tmp.result/dicts') as f:
	keywords = [line.strip() for line in f.readlines()]

# for ind, kw in enumerate(keywords):
# 	print(ind + 1, kw)

def find(lines):
	locations = []
	for ind, line in enumerate(lines):
		for kw in keywords: 
			if line.find(kw) > -1:
				locations.append({
					'line': ind + 1,
					'text': line,
					'name': kw
				})
	return locations

counter = 0
t0 = time.process_time()
for parent, dirnames, filenames in os.walk('./tmp.plain'):
	for fname in filenames:
		# print('[INFO]', '------------------------------------------------')
		# print('[INFO]', 'File: %s' % fname)
		with open('%s/%s' % (parent, fname)) as f:
			locations = find(f.readlines())
			# print(locations)
			if locations:
				# print('[INFO]', 'Had been found')
				counter += len(locations)
				print('[INFO]', '------------------------------------------------')
				print('[INFO]', 'Table: %s' % fname.replace('.txt', ''))
				for loc in locations:
					print('[WARNING]', 'Line: %d, Name: %s' % (loc['line'], loc['name']))
					print(loc['text'])
			else:
				# print('[INFO]', 'Not found')
				pass

print('[INFO]', '------------------------------------------------')
print('[INFO]', 'Total %d records' % counter)
print('[INFO]', 'Total cost: %.6fs' % (time.process_time() - t0))
