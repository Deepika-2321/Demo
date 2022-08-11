import random

def guess(x):
	random_number=random.randint(5,x)
	guess=0
	while guess!=random_number:
		guess=int(input(f"Guess a number between 5 and {x}: "))
		if guess < random_number:
			print("Sorry, you have guessed wrong.The number is low.")
		elif guess > random_number:
			print("Sorry, you have guessed wrong.The number is high.")
				
	print("Yayy! You have guessed right!")
	

def computer_guess(x):
	low=5
	high=x
	feedback=''
	while feedback!='c':
		if low!=high:
			guess=random.randint(low,high)
		else:
			guess=low #could also be high because low=high
		feedback=input(f"Is {guess} too high (H), too low (L),or correct (C): ").lower()
		if feedback=='h':
			high=guess-1
		elif feedback=='l':
			low=guess+1
		
	print("Yayy!Computer guessed your number correctly")
		
computer_guess(100)
