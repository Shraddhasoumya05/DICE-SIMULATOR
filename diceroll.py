import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Let's play the dice roll game!")
    print("The game will start when either player rolls a one.")
    print("The first player to roll a six after rolling a one wins!")
    print("If both players roll a three within 10 rounds, it's a tie.")
    
    round_count = 0
    player = None
    human_three = False
    bot_three = False
    
    while round_count < 10:
        input("Press Enter to roll the dice...")
        human_roll = roll_dice()
        bot_roll = roll_dice()
        
        print("\nYou rolled:", human_roll)
        print("Bot rolled:", bot_roll)
        
        if human_roll == 1 or bot_roll == 1:
            print("Game starts!")
            player = "Human" if human_roll == 1 else "Bot"
        
        if player == "Human":
            if human_roll == 6:
                print("Congratulations! You win!")
                return
            elif bot_roll == 3:
                bot_three = True
        elif player == "Bot":
            if bot_roll == 6:
                print("Bot wins!")
                return
            elif human_roll == 3:
                human_three = True
        
        if human_three and bot_three:
            print("\nGame Over!")
            print("Both players rolled a three within 10 rounds. It's a tie!")
            return
        
        round_count += 1
    
    print("\nGame Over!")
    print("Neither player rolled a six within 10 rounds. It's a tie!")

if __name__ == "__main__":
    main()




