from couchdb import client, http
# 
server = client.Server()
db = server['python-tests']
db.cleanup()
db.compact()

