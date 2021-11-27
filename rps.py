from random import randint
import random


comp_wins = 0
player_win = 0

def choose_option():
    user_choice = input("Choose Rock, Paper or Scrissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S",]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_option()
    return user_choice

def computer_option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You choose rock. The Computer choose rock. you tied.")
        elif comp_choice == "p":
            print("You choose rock. The computer choose paper. you lose.")
            comp_win =+ 1

        elif comp_choice =="s": 
            print("You choose rock. The computer choose scissors. you win.")
            player_win += 1

        elif user_choice == "p":
            if comp_choice == "r":
                print("You choose paper. The computer choose rock. you win.")
                player_win += 1

            elif comp_choice =="p":
                print("You choose paper. The computer choose scrissors. you lose.")

            elif comp_choice =="s":
                print("You choose paper. The computer choose rock. you lose.")
                comp_win +=1

        elif user_choice == "s":
            if comp_choice == "r":
                print ("You choose scissors. The computer choose rock. you lose.")
                comp_win +=1
            elif comp_choice == "p":
                print("You choose Scissors. The computer choose paper. you win.")
                player_win += 1

            elif comp_choice == "s":
                print("You choose scissors. The computer choose scissors. you tied.")
                
    print("")
    print("player wins: " + str(player_win))
    print("computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to ply again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
