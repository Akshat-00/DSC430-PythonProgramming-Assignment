# Name: Akshat Gaur
# Student ID: 2176685
# Date : 10/19/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/fchJikSfCxA

import random
import A0501_diceAndCups as diceAndCups

def greetUser():
    """
    Greets user
    Returns the name
    """
    print("\nHello and welcome to the Dice Game!\n")
    name = input("Please enter your name: ")
    return name

def Bet(balance):
    """
    Check sif the user enters an amount greater than remaining balance or in negative.
    Returns the amount user wants to bet
    """
    betAmount = int(input("\nHow much would you like to bet? $"))
    if betAmount > balance or betAmount < 0:                                
        print(f"\nPlease enter the bet amount between 0 and {balance} $")
        betAmount=Bet(balance)    # Calls the same function again to take the correct amount from the user
    return betAmount

def determineOutcome(total,goal,betAmount,balance):
    """
    Determine the outcome by comparing goal and total of the dice
    Returns the updated balance
    """
    print(f"The goal was {goal}.")
    if total == goal:                                                      # If the roll exactly matches the goal
        balance = balance + betAmount * 10
        print("\nJackpot!! You've matched the goal and won 10x your bet.")
    elif abs(goal - total) <= 3:                                           # If the roll is within 3 of the goal
        balance = balance + betAmount * 5
        print("\nThat was close! You've won 5x your bet.")
    elif abs(goal - total) <= 10:                                          # If the roll is within 10 of the goal
        balance = balance + betAmount * 2
        print("\nYou're not too far! You've won 2x your bet.")
    else:
        balance = balance - betAmount
        print("\nSorry, you didn't win this time.")
    return balance

def main():
    playerName= greetUser()                     # Calling greetUser function to get the name of the user

    balance = 100                               # Initializing Starting balance as 100

    play = input("\nWould you like to play a game? (yes/no): ").strip().lower() 
    if play != 'yes':                           # If user doesn't want to play
        print("\nThankyou. See you Again.")
        return 0

    while True:                                 # Runs till user wants

        print(f"\nHello, {playerName}! Your current balance is {balance} $")

        goal = random.randint(1, 100)           # Generate a random goal between 1 and 100
        betAmount = Bet(balance)                # Calling Bet function to get Beting amount from user

        # Ask the user how many of each die they'd like to roll
        sixSidedCount = int(input("\nHow many 6-sided dice would you like to roll? "))
        tenSidedCount = int(input("How many 10-sided dice would you like to roll? "))
        twentySidedCount = int(input("How many 20-sided dice would you like to roll? "))

        # Creates a new instance of class Cup from diceAndCups program and assigns it to cup
        cup = diceAndCups.Cup(sixSidedCount, tenSidedCount, twentySidedCount)
        cup.roll()  
        total = cup.getSum() # To get the total sum of rolled dice
        print(f"\nResult of the roll: {total}")

        balance = determineOutcome(total,goal,betAmount,balance)
        print(f"\n{playerName}'s Updated balance: {balance} $")

        play_again = input("\n\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print(f"Thanks for playing, {playerName}! Your final balance is {balance} $")

main()