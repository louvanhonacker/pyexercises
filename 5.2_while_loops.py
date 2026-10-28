"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My stop condition, my attempt limit, my summary:

# setting the number of attempts
i = 0

# repeating until the correct answer or the maximum number of attempts
while i < 5:
    user_input = input("Guess the luxury brand: ").strip().upper()
    i = i + 1

    if user_input == "CHANEL":
        print("You found the correct word.")
        break
    elif i == 5:
        print("The maximum number of attempts has been reached.")
    else:
        print("Incorrect answer. Try again.")

# displaying the summary
print("This is the end of the loop.")
print("Number of attempts:", i)
