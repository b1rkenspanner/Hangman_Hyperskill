import random

def attempt(random):
    length = len(random)
    guess_word = (list("-"*length))

    count = 8
    while count > 0:
        print("".join(guess_word))
        word = input("Input a letter: ") 
        if word in random:
            for i in range(length):
                if random[i] == word:
                    guess_word[i] = word
                    print("")

        else:
            print("No such letter in a word")
            print("")

        count-=1
    print("""Thanks for playing!
We'll see how well you did in the next stage""")

words = ['python', 'java', 'kotlin', 'javascript']
random = words[random.randrange(0, 4)]

print("H A N G M A N\n")

attempt(random)
