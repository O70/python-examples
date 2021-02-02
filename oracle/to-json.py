# -*- coding: utf-8 -*-

import cx_Oracle as cx
import json, time, config

def outputTypeHandler(cursor, name, defaultType, size, precision, scale):
	if defaultType == cx.CLOB:
		return cursor.var(cx.LONG_STRING, arraysize = cursor.arraysize)
	elif defaultType == cx.BLOB:
		return cursor.var(cx.LOGIN_BINARY, arraysize = cursor.arraysize)
	# elif defaultType == cx.DB_TYPE_RAW:
	# 	return 'RAW-TYPE-V2'
	# elif defaultType == cx.DB_TYPE_DATE:
	# 	# return 'df' #val.strftime('%Y-%m-%d')
	# 	return cursor.var(cx.)
	# elif defaultType == cx.DB_TYPE_TIMESTAMP:
	# 	# return 'df' #val.strftime('%Y-%m-%d')
	# 	return cursor.var(cx.)

conn = cx.connect(config.username, config.password, config.dsn)
conn.outputtypehandler = outputTypeHandler

# <cx_Oracle.DbType DB_TYPE_CLOB>
# <cx_Oracle.DbType DB_TYPE_LONG>
# <cx_Oracle.DbType DB_TYPE_VARCHAR>
# <cx_Oracle.DbType DB_TYPE_CHAR>
# <cx_Oracle.DbType DB_TYPE_RAW>
# <cx_Oracle.DbType DB_TYPE_NUMBER>
# <cx_Oracle.DbType DB_TYPE_DATE>
# <cx_Oracle.DbType DB_TYPE_TIMESTAMP>

# data = []
with conn.cursor() as cursor:
	tables = []
	cursor.execute('SELECT * FROM USER_TABLES')
	for row in cursor.fetchall():
		tables.append(row[0])

	t0 = time.process_time()
	for table in tables:
		# if table != 'SYS_EXPORT_SCHEMA_13':
		# if table != 'USER_INFO':
		# 	continue

		print('[INFO]', '------------------------------------------------')
		print('[INFO]', 'Table: %s' % table)
		s0 = time.process_time()
		# item = { 'table': table }
		try:
			cursor.execute('SELECT * FROM ' + table)

			columns = []
			for col in cursor.description:
				columns.append(col)

			rows = []
			alls = cursor.fetchall()
			print('[INFO]', 'Rows: %d' % len(alls))
			for row in alls:
				dictRow = {}
				for ind, val in enumerate(row):
					col = columns[ind]
					if col[1] == cx.DB_TYPE_RAW:
						dictRow[col[0]] = 'RAW-TYPE'
					elif col[1] == cx.DB_TYPE_DATE:
						if val:
							val = val.strftime('%Y-%m-%d')
						dictRow[col[0]] = val
					elif col[1] == cx.DB_TYPE_TIMESTAMP:
						if val:
							val = val.strftime('%Y-%m-%d %H:%M:%S')
						dictRow[col[0]] = val
					else:
						dictRow[col[0]] = val

				rows.append(dictRow)
			# item['rows'] = rows
			# data.append(item)

			with open('./tmp.json/%s.json' % table, 'w', encoding = 'UTF-8') as f:
				json.dump(rows, f, sort_keys = False, indent = 2, ensure_ascii = False)
		except Exception as e:
			print('[ERROR]', '%s[%s]' % (e, table))
		finally:
			print('[INFO]', 'Cost: %.6fs' % (time.process_time() - s0))

	print('[INFO]', '------------------------------------------------')
	print('[INFO]', 'Total cost: %.6fs' % (time.process_time() - t0))

conn.close()

# print('********************', 'Storing files', '********************')
# t0 = time.process_time()
# for item in data:
# 	with open('./tmp/%s.json' % item['table'], 'w', encoding = 'UTF-8') as f:
# 		json.dump(item['rows'], f, sort_keys = False, indent = 2, ensure_ascii = False)
# print('[INFO]', 'Total cost: %.6fs' % (time.process_time() - t0))
