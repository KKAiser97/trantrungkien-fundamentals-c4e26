n=int(input("Enter a number: "))
if n%2==0:
    for i in range (n/2):
        print("x *",end=" ")
else:
    print("x",end=" ")
    for i in range((n-1)/2):
        print("* x",end=" ")