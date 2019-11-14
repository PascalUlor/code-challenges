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
    if cmd == "r":
        if ai_choice == "p":
            losses += 1
            print("You Lose!")
        if ai_choice == "s":
            wins += 1
            print("You Win!")
        if ai_choice == "r":
            ties += 1
            print("You Tie!")
    elif cmd == "p":
        if ai_choice == "s":
            losses += 1
            print("You Lose!")
        if ai_choice == "r":
            wins += 1
            print("You Win!")
        if ai_choice == "p":
            ties += 1
            print("You Tie!")
    elif cmd == "s":
        if ai_choice == "r":
            losses += 1
            print("You Lose!")
        if ai_choice == "p":
            wins += 1
            print("You Win!")
        if ai_choice == "s":
            ties += 1
            print("You Tie!")
    elif cmd == "q":
        print("Goodbye!")
        break
    else:
        print("I do not understand that command")
        
        
