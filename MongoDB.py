import pymongo
uri="mongodb://127.0.0.1:27017 "

client=pymongo.MongoClient(uri) #initialize mongoldb client
db=client['itemsDB'] #Get the database
collection=db['itemsCol']  #Get collections
