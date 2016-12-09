""" Combines two random words to make a company name """
import random as r

words = []
with open('data/names.txt', 'r') as f:
    for word in f:
        words.append(word.strip())
        print(word.strip())

print()
while True:
    print(r.choice(words), r.choice(words))
    input('Next?\n')
