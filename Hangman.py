print("Hangman - The Guessing Game")
print()
print("Here, a random word is picked up from our collection and the player gets limited chances to win the game."
"When a letter in that word is guessed correctly, that letter position in the word is made visible." 
"In this way, all letters of the word are to be guessed before all the chances are over."
"For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user"
"gets 5 + 2 = 7 chances, as mango is a five letter word.")
print()
print()
print("Let's get into the Game...")
print()
print("The word is given below")
def display(c):
    for i in c:
        print(i,end="  ")
collection={"hello","dangerous","mexico","random","mathematics","music","money","cricket","football","rockstar","market","lemon",
"carrot","raddish","monkey","mountain","lake","lifetime","knife","love","lottery","pirate","movie","mobile","fountain","charger",
"computer","landline","dragon","yellow","orange","cake","birthday","chess","guitar","friend","memory","body","pain","muscle","own",
"seven","eight","nine","building","dinner","lunch","game","stable","drone","development","actor","old","young","author","rabbit",
"avengers","scene","series","number","alphabet","vampire"}
q=1
while(q!=0):
    z=[]
    l=list(collection)
    size=len(l[q])
    dup=l[q]
    l[q]=list(l[q])
    for i in range(size):
        z.append("_")
    display(z)
    win=0
    j=0
    while(j<size+2):
        count=0
        print("\n\nEnter a letter to guess : ")
        a=input()
        if(a in l[q]):
            for i in l[q]:
                if(i==a):
                    j=j-1
                    z[l[q].index(i)]=a;
                    l[q][l[q].index(i)]=-1
        display(z)
        for i in z:
            if(i=='_'):
                count=1
        if(count==0):
            win=1
            print("\n\nYou won...you find the word "+dup+" correctly...Wanna try again (Y/N)")
            break
        j=j+1
    if(win!=1):
        print("\n\nYou lost...the word is "+dup+"... Wanna try again (Y/N)")
    g=input()
    if(g=='Y'):
        q+=1
    else:
        q=0
        print("Thanks for playing...Bye Bye")
    



