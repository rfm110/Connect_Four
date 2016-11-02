import random


random_number = random.randint(0, 10)


for i in range(0, 6):
    guess = raw_input("Pick a random number between 0 and 10\n")

    try:
        guess = int(guess)
    except:
        print "your input is invalid"
        continue

    if int(guess) == int(random_number):
        print("You have picked the correct answer!")
        break
    else:
        print("Incorrect response")

        if guess < random_number:
            print("Your number is too small")
        else:
            print("Your number is too big")

print("The correct answer was %s" % random_number)
