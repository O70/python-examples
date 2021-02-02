# -*- coding: utf-8 -*-

import cx_Oracle as cx
import json, config, chardet

# conn = None
# try:
# 	# , encoding = 'UTF-8'
#     conn = cx.connect(config.username, config.password, config.dsn)
#     # print(conn.version)

#     cur = conn.cursor()
#     cur.execute('select * from user_info')
#     # print(a)
#     res = cur.fetchall()
#     # print(type(res))
#     for row in res:
#     	print(type(row))
#     # for row in a:
#     # 	print(type(row))
# except cx.Error as error:
#     print(error)
# finally:
#     if conn:
#         conn.close()

def store(table, cursor):
	columns = []
	for col in cursor.description:
		# if col[1] == cx.DB_TYPE_RAW:
		# 	print(col, col[1], type(col[1]))
		# print(col, col[1], type(col[1]))
		# columns.append(col[0])
		columns.append(col)

	rows = []
	for row in cursor.fetchall():
		dictRow = {}
		for ind, val in enumerate(row):
			# if columns[ind] == 'NAME':
			# 	dictRow[columns[ind]] = val.encode('utf-8')
			# else:
			# 	dictRow[columns[ind]] = val
			col = columns[ind]
			# if col[1] == cx.DB_TYPE_RAW:
			# 	dictRow[col[0]] = 'RAW-TYPE'
			if col[1] == cx.DB_TYPE_TIMESTAMP:
				if val:
					# print(col[0], val, type(val), val.strftime('%Y-%m-%d %H:%M:%S'))
					val = val.strftime('%Y-%m-%d %H:%M:%S')
				dictRow[col[0]] = val
			else:
				dictRow[col[0]] = val
			# print(val)
			# if columns[ind] == 'NAME' and isinstance(val, str) == True:
			# if columns[ind] == 'NAME':
			# 	print(type(val), val, chardet.detect(val.encode('UTF-8')))
			# print(type(columns[ind]), type(col))
		rows.append(dictRow)

	with open('./tmp/%s.json' % table, 'w', encoding = 'UTF-8') as f:
		json.dump(rows, f, sort_keys = False, indent = 2, ensure_ascii = False)

conn = cx.connect(config.username, config.password, config.dsn)

with conn.cursor() as cursor:
	tables = []
	cursor.execute('SELECT * FROM USER_TABLES')
	for row in cursor.fetchall():
		tables.append(row[0])

	# for table in tables:
	# 	try:
	# 		cursor.execute('SELECT * FROM ' + table)
	# 		for col in cursor.description:
	# 			print(col[0])
	# 	except Exception as e:
	# 		print('%s[%s]' % (e, table))

	cursor.execute('SELECT * FROM USER_INFO')
	# for col in cursor.description:
	# 	print(col[0])
	store('USER_INFO', cursor)

conn.close()
