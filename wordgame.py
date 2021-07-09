import random
system=['laptop','desktop','smart TV','Mobile']
print("Guess the word: {}".format(system))
store=random.choice(system)
# print(store)answer
j=2
def chance():
    global j
    if j>=1:
        print("Still %d chances" %j)
    else:
        print("Game Over................")
    j-=1
#let check with user:
i=0
while i<3:

    get=input("Enter the Word: ")
    if get not in system:
        print("Cannot match item")
    if get==store:
        print("Your answer is matched")
        print("Game Over.................")
        play=input("If you like to play again [y or n]: ")
        if play=='y':
            j=2
            i=0
            store=random.choice(system)
            continue
        else:
            break

        # break
    else:
        print("Failed")
        chance()
    i+=1
