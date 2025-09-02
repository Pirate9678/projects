import random

def roll_dice():
    return random.randint(1, 6)

def dice_simulator():
    print("🎲 Welcome to the Dice Simulator 🎲")
    while True:
        user_input = input("Press Enter to roll the dice or type 'q' to quit: ").lower()
        if user_input == 'q':
            print("Thanks for playing! Goodbye 👋")
            break
        else:
            print(f"You rolled: {roll_dice()}")

if __name__ == "__main__":
    dice_simulator()