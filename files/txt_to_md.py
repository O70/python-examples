# -*- coding: utf-8 -*-

# https://blog.csdn.net/whatday/article/details/107965258
# with open('./zt.txt', 'r+') as f:
# 	# print(type(f.readlines()))
# 	# for line in f.readlines():
# 	# 	print(line)
# 	t = f.read()
# 	t = t.replace('第001章', '## 第001章')

# 	# 读写偏移位置移到最开始处
# 	f.seek(0, 0)
# 	f.write(t)

# 	# 设置文件结尾 EOF
# 	# 设置文件结尾 为了避免 多字符 替换为 少字符后 文件尾部有 原文件残余字符
# 	f.truncate()

import re

with open('./zt.txt', 'r') as f:
	with open('./tmp.zt.md', 'w') as fd:
		for line in f.readlines():
			# if line.find('第001章') > -1:
			# 	print(line)
			# print(re.match(r'第(.+?)章', line))
			if re.match(r'第(.+?)章', line):
				fd.write('## ' + line)
			else:
				fd.write('<p>' + line + '</p>')
