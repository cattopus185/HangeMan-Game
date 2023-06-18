import random
from words import words

CC=list(random.choice(words))
CCI=len(CC)
MM=7
mygw = ['_'] * len(CC)
print(CC)

for i in range(MM):
    UI=input("Enter one letter you think in the word ")
    if UI not in CC:
        print("keep trying with the correct letters")
    else:
            indices = [a for a, x in enumerate(CC) if x == UI] #for i, x in enumerate(CC) says to go through these pairs, where i is the index and x is the value at that index.
            for index in indices:
                 mygw[index]=UI
                 
            showmygw=' '.join(mygw)
            showCC=' '.join(CC)
            print(showmygw)

            if showmygw==showCC:
                 print("yo man, you got it ")

print("you ran out of trials ")      
