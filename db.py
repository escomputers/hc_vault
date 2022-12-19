import pymongo

user = 'admin'
password = 'Fzf7WHvf'
cluster = 'hcvaultdb.9bx7mqn.mongodb.net'
uri = 'mongodb+srv://' + user + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client.test
print(db)