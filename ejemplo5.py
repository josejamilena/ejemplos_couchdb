from couchdb import client, http
# 
server = client.Server()
db = server['python-tests']
try:
	doc = db['arch']
	db.delete(doc)
except:
    print "ya existe"
db['arch'] = dict(type='archivo', name='mi archivo')
doc = db['arch']
db.put_attachment(doc, 'hola mundo',  filename='mi archivo.txt', content_type='text/plain')


map_fun = '''function(doc) {
	     if (doc.type == 'archivo')
	    	emit(doc.name, null);
	  }'''
for row in db.query(map_fun):
    print row.key
