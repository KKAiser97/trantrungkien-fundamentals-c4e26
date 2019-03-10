from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client=MongoClient(uri)
db=client.c4e
river_collection=db["river"]
African_rivers=river_collection.find({"continent":"Africa"})
American_rivers=river_collection.find({"continent":"S.America", "length":{"$lt":1000}})

def close():
    client.close