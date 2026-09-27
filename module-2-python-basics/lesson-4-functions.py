"""
Module 2 — Lesson 4: Functions
Student: [Dhayle Tabamo]
Date: [September 27, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[its a piece of reusable code, it can be called anytime if the function is in the same file,
if its not the you can still call it but only aailable if you import the file it was on.
Basically like a recipe card write it once, then whenever you want it instead of rewriting all the steps again]


============================================
KEY VOCABULARY
============================================
- function: a named, reusable block of code that performs a specific task. You define it once and can call it as many times as you want.
- def: the keyword used to define a new function in Python
- parameter: a placeholder variable listed in a function's definition that will receive a value when the function is called, e.g. the "name" in def greet(name):
- argument: the actual value you pass in when calling a function, which fills in for the parameter, e.g. greet("Dhayle") — "Dhayle" is the argument.
- return: a keyword used inside a function to send a value back out to wherever the function was called from. A function without a return statement just runs its code and gives back None.
- call (calling a function): actually running a function by writing its name followed by parentheses, e.g. greet("Dhayle").
(add more as needed)

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
def calculate_pay(hours, rate):          

    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        pay = regular + overtime
    else:
        pay = hours * rate
    return pay

print(calculate_pay(35, 12))
print(calculate_pay(45, 12))

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[Hardcoding variables in a function is a bad idea because it make the function reusable
 unless you change the variable inside the function again, better use of parameters next time.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""