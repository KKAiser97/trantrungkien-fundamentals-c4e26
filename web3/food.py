from db import food_collection
def add_food(name,price):
    new_food={"name":food,
            "price":price}
    food_collection.insert_one(new_food)
def get_food():    
    food_list=food_collection.find()  #lazy loading
    return food_list
if __name__=='__main__':
    # while True:
    #     f=input("Enter a new food: ")
    #     p=int(input("Enter the price of the new food: "))
    #     add_food(f,p)
    # food_list=food_collection.find({"price":{"$gte":500}})
    food_list = get_food()
    for food in food_list:
        
        print(food["name"])
        print(food["price"])
        
    