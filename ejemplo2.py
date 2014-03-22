from couchdb import client, http
# 
server = client.Server()
db = server['python-tests']
#update 1
print 'update 1'
doc = db['12312312']
doc['type']='Person'
doc['name']='cosa 1'
db['12312312']=doc
print 'update 2'
doc=db['m1231231232aryjane']
doc['type']='Person'
doc['name']='cosa 2'
doc=db['m1231231232aryjane']=doc
print 'update 3'
doc=db['gotham']
doc['type']='Persona'
doc['name']='Persona falsa'
db['gotham']=doc
print 'mapeo 1'
map_fun = '''function(doc) {
	     if (doc.type == 'Person')
	    	emit(doc.name, null);
	  }'''
for row in db.query(map_fun):
    print row.key
print 'update 4'
doc=db['gotham']
doc['type']='City'
doc['name']='Gotham City'
db['gotham']=doc
print 'mapeo 2'
map_fun1 = '''function(doc) {
	     if (doc.type == 'City')
	    	emit(doc.name, null);
	  }'''
for row in db.query(map_fun1):
    print row.key

	  