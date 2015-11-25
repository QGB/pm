#coding=utf-8
from qgb import U,T
import xlrd
U.helphtml(xlrd)
fn=r"E:\HT\Hacked Team\Amministrazione\08 - VIAGGI\3 - Note Spese\2013\Costi 2013.xlsx"
# fn=r"C:\RaLC三维仿真软件\实用工具\LOG分析工具\LOG分析工具2.xls"
# fn=r"E:\HT\Hacked Team\Amministrazione\01 - CLIENTI\7 - Difensiva\ANAGRAFICA FORNITORE x Trentino Trasporti.xls"
# fn=r"E:\HT\Hacked Team\Amministrazione\01 - CLIENTI\6 - Offensiva\OLD\Budget_Business Plan_2014-2018_Template - USA - SGP.xlsx"
# fn=r"C:\RaLC三维仿真软件\实用工具\XML変換工具\XML変換工具.xls"
fn=r"D:\Test\te.xls"
data = xlrd.open_workbook(fn)

# U.helphtml(data)
ctype = 1
value = 'aaaaaa'
ss=data.sheets()
for table in ss:
	for i in range(table.nrows ):
		table.put_cell(0, 0, ctype, value, 0)
		# U.helphtml(table.put_cell);exit()
		print str(table.row_values(i)).decode().encode('gbk')

