import random
# create a simple rock paper scisors game in python

# Create a rock/paper/scissors REPL
# Have a computer AI to play agains us
# keep track of a score
# RULES: r beats s, s beats p, p beats r

# set up some sentinal values for variables
wins = 0
losses = 0
ties = 0
# set up a list of possible choices
choices = ["r", "p", "s"]

# a function that compares choices
def compare_choices(player_choice, computer_choice):
    #test if player_choice is equal to computer_choice
    if player_choice == computer_choice:
        # return 0
        return 0
    # otherwise (if pc is r and cc is s) 
    # or (pc is p and cc is r) or
    # (pc s and cc is p)
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        # return 1
        return 1
    # otherwise
    else:
        # return -1
        return -1

# start a REPL
while True:
    # show score
    print(f"Score: {wins} - {losses} - {ties}")
    # take input from the player
    cmd = input("\nChoose r/p/s/q: ")
    # have the AI make a random choice of r/p/s
    ai_choice = choices[random.randrange(3)]
    # show the AI choice
    print(f"Computer Chose {ai_choice}")
    # conditional logic or commande
    # compare the choices
    results = compare_choices(cmd, ai_choice)

    if cmd == "q":
        print("Goodbye!")
        break
    if results == 1:
        wins += 1
        print("You Win!")
    elif results == -1:
        losses += 1
        print("You Lose!")
    elif results == 0:
        ties += 1
        print("You Tied!")
        
        
