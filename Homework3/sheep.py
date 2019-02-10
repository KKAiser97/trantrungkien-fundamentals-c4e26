items=[]
sum=0
m=int(input("Enter the number of your flock: "))
for i in range(m):
    n=int(input("Enter your flock sizes: "))
    items.append(n)
print("Hello, my name is Kien and these are my sheep sizes:",items)
for month in range(3):
    print("Month",month+1)
    print("Now my biggest sheep has size",max(items),". Let's sheer it!")
    o=max(items)
    p=items.index(o)
    del items[p]
    print("After sheering, here is my flock:",items)
    sheep=[]
    for i in items:
        i=i+50
        sheep.append(i) 
    print("One month has passed, here is my flock now:",sheep)
for i in sheep:
    sum +=i
print("My flock has size in total:",sum)
print("I would get:",sum,"*2$= ",sum*2)
