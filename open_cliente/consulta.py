# -*- coding: utf-8 -*-
import functools
import xmlrpclib
import csv

HOST = '66.228.37.73'
PORT = 8069
DB = 'PAN_PROD'
USER = 'admin01'
PASS = 'admin'
ROOT = 'https://%s/xmlrpc/' % (HOST)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(xmlrpclib.ServerProxy(ROOT + 
	'object').execute,DB, uid, PASS)

# 2. Read the sessions
#xwriter = csv.writer(open('temp.csv','wb','utf-8'))
with open('temp.csv', 'w', newline='') as csvfile:
	xwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	
def seleccionA():
	Campos = call('res.partner','search_read', [], ['id','name'])
	for Campo in Campos:
		xwriter.writerow([Campo['name'], Campo['id']])
		print "%s, %s" % (Campo['id'], Campo['name'])

def seleccionB():
	Campos = call('open_cliente.urb','search_read', [], ['id','name'])
	for Campo in Campos:
		xwriter.writerow([Campo['name'], Campo['id']])
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

