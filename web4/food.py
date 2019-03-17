from db import food_collection
from bson import ObjectId
def add_food(name,price):   #add
    new_food={"name":name,
            "price":price}
    a=food_collection.insert_one(new_food)
def get_food(query):    #filter, limit(sl query), skip(stt query)
    food_list=food_collection.find(query)  #lazy loading
    return food_list
def get_by_id(id):   #find
    f=food_collection.find_one({"_id":ObjectId(id)})
    return f
def del_by_id(id):   #del
    d=food_collection.delete_one({"_id":ObjectId(id)})
    return d
def update_by_id(id, name, price):
    query={"_id":ObjectId(id)}
    updater={
        "$set":{"price":price},
        "$set":{"name":name}
    }
    food_collection.find_one_and_update(query,updater)
    
if __name__=='__main__':
    app.run(debug=True) 
    # while True:
    #     f=input("Enter a new food: ")
    #     p=int(input("Enter the price of the new food: "))
    #     add_food(f,p)
    # # food_list=food_collection.find({"price":{"$gte":500}})
    # food_collection.delete_one({"_id":ObjectId("5c81250b68a3ff01440a1614")})
    # f=get_by_id("5c81238668a3ff1ee46af9a1")
    
    # if f !=None:
    #     print(f["name"])
    # # for food in get_food({"_id":ObjectId("5c81238668a3ff1ee46af9ad")}):
        
    # #     print(food)
    # a=add_food("Bun cha",20000)
    # d=del_by_id("5c81238668a3ff1ee46af9ad")
    # # query={"_id":ObjectId("5c8a5eb068a3ff0d88115604")}
    # # updater={"$set":{"price":10000}}   #$inc, $dec, $set, $unset
    # # food_collection.find_one_and_update(query,updater)
    # # print(*get_food({}), sep="\n")
    # u=update_by_id("5c8a5ef968a3ff1a787d5009", "bun cho", 15000)
    