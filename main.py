
# Basic Rock Paper Scissors Game
# Name: Aidana
# Date: 02/20/2026

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

# Possible choices in the game
choices = ['rock', 'paper', 'scissors']
# Mapping from number input to choice
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# Implement this function to get and validate the user's choice.
def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	# Use console.input and validate input (accept 1/2/3 or words)
	user_input = console.input("Enter your choice (rock/paper/scissors or 1/2/3): ").lower()
	if user_input in num_to_choice:
		return num_to_choice[user_input]
	elif user_input in choices:
		return user_input
	else:
		console.print("[bold red]Invalid input. Please try again.[/bold red]")
		return get_user_choice()

# Implement this function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	return random.choice(choices)
	

# Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice: # If both choices are the same, it's a tie
		return "tie"
	elif user_choice == "rock" and computer_choice == "scissors":
		return "user"
	elif user_choice == "scissors" and computer_choice == "paper":
		return "user"
	elif user_choice == "paper" and computer_choice == "rock":
		return "user"
	else:
		return "computer"
	

# Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	console.print(f"You choose [bold blue]{user_choice}[/bold blue]. Computer chooses [bold red]{computer_choice}[/bold red].")
	if winner == "user":
		console.print('[bold green]You win this round![/bold green]')
	elif winner == 'computer':
		console.print(f"[bold red]Computer wins this round![/bold red]")
	else:
		console.print(f"[bold yellow]It's a tie![/bold yellow]")

#  Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		# Get user and computer choices
		user_choice = get_user_choice()
		computer_choice = get_computer_choice()
		# Determine winner
		winner = determine_winner(user_choice, computer_choice)
		# Print round result
		print_round_result(user_choice, computer_choice, winner)
		console.print(f"Rounds number: {round_num}")
		# Update scores
		if winner == "user":
			user_score += 1
		elif winner == "computer":
			computer_score += 1
		
	# Print final scores and announce the overall winner
	console.print(f"-----Final scores-----")
	console.print(f"User's score: {user_score}")
	console.print(f"Computer's score: {computer_score}")
	print_round_result(user_choice, computer_choice, winner)

if __name__ == "__main__":
	main()
	
