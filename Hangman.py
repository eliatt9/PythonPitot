import random

# General list of words to guess
arr = ["eli", "zazu", "linoy", "davidtheking", "talma"]

# Choosing a random word
word = random.choice(arr)

# Initializing the array of the guesses to display to the user.
answer = [" _ "] * len(word)

# Variables for if the player guessed the word and how many lives the player has left.
guess = False
life = 8

# Giving the player his guesses.
while (not guess) and (life > 0):
    correct = True
    print("you still have %d lifespans" % life)
    print("".join(answer))
    user_input = input("My guess is:")
    
    # Checking if the user guessed correctly, and if so - replace the matching letter in the answer list.
    if user_input.isalpha() and len(user_input) == 1:
        correct = False
        for i in range(len(word)):
            if user_input.lower() == word[i]:
                answer[i] = user_input.lower()
                correct = True
        
        # If the user guessed wrong - reduce his life points
        if not correct:
            life -= 1
           
        # Checking if the player won - and if so, exit the loop.
        if answer.count(" _ ") == 0:
            guess = True
    else:
        print("please enter a valid single letter")
        life -= 1

if life > 0:
    print("Hayde! the word is")
    print("".join(answer))
else:
    print("Meahzev aval lo maftia HEFSADETA")
    print("the correct word was")
    print("".join(word))
