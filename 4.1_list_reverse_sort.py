"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of ten numbers from exercise 4.0.
# 2. Process: The program displays the list in four different orders and checks if the original list changes.
# 3. Out: The original list, the sorted list, the reverse sorted list, and the reversed list.
# 4. My four orders, and which ones modify the original:
# The original order does not modify the list.
# The sorted() function creates a new sorted list.
# The sort() method modifies the original list.
# The [::-1] operation creates a reversed copy without modifying the original.



# Your code below
# I create the original list from exercise 4.0.
list_of_numbers = [100, 90, 10, 70, 80, 60, 20, 30, 40, 50]

# I display the original list.
print("The original list:")
print(list_of_numbers)

# I display the list sorted from smallest to largest without changing the original.
print("The list sorted from smallest to largest:")
print(sorted(list_of_numbers))

# I display the list sorted from largest to smallest.
print("The list sorted from largest to smallest:")
print(sorted(list_of_numbers, reverse=True))

# I display the list in reverse order without sorting it.
print("The list in reverse order:")
print(list_of_numbers[::-1])

# I display the original list again to check that it has not changed.
print("The original list at the end:")
print(list_of_numbers)
