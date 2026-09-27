"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Dhayle Tabamo]
Date: [September 27, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Control flows are pretty straight forward, they act like a condition the code will follow if certain conditions were met.]


============================================
KEY VOCABULARY
============================================
- condition: this is the key point of this lesson, the conditions were dictated by if / elif / else.
- if / elif / else: this what's called the conditional statements they dictate what will the code do depending on the conditions.
- comparison operator: this go hand in hand with conditional statements(==, !=, <, >, <=, >=).
- boolean expression: any expression that dictates if it was true or fals, it could be outside of conditional statements but usually used inside.
- logical operators: this is like comparison operator they help conditional statements (and, or, not).
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
age = input("enter your age: ")

if age >= "18" and age <= "29":
    print("young adult")
elif age >= "30" and age <= "49":
    print("middle aged person")
elif age >= "50" and age <= "90":
    print("ancient")
elif age < "18" :
    print("weed")
else:
    print("did you enjoy all of it?")
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[not knowing logical operators can stack meaning you can make more than 2 logical condition in a conditional statment]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
