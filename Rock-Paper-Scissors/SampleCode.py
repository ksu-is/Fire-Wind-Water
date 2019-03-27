import random
import sys
#begin the game and then loop after the first play.

def play():
    while True:
        p_choice = input("What do you choose?")
        cpu_random = random.randint(1,3)
        cpu_choice = cpu_random
        if cpu_random == 1:
            cpu_choice = "Rock"
        elif cpu_random == 2:
            cpu_choice = "Paper"
        elif cpu_random == 3:
            cpu_choice = "Scissors"

#Compare the data given by the user to the CPU

        def compare():

            play_again = None
#Tie outcome
            if p_choice == cpu_choice:
                print("Tie!")
                play_again = input("Play again?")

#Rock outcome

            elif p_choice == "Rock" and cpu_choice == "Paper":
                print("You Lose!")
                play_again = input("Play again?")
            elif p_choice == "Rock" and cpu_choice == "Scissors":
                print("You Win!")
                play_again = input("Play again?")

#Paper outcome

            elif p_choice == "Paper" and cpu_choice == "Scissors":
                print("You Lose!")
                play_again = input("Play again?")
            elif p_choice == "Paper" and cpu_choice == "Rock":
                print("You Win!")
                play_again = input("Play again?")

#Scissors outcome

            elif p_choice == "Scissors" and cpu_choice == "Rock":
                print("You Lose!")
                play_again = input("Play again?")
            elif p_choice == "Scissors" and cpu_choice == "Paper":
                print("You Win!")
                play_again = input("Play again?")

#Ask if you want to play again, then give input

            if play_again == "Yes":
                play()
            elif play_again == "No":
                print("Game Over")
                sys.exit()
            else:
                print("Please try again")
                play_again = input("play again?")
                return play_again

        compare()



#ask if player wants to start
def game_start():
    while True:
        begin = input("Would you like to play Rock, Paper, Scissors?")
        if begin == "Yes":
            play()
            return begin
        while begin != "Yes":
            if begin == "No":
                print("Game Over")
                return begin
            else:
                print("Please try again")
                break

game_start()
