"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# 1. In:
# 2. Process, problem by problem:
# 3. Out:
# 4. How I decide which word is the last name:


# Your code below
# Open names.txt and read all the lines
with open("names.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Create an empty list to store the cleaned names
people = []

# Clean each line
for line in lines:

    # Remove unnecessary spaces
    line = line.strip()

    # Ignore empty lines
    if line == "":
        continue

    # Split the name into separate words
    parts = line.split()

    # Handle names with two words
    if len(parts) == 2:
        first_name = parts[0].capitalize()
        last_name = parts[1].capitalize()

    # Handle the name Guido van Rossum
    elif len(parts) == 3 and parts[1].lower() == "van":
        first_name = parts[0].capitalize()
        last_name = "van " + parts[2].capitalize()

    else:
        print("Unexpected name format:", line)
        continue

    # Add the cleaned name to the list
    people.append((last_name, first_name))

# Sort the names alphabetically by last name
people.sort(key=lambda person: person[0].casefold())

# Create a new file with the cleaned and sorted names
with open("cleaned_names.txt", "w", encoding="utf-8") as file:

    for last_name, first_name in people:
        file.write(first_name + " " + last_name + "\n")

# Display the result
print("Cleaning completed!")
print("Number of names:", len(people))
print("The result is saved in cleaned_names.txt")
