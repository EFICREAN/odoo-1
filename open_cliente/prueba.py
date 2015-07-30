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
Campos = call('account.invoice.line','search_read', [], 
				['account_id','id','company_id',
				 'invoice_id','name','price_unit'])
for Campo in Campos:
    print "%s || %s || %s || %s || %s || %s" % (Campo['account_id'], Campo['id'],  
    							Campo['company_id'],Campo['invoice_id'],
    							Campo['name'],Campo['price_unit'])

#3.create a new session

#session_id = call('openacademy.course', 'create',{
#    'name' : 'Curso 3',
#    'description' : 'Descripcion 3',
#    'responsible_id' : 'Administrator'
#})

