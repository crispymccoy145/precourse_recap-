import random

#generates a random number from the imported random module method
x = random.randint(1, 100)

#prints the task for the client
print("Guess the number between 1 and 100")

#creates a loop of guessing that only ends when the client guesses correctly
while True:
    y = int(input('What is your guess? '))
    if x == y:
        print("correct answer")
        break
    elif y < x:
        print("too low")
    else:
        print("too high")