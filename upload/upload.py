# -*- coding: utf-8 -*-

import os, requests

dirs = 'tmp'
for d in os.listdir(dirs):
	# with open('%s/%s' % (dirs, d), 'r') as f:
	# 	print(f)

	data = {
		'appName': 'esp-fs',
		'dirPath': 'docs'
	}

	files = { 'file': (d, open('%s/%s' % (dirs, d), 'rb'), 'image/jpeg', {}) }
	res = requests.post('http://localhost:8031/file/upload', data = data, files = files)
	print(res.json())
