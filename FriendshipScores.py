#! /usr/bin/python

alphabet= "abcdefghijklmnopqrstuvwxyz"
names = input("Enter the names of 2 people : ")
print(names)
score = 0

for charater in names:
    #if charater in alphabet:
    #    position = alphabet.find(charater)
    #    score += position
    #else:
    #    score += 0
    if charater in 'aeiou':
        score += 5
    elif charater in 'friend':
        score += 10
    elif charater in 'best':
        score += 15
    else:
        score += 0
        
print("Score : " , score)

if score > 100:
    print("Best Friends!")
elif score > 50:
    print("Good Friends!")