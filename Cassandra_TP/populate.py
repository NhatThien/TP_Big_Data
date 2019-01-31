import pycassa
import sys 

pool = pycassa.ConnectionPool('wordcount',['127.0.0.1:9160'])#9160
bible = pycassa.ColumnFamily(pool, 'bible') 
key = 1

for actual_line in sys.stdin:
	bible.insert(key, {'line': actual_line})
	key+=1

