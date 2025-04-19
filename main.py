import pymongo
#provide the mongodb localhost url to connect python to mongodb
client= pymongo.Mongoclient("mongodb://localhost:27017/DB1")
#Database name
database= client["DB1"]

#collection name
collection = database['Products']

#Sample data
d= {'companyname' : 'xyz', 'product': 'AI','Course' : 'ML'}

#Insert above record in the collection
rec= collection.insert_one(d) 

#Lets verify all the records at once present in the record with all the fields
all_record = collection.find()

#printing all records present in the collection
for idx,record in enumerate(all_record):
    print(f"{idx} : {record}")