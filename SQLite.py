from qgb import *
import sqlite3
conn = sqlite3.connect('d:\\test\\douban.db')
def execsql(sql):
	global conn
	if sql is not None and sql != '':
		cu =conn.cursor()
		# print('{}'.format(sql))
		r=cu.execute(sql)
		print r.next()
		conn.commit()
	else:
		print('the [{}] is empty or equal None!'.format(sql))
# execsql('create
execsql(T.sqlite)