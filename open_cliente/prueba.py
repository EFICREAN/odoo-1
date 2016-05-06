import functools
import xmlrpclib
HOST = '162.243.82.50'
PORT = 8069
DB = 'PAN_PROD'
USER = 'admin03'
PASS = 'admin'
ROOT = 'https://%s/xmlrpc/' % (HOST)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(xmlrpclib.ServerProxy(ROOT + 
	'object').execute,DB, uid, PASS)

# 2. Read the sessions
Campos = call('res.users','search_read', [], 
				['name','password'])
for Campo in Campos:
    print "%s ---> %s  \n" % (Campo['name'],Campo['password'])

#3.create a new session

#session_id = call('openacademy.course', 'create',{
#    'name' : 'Curso 3',
#    'description' : 'Descripcion 3',
#    'responsible_id' : 'Administrator'
#})

