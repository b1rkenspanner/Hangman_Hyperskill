import random

def hangman(random):
    if guess == random:
        return "You survived!"
    else:
        return "You are hanged!"
        
words = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")

guess = input("Guess the word: ")

random = words[random.randrange(0, 4)]

print(hangman(random))
