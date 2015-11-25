import sqlite3
conn = sqlite3.connect('d:\\test\\test.db')
def execsql(sql):
	global conn
	if sql is not None and sql != '':
		cu =conn.cursor()
		print('{}'.format(sql))
		cu.execute(sql)
		conn.commit()
	else:
		print('the [{}] is empty or equal None!'.format(sql))
# execsql('create table ta(t varchar(20) NOT NULL)')
execsql('insert into ta(t) values(1)')