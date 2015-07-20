import functools
import xmlrpclib
import csv

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
    print "Campos %s - %s" % (Campo['id'], Campo['name'])

#3.create a new session
reader = csv.reader(open('categ_ind.csv','rb'))
for row in reader:
	print row[0]
	campos_id = call('open_cliente.categ_ind', 'create',{
    	'name' : row[0]
	})

