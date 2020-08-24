import random

def attempt(random):
    length = len(random)
    guess_word = (list("-"*length))
    
    rep_letter = []
    
    count = 8
    while count > 0:
        print()
        if "".join(guess_word)  == random:
            print("".join(guess_word))

            print("""You guessed the word!
You survived!""")
            break
              
        print("".join(guess_word))
        word = input("Input a letter: ") 
        if len(word) != 1:
            print("You should input a single letter")
            continue
        if word >= "a" and word <= "z":
            
            if word in rep_letter:
                print("You already typed this letter")
            
            
            elif word in random:
                if word in rep_letter:
                    print("You already typed this letter")
                else:
                    for i in range(length):
                        if random[i] == word:
                            guess_word[i] = word
                            rep_letter.append(word)
                
            else:
                print("No such letter in the word")
                rep_letter.append(word)
                count-=1
        else:
            print("It is not an ASCII lowercase letter")
    if "".join(guess_word) != random:
        print("You are hanged!")
words = ['python', 'java', 'kotlin', 'javascript']
random = words[random.randrange(0, 4)]

print("H A N G M A N")

attempt(random)
