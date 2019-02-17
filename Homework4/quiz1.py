answers={"1":"35",
"2":"36",
"3":"40",
"4":"44"
}
print("Answer the following algebra question: ")
while True:
    
    print("If x=8, then what is the answer of 4(x+3)?")
    for k in answers:
        print(k,answers[k],sep=". ")
    choices=int(input("Your choice: "))
    if choices==4:
        print("Bingo")
        break
    else:
        print(":(")
        