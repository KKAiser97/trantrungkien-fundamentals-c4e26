answers1={"1":"35",
"2":"36",
"3":"40",
"4":"44"
}
answers2={"1":"about 55",
"2":"about 65",
"3":"about 75",
"4":"about 85"
}
true=0
print("Answer the following algebra question: ")
print("If x=8, then what is the answer of 4(x+3)?")
for k in answers1:
    print(k,answers1[k],sep=". ")
choices1=int(input("Your choice: "))
if choices1==4:
    print("Bingo")
    true+=1
else:
    print(":(")
print()
print("Estimate this answer(exact calculation not needed):")
print("Jack scores these marks in 5 tests: 49, 81, 72, 66, and 52. what is the mean?")
for j in answers2:
    print(j,answers2[j],sep=". ")
choices2=int(input("Your choice: "))
if choices2==2:
    print("Bingo")
    true+=1
else:
    print(":(")
print()
if true==0:
    print("You correctly answer 0 out of 2 questions")
elif true==1:
    print("You correctly answer 1 out of 2 questions")
elif true==2:
    print("You correctly answer 2 out of 2 questions")

        