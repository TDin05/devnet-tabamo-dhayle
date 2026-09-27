"""
Module 2 — Lesson 3: Loops & Lists
Student: [Dhayle Tabamo]
Date: [September 27, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Okay I explain list in lesson 1 but sure here it is again.
list is like, well a list it stores multiple values inside 1 variable

now for loops these are like the conditional statements you make it do something till the requirements of the conditions are met
let's say you made a loop that tells loop this until you printed 100 i love you, the code only stops after completing the task.
or lets say you run a code indefenitely unless you stop it via conditions.]


============================================
KEY VOCABULARY
============================================
- list: a variabble that can store more than one value
- for loop: it can iterate or loop with certain amount of time set
- while loop: it will loop the code for uncertain amount of time until your conditions are met
- index: the position of an item in a list -1 indicates last 0 indicates the first 
- iteration: the loop you passed, 1 loop done = 1 iteration
- range: used in for loop, it tells the loop to do this much loops before stoping

(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

fruits = ["apple", "banana", "cherry", "banana", "date"]

for i, fruit in enumerate(fruits):      
    if fruit == "banana":
        continue                          
    if fruit == "date":
        break                             
    print(f"{i}: {fruit}")  
else:
    print("loop finished normally")             

# --- your code example goes here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[a range will always start from 0, lets say for i in range(5) and inside you want to print 1 to 5, the print will
print 0 to 4 instead, it can be fixed by stating for i in range(1, 6) so it will start from 1 then stop at 5.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
