import random

def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        result = random.randint(1, sides)
        results.append(result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    # Get user input for the number of sides on the dice
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice (e.g., 6 for a standard die): "))
            if sides < 1:
                raise ValueError("Number of sides must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Get user input for the number of rolls
    while True:
        try:
            rolls = int(input("Enter the number of rolls: "))
            if rolls < 1:
                raise ValueError("Number of rolls must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Roll the dice and display the results
    results = roll_dice(sides, rolls)
    print("\nRolling the dice...")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
