from qgb import U,T
def p(al):
	for i in al:
		print i
	U.pln()

class zr:
	def __init__(s,index,a,r=None):
		s.i=index
		s.a=a
		s.r=r
		s.ri=None
		s.html=None
	def __str__(s):
		return '{%s:%s,%s[%s}'%(s.i,s.a,s.r,s.ri)


ld=[[1],[2,1],[3],[3,2],[4],[5,1]]
lt=[]

for i in range(len(ld)):
	if(len(ld[i])==1):
		lt.append(zr(i,ld[i][0]))
	if(len(ld[i])==2):
		lt.append(zr(i,ld[i][0],ld[i][1]))
		j=i
		while(j>-1):
			if(ld[j][0]==ld[i][1]):
				lt[-1].ri=j
			j-=1
p(lt) 
ls=[]
for i in lt:
	ls.append([])
	if(i.ri!=None):
		ls[-1].append(lt[i.ri])
	else:
		ls.append()


exit()
for i in ld:
	if(len(i)==1):
		lt.append([(i[0],)])
	if(len(i)==2):
		lt.append([(i[0],i[1])])

print lt
exit()

ls=[]
for d in ld:
	if(len(d)==1):
		ls.append(d)
		continue
	if(len(d)==2):
		im=len(ls)-1
		while(im>-1):
			if(ls[im][0]==d[1]):
				ls[im]=[]				
				print im
			im-=1
			
		
	break
		