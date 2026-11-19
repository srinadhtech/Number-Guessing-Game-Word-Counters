import random

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


def word_counter():
    print("\n--- Word Counter ---")

    filename = input("Enter filename (example: text.txt): ")

    try:
        with open(filename, "r") as file:
            text = file.read()

        words = text.split()
        characters = len(text)
        lines = len(text.splitlines())

        print("\nFile Statistics:")
        print("Words:", len(words))
        print("Characters:", characters)
        print("Lines:", lines)

    except FileNotFoundError:
        print("File not found! Please check the filename.")


def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


main()