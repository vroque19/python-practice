#quiz game

print("Welcome to my quiz!")

playing = input("Do you think you know Vanessa? ")

if playing.lower() != "yes":
    print("Okay. Fake friend. Goodbye!")
    quit()

print("Okay. Let's play!")
score = 0
# question 1
answer = input("What is Vanessa's middle name? ")
if answer.lower() == "Isabel":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# question 2
answer = input("How old is Vanessa? ")
if answer == "19":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# question 3
answer = input("How many dogs does Vanessa have? ")
if answer == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

#question 4
answer = input("Where was Vanessa born? ")
if answer.lower() == "Cuba":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")


print("You got " + str(score) + " out of 4 questions correct! ")
print("You got a " + str((score/4 * 100)) + " %! ")

