#coding=utf-8
from qgb import U,T


# import xlwt

# U.pprint(globals()) 
# U.helphtml(xlwt)
import xlwt
wbook=xlwt.Workbook(encoding='utf-8')
ws =wbook.add_sheet('xlwt1')


def wrow(al,aws=None,aindex=-1):
	if(aws==None):global ws
	else:ws=aws
	if(ws==None and aws ==None):raise Exception('xlwt ws None')
	
	if(aindex>-1):im=aindex
	else:im=len(ws.rows)
	
	for i in range(len(al)):
		ws.write(im,i, al[i])

wrow([23,4,32,'等等'])
print ws.rows
wbook.save('mini.xlsx')