#ToDo List
import redis

r = redis.Redis(host='192.168.2.168',port=6379,db=0)
print (r.get('Julia'))
r.set('Oki', 'Doki')
print (r.get('Oki'))