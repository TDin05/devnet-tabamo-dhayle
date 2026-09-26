"""
Module 2 — Lesson 1: Variables & Data Types
Student: [Dhayle Tabamo]
Date: [September 27, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[in this lesson we will discuss the variables(containers) and datatypes(the values)]


============================================
KEY VOCABULARY
============================================
- variable: a  container that can store with values with different types
- data type: a data type is the type of value that you store inside a variable(container) this can range from numbers, letters, and logic.
- int: an int is a data type that is a whole number or a number without decimal (1, 2, 3, 4, 5, etc.)
- float: a float is a data type that is a number with a decimal (3.14, 1.5, 2.718, etc.)
- string: a string is a data type that only contains letters ("this is a data type")
- boolean: a boolean is a return data type that tells you true or false
- list: a data type like a variable but can store multiple values
- tuple: it is like a list but once you put the value inside you cannot change the value (unless was turned to list to add a new value inside)
- dictionary: a data type like list but it stores the values inside a key
- set: is a data type structured like a dictionary but act like a tuple as it cannot be changed but can still add or remove values
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
a = int(5)
b = float(5.19)
c = str("you can declare the data type or not since python will do it for you anyway.")
d = bool(0)

print(a, b, c, d)

thislist = ["egg", "bacon", "hotdog"]
thistuple = ("mama", "papa", "you")
thisdic = {"name": "Dhayle",
"age": 20,
"lovelife": False
}
thisset = {"blade", "blunt", "pointed"}

print(thislist)
print(thistuple)
print(thisdic)
print(thisset)

# --- your code example goes here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I did not know  list, dictionary, tuple, and sets are data types]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
