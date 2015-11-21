import random
# print random.randint(1, 10)
import string
ls=string.lowercase
from qgb import U,T

U.setOut('d:/test/dot/b.dot')
print '''
digraph G {
    main -> parse -> execute;
'''
for i in range(len(ls)):
    print "%s->%s->%s->%s"%(ls[i],ls[min(25,i+1)],ls[random.randint(0, 25)],ls[random.randint(0, 25)])
	
print '''
    execute -> compare;
}
'''
