from dice_roll import roll_dice

def main():
    print("🎲 Welcome to the Dice Roller! (type 'quit' to exit)")

    while True:
        choice = input("\nHow many dice do you want to roll? ")

        if choice.lower() == "quit":
            print("Goodbye!")
            break

        if not choice.isdigit():
            print("Please enter a valid number or 'quit'.")
            continue

        num_dice = int(choice)

        sides = input("How many sides per die? (default 6): ")
        if sides.strip() == "":
            sides = 6
        elif sides.isdigit():
            sides = int(sides)
        else:
            print("Invalid input, using default 6 sides.")
            sides = 6

        rolls = roll_dice(num_dice, sides)
        print(f"You rolled: {rolls} (total = {sum(rolls)})")

# Make sure this only runs if executed directly
if __name__ == "__main__":
    main()