import functools
import xmlrpclib
HOST = '104.236.123.102'
PORT = 8070
DB = 'miaspa_pr2'
USER = 'admin'
PASS = 'admin'
ROOT = 'https://%s/xmlrpc/' % (HOST)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(xmlrpclib.ServerProxy(ROOT + 
	'object').execute,DB, uid, PASS)

# 2. Read the sessions
Campos = call('open_cliente.categ_ind','search_read', [], ['id','name'])
for Campo in Campos:
    print "%s, %s" % (Campo['id'], Campo['name'])

#3.create a new session

#session_id = call('openacademy.course', 'create',{
#    'name' : 'Curso 3',
#    'description' : 'Descripcion 3',
#    'responsible_id' : 'Administrator'
#})

