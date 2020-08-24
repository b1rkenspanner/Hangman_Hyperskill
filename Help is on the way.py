import random

def hangman(random):
    if guess == random:
        return "You survived!"
    else:
        return "You are hanged!"
        
words = ['python', 'java', 'kotlin', 'javascript']
random = words[random.randrange(0, 4)]

print("H A N G M A N")

guess = input("Guess the word "+random[0:3]+'-'*(len(random)-3))


print(hangman(random))
