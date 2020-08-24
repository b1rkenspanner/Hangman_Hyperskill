import random

def attempt(random):
    length = len(random)
    guess_word = (list("-"*length))

    count = 8
    while count > 0:
        print()
        if "".join(guess_word)  == random:
            print("".join(guess_word))

            print("""You guessed the word!
You survived!""")
            break
              
        print("".join(guess_word))
        word = input("Input a letter:") 
        
        if word in guess_word:
            print("No improvements")
            count-=1
        
        
        elif word in random:
            for i in range(length):
                if random[i] == word:
                    guess_word[i] = word

        
        else:
            print("No such letter in the word")
            count-=1
    if "".join(guess_word) != random:
        print("You are hanged!")
words = ['python', 'java', 'kotlin', 'javascript']
random = words[random.randrange(0, 4)]

print("H A N G M A N")

attempt(random)
