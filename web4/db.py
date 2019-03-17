from pymongo import MongoClient
uri="mongodb+srv://admin:admin123@c4e-wzwhq.mongodb.net/test?retryWrites=true"
# 1.Connect
client=MongoClient(uri)
# 2.Get db
db=client.test
# 3.Get collection
food_collection=db["food"]
user_collection=db["users"]
# # 4.Create a new document
# new_food={
#     "name":"bun cha",
#     "price":100
# }
# # 5.Insert new doc into collection
# food_collection.insert_one(new_food)
# 6.Close conection
def close():
    client.close()