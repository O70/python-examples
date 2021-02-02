# -*- coding: utf-8 -*-

import cx_Oracle as cx
import time, config

def outputTypeHandler(cursor, name, defaultType, size, precision, scale):
	if defaultType == cx.CLOB:
		return cursor.var(cx.LONG_STRING, arraysize = cursor.arraysize)
	elif defaultType == cx.BLOB:
		return cursor.var(cx.LOGIN_BINARY, arraysize = cursor.arraysize)

conn = cx.connect(config.username, config.password, config.dsn)
conn.outputtypehandler = outputTypeHandler

with conn.cursor() as cursor:
	# tables = ['USER_INFO', 'SYS_EXPORT_SCHEMA_13']
	tables = []
	cursor.execute('SELECT * FROM USER_TABLES')
	for row in cursor.fetchall():
		tables.append(row[0])

	t0 = time.process_time()
	for table in tables:
		print('[INFO]', '------------------------------------------------')
		print('[INFO]', 'Table: %s' % table)
		s0 = time.process_time()
		try:
			rows = []
			for row in cursor.execute('SELECT * FROM ' + table):
				rows.append(' | '.join(str(v).replace('\n', '') for v in row if v != None) + '\n')

			with open('./tmp.plain/%s.txt' % table, 'w', encoding = 'UTF-8') as f:
				f.writelines(rows)
		except Exception as e:
			print('[ERROR]', '%s[%s]' % (e, table))
		finally:
			print('[INFO]', 'Cost: %.6fs' % (time.process_time() - s0))

	print('[INFO]', '------------------------------------------------')
	print('[INFO]', 'Total cost: %.6fs' % (time.process_time() - t0))

conn.close()
