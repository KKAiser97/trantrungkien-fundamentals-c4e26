from pymongo import MongoClient
import matplotlib.pyplot as plt
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client=MongoClient(uri)
db=client.c4e
post_collection=db["posts"]
new_post={
    "title":"C4E",
    "author":"Tran Kien",
    "content":"Learning is good, let's learn more!"
}
post_collection.insert_one(new_post)

customer_collection=db["customers"]
customers=customer_collection.find()
e=0
w=0
a=0
for c in customers:
    if c["ref"]=="events":
        e+=1
    elif c["ref"]=="wom":
        w+=1
    else:
        a+=1
parts=[e,w,a]
labels=["event","wom","ads"]
colors=["red","blue","yellow"]
plt.pie(parts, labels=labels, colors=colors)
plt.axis("equal")
plt.show() 

def close():
    client.close()