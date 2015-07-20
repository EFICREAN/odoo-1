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
sessions = call('openacademy.course','search_read', [], ['name','description',
	'responsible_id'])
for session in sessions:
    print "Session %s (%s seats) %s" % (session['name'], session['description'],
session['responsible_id'])

#3.create a new session

session_id = call('openacademy.course', 'create',{
    'name' : 'Curso 3',
    'description' : 'Descripcion 3',
    'responsible_id' : 'Administrator'
})

