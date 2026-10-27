"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a sentence.
# 2. Process: The program applies four different string methods to the sentence.
# 3. Out: The program displays four transformed versions of the sentence.
# 4. My four transformations, and when each is useful:
# strip() removes extra spaces at the beginning and end, useful for cleaning text.
# upper() changes all letters to uppercase, useful for titles or headings.
# lower() changes all letters to lowercase, useful for standardising text.
# title() capitalises the first letter of each word, useful for formatting names.


# Your code below
# I ask the user to enter a sentence.
sentence = input("Enter a sentence: ")

# I remove spaces at the beginning and end.
print("Without extra spaces:", sentence.strip())

# I convert the sentence to uppercase.
print("Uppercase:", sentence.upper())

# I convert the sentence to lowercase.
print("Lowercase:", sentence.lower())

# I capitalise the first letter of each word.
print("Title case:", sentence.title())