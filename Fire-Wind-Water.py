import sys
import random

tokens = 20
answer = input("Enter P to play or Q to quit : ").upper()
while answer != 'P' and answer != 'Q':
	print("Invalid answer.")
	answer = input("Enter P to play or Q to quit : ").upper()
while answer == 'P':
	playerChoice = input("Enter F to choose Fire, W to choose Wind or WA for Water : ").upper()
	while playerChoice != 'F' and playerChoice != 'W' and playerChoice != 'WA':
		print("Invalid answer.")
		playerChoice = input("Enter F to choose Fire, W to choose Winf or WA for water : ").upper()
	invalid = True
	while invalid:
		bet = input("Tokens available : {}. How many tokens do you want to bet ?\n".format(tokens))
		if not bet.isdecimal():
			print("Invalid bet, please try again.")
		else:
			bet = int(bet)
			if bet > tokens:
				print("You don't have enough tokens !")
			elif bet <= 0:
				print("You can not bet less than one chip !")
			else:
				invalid = False
	randint = random.randint(1,3)
	if randint == 1:
		botChoice = 'F'
		fullBotChoice = "fire"
	elif randint == 2:
		botChoice = 'w'
		fullBotChoice = "wind"
	elif randint ==3:
		botChoice = 'WA'
		fullBotChoice = "water"
	tokens -= bet
	if playerChoice == botChoice:
		print("The computer chose {}. Equality !".format(fullBotChoice))
		tokens += bet
	elif (playerChoice == 'F' and botChoice == 'WA') or (playerChoice == 'W' and botChoice == 'F') or (playerChoice == 'WA' and  botChoice == 'W'):
		print("The computer chose {}. You won !\nYou recover your bet and win {} tokens.".format(fullBotChoice, bet))
		tokens += bet*2
	else:
		print("The computer chose {}. you lost your bet, you still have {} tokens.".format(fullBotChoice, tokens))
		if tokens == 0:
			print("You have no more tokens.")
			sys.exit()
	print("Owned tokens : {}.".format(tokens))
	answer = input("Enter P to play or Q to quit : ").upper()
	while answer != 'P' and answer != 'Q':
		print("Invalid answer.")
		answer = input("Enter P to play or Q to quit : ").upper()
sys.exit()
