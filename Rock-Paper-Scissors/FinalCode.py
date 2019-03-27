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

    if same:
        print("You both chose: " + do + "!")
    else:
        print("You chose: " + do + "!")
        print("Your opponent chose: " + cpu + "!")

    print(win_condition[int(won)])
    print("- "*10)
    print("Your score: " + str(score))
    print("- "*10)

    game()

game()
