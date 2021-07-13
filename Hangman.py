import random

arr = ["eli", "zazu", "linoy", "davidtheking", "talma"]
num = random.randint(0, len(arr)-1)
word = arr[num]

length = len(word)
answer = []
for le in range(length):
    answer.append("_")

guess = False
life = 8

while (not guess) and (life > 0):
    correct = True
    print("you still have %d lifespans" % life)
    print("".join(answer))
    user_input = input("My guess is:")
    if user_input.isalpha() and len(user_input) == 1:
        i = 0
        while i < len(word):
            if user_input.lower() == word[i]:
                answer[i] = user_input.lower()
                correct = False
            i += 1
        if correct:
            life -= 1
        if answer.count("_") == 0:
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
