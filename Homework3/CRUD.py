items=['T-Shirt', 'Sweater']
while(True):
    n=input("Welcome to our shop, what do you want(C, R, U, D)?")
    if n=='r':
        print(items)
    elif n=='c':
        m=input("Enter a new item: ")
        items.append(m)
        print(items)
    elif n=='u':
        o=int(input("Update position?"))
        items[o-1]=input("New item: ")
        print(items)
    elif n=='d':
        p=int(input("Delete position?"))
        del items[p-1]
        print(items)
    else:
        print("You must select C or R or U or D!")

