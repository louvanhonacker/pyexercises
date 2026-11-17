
# ============================================================
# SURVIVE THE QUARTER - CROISSANT ROCKET
# Name: Lou Vanhonacker-Dutoit
# Group: 5
#
# QUESTION 1 - INPUT:
# The program reads scenarios_A.csv.
# The separator is a comma.
# The file contains 14 columns:
# ID, Scenario, OptionA, OptionB, OptionC,
# BudgetA, BudgetB, BudgetC,
# ReputationA, ReputationB, ReputationC,
# FeedbackA, FeedbackB, FeedbackC.
# The file contains the situation, three choices,
# their budget and reputation impacts, and feedback.
# Numerical impacts are written as integers.
#
# QUESTION 2 - PROCESS:
# 1. Ask the player's name.
# 2. Ask the player to choose a difficulty.
# 3. Set the starting budget and reputation.
# 4. Load and shuffle the scenarios.
# 5. Play 10 days.
# 6. Display the situation and three possible choices.
# 7. Ask the player to choose A, B or C.
# 8. Apply the budget and reputation changes.
# 9. Stop if the budget or reputation reaches zero.
# 10. Display the final result and save it.
#
# QUESTION 3 - OUTPUT:
# The player sees the daily situations, choices,
# feedback, budget and reputation.
# At the end, the program displays the final score,
# the player's title and the best and worst moves.
# results.csv stores name, budget, reputation,
# title and date for every completed game.
#
# QUESTION 4 - POSSIBLE ERRORS:
# 1. An invalid choice: ask again until A, B or C.
# 2. A missing CSV file: display an error message.
# 3. Incorrect numerical data: display an error message.
# 4. Budget or reputation at zero: stop the game.
# 5. Reputation above 100: limit it to 100.
#
# FEATURE D - DIFFICULTY:
# I chose difficulty because it gives the player
# a choice between an easy and a hard game.
# Easy starts with 15,000 EUR.
# Hard starts with 6,000 EUR.
# ============================================================

import csv
import random
from datetime import date
import os


# Ask the player for their name
def get_player_name():
    name = input("Enter your name: ").strip()

    while name == "":
        print("Please enter a valid name.")
        name = input("Enter your name: ").strip()

    return name


# Ask the player to choose the difficulty
def choose_difficulty():
    while True:
        difficulty = input(
            "Choose your difficulty (easy or hard): "
        ).strip().lower()

        if difficulty == "easy":
            return 15000

        elif difficulty == "hard":
            return 6000

        else:
            print("Invalid choice. Please type easy or hard.")


# Load all scenarios from the CSV file
def load_scenarios():
    scenarios = []

    with open("scenarios_A.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            scenarios.append(row)

    return scenarios


# Create the three possible options for one scenario
def create_options(scenario):
    options = {
        "A": (
            scenario["OptionA"],
            int(scenario["BudgetA"]),
            int(scenario["ReputationA"]),
            scenario["FeedbackA"]
        ),

        "B": (
            scenario["OptionB"],
            int(scenario["BudgetB"]),
            int(scenario["ReputationB"]),
            scenario["FeedbackB"]
        ),

        "C": (
            scenario["OptionC"],
            int(scenario["BudgetC"]),
            int(scenario["ReputationC"]),
            scenario["FeedbackC"]
        )
    }

    return options


# Apply the consequences of the player's choice
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option

    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)

    print("\n" + feedback)
    print("Budget change:", budget_change, "EUR")
    print("Reputation change:", reputation_change)

    return budget, reputation


# Ask the player to choose a valid option
def get_player_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()

        if choice in ["A", "B", "C"]:
            return choice

        print("Invalid choice. Please type A, B or C.")


# Calculate the player's final title
def get_title(score):
    if score < 95:
        return "Eternal Intern"

    elif score < 120:
        return "Growth Hacker"

    elif score < 140:
        return "CMO Material"

    else:
        return "Viral Legend"


# Save the game result in results.csv
def save_result(name, budget, reputation, title):
    file_exists = os.path.exists("results.csv")

    with open("results.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize("results.csv") == 0:
            writer.writerow([
                "Name",
                "Budget",
                "Reputation",
                "Title",
                "Date"
            ])

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            date.today()
        ])

    print("\nResult saved successfully in results.csv!")


# Display the best and worst moves
def show_best_and_worst(history):
    if len(history) == 0:
        return

    best_move = max(history)
    worst_move = min(history)

    print("\nBEST MOVE:")
    print(
        "Day", best_move[1],
        "-", best_move[2],
        "(+" + str(best_move[0]) + ")"
    )

    print("\nWORST MOVE:")
    print(
        "Day", worst_move[1],
        "-", worst_move[2],
        "(" + str(worst_move[0]) + ")"
    )


# Start and manage the game
def main():

    # Get the player's name and starting budget
    player_name = get_player_name()
    budget = choose_difficulty()
    reputation = 50

    print("\nWelcome to Croissant Rocket,", player_name)
    print("Your starting budget is:", budget, "EUR")
    print("Your starting reputation is:", reputation, "/100")

    # Load and shuffle the scenarios
    try:
        scenarios = load_scenarios()

    except FileNotFoundError:
        print("Error: scenarios_A.csv was not found.")
        return

    except (KeyError, ValueError):
        print("Error: the CSV file contains incorrect data.")
        return

    if len(scenarios) < 10:
        print("Error: at least 10 scenarios are required.")
        return

    random.shuffle(scenarios)

    # Keep track of every move during the game
    history = []

    # Play ten days
    for day in range(1, 11):

        scenario = scenarios[day - 1]

        try:
            options = create_options(scenario)

        except (KeyError, ValueError):
            print("Error: incorrect scenario data.")
            return

        print("\n" + "=" * 40)
        print("--- DAY", day, "---")
        print("=" * 40)

        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")

        print("\n" + scenario["Scenario"])

        # Display the three possible choices
        for letter in ["A", "B", "C"]:
            print(letter + ":", options[letter][0])

        # Ask for a valid choice
        choice = get_player_choice()

        selected_option = options[choice]

        # Apply the selected option
        budget, reputation = apply_choice(
            budget,
            reputation,
            selected_option
        )

        # Record the move as a tuple
        history.append((
            selected_option[2],
            day,
            selected_option[0]
        ))

        print("\nCurrent budget:", budget, "EUR")
        print("Current reputation:", reputation, "/100")

        # Check if the player has been fired
        if budget <= 0 or reputation <= 0:
            print("\nGAME OVER!")

            if budget <= 0:
                print("You have been fired because your budget reached zero.")

            if reputation <= 0:
                print("You have been fired because your reputation reached zero.")

            break

    # Display the final result
    print("\n" + "=" * 40)

    if budget <= 0 or reputation <= 0:
        title = "Fired"
        print("You have been fired!")

    else:
        print("Quarter survived!")

        score = reputation + budget // 200
        title = get_title(score)

        print("Final budget:", budget, "EUR")
        print("Final reputation:", reputation, "/100")
        print("Final score:", score)
        print(player_name + ", your title:", title)

    # Show the best and worst moves
    show_best_and_worst(history)

    # Save the result
    save_result(player_name, budget, reputation, title)


# Run the game
if __name__ == "__main__":
    main()
