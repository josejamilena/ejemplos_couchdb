from couchdb import client, http
# 
server = client.Server()
db = server.create('python-tests')
db['johndoe'] = dict(type='Person', name='John Doe')
db['maryjane'] = dict(type='Person', name='Mary Jane')
db['gotham'] = dict(type='City', name='Gotham City')
map_fun = '''function(doc) {
	     if (doc.type == 'Person')
	    	emit(doc.name, null);
	  }'''
for row in db.query(map_fun):
    print row.key
