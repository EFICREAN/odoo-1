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
xwriter = csv.writer(open('temp.csv','wb'))
def seleccionA():
	Campos = call('open_cliente.categ_ind','search_read', [], ['id','name'])
	for Campo in Campos:
	#	xwriter.writerow([Campo['name'], Campo['id']])
		print "%s, %s" % (Campo['id'], Campo['name'])

def seleccionB():
	Campos = call('open_cliente.urb','search_read', [], ['id','name'])
	for Campo in Campos:
	#	xwriter.writerow([Campo['name'], Campo['id']])
		print "%s, %s" % (Campo['id'], Campo['name'])

		
available_actions = {"1": seleccionA,
                     "2": seleccionB}
action = raw_input("What should I do now? ")
try:
    available_actions[action]()
except KeyError:
    print "Unrecognized command ", action

#3.create a new session

#session_id = call('openacademy.course', 'create',{
#    'name' : 'Curso 3',
#    'description' : 'Descripcion 3',
#    'responsible_id' : 'Administrator'
#})

