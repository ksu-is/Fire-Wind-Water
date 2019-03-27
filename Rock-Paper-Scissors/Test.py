import random

win_condition = ["Try again!", "You won!"]
options = {"scissors":"rock","paper":"scissors","rock":"paper"}
score = 0

def game():
    global score

    valid = False
    while valid is False:
        do = input("Rock, paper or scissors: ")
        valid = do in options

    cpu = random.choice(list(options))
    same = cpu == do
    won = options[cpu] == do
    score += int(won)
