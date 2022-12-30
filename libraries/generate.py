from random import choice
from random import randint
from random import shuffle

cards = ["jack", "queen", "king"]
# print(choice(["heads", "tails"]))
# print(randint(1,10))

shuffle(cards)
for _ in cards:
    print(_)