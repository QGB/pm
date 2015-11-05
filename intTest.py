s='''
print {0},0{0},'{1}{01}','{8}{08}'
'''
for i in range(33):
	try:
		exec s.format(i,'a','b','c','d','e','f','g','h')
	except:
		pass