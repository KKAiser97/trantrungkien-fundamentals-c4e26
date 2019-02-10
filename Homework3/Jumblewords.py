import random
words=['professional','produce','chaos','mediaval','supernature','omnipotent','bless']
print("Welcome to the world of Jumble Words!")
n=input("Do you want to start?(yes/no)")
if n=='yes':
    word=random.choice(words)
    jumble=[]
    correct=word
    for i in word:
        pos=random.randrange(len(word))
        jumble+=word[pos]
    print("Quest:",jumble)
    m=input("Your answer:")
    if m!=correct:
        print(":(")
        m=input("Your answer:")
    else:
        print("Hura")
        n=input("Do you want to paly again?(yes/no")
elif n=='no':
    print("Good bye!")
else:
    print("You should choose yes or no.")
    n=input("Do you want to start?(yes/no)")
print("Thanks for enjoying the game!")
        

