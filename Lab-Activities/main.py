import requests
import json
import random


pmon = random.sample(range(2, 1026), 5)
#https://pokeapi.co/api/v2/pokemon/1 <-- change this to change the pokemon dawg.
try:
    pokemon1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pmon[0]}")
    if pokemon1.status_code != 200:
        raise ValueError(f"HTTP{pokemon1.status_code}") 
    info1 = pokemon1.json()
    if pokemon1.status_code == 200:
        print(f"P1_status: {pokemon1.status_code} : OK")

except ValueError as p1:
    print(f"There is an error occured, failed to fetch{p1}")
    info1 = None

try:
    pokemon2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pmon[1]}")
    if pokemon2.status_code !=200:
        raise ValueError(f"HTTP{pokemon2.status_code}")
    info2 = pokemon2.json()
    if pokemon2.status_code == 200:
        print(f"P2_status: {pokemon2.status_code} : OK")

except ValueError as p2:
    print(f"There is an error occured, failed to fetch{p2}")
    info2 = None

try:
    pokemon3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pmon[2]}")
    if pokemon3.status_code != 200:
        raise ValueError(f"HTTP{pokemon3.status_code}")
    info3 = pokemon3.json()
    if pokemon3.status_code == 200:
        print(f"P3_status: {pokemon3.status_code} : OK")

except ValueError as p3:
    print(f"There is an error occured, failed to fetch{p3}")
    info3 = None

try:
    pokemon4 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pmon[3]}")
    if pokemon4.status_code !=200:
        raise ValueError(f"HTTP{pokemon4.status_code}")
    info4 = pokemon4.json()
    if pokemon4.status_code == 200:
        print(f"P4_status: {pokemon4.status_code} : OK")

except ValueError as p4:
    print(f"There is an error occured, failed to fetch{p4}")
    info4 = None

try:
    pokemon5 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pmon[4]}")
    if pokemon5.status_code != 200:
        raise ValueError(f"HTTP{pokemon5.status_code}")
    info5 = pokemon5.json()
    if pokemon5.status_code == 200:
        print(f"P5_status: {pokemon5.status_code} : OK")

except ValueError as p5:
    print(f"There is an error occured, failed to fetch{p5}")
    info5 = None

print("=-" * 25)
print("                      START!")

mvlimit = 4 #the 4 moves the pokemon could learn this could include hm and tm not just the level up moves.
score = 0

pname1 = info1["name"]
id1 = info1["id"]
t1 = info1["types"]
type1 = [t1["type"]["name"] for t1 in info1["types"]]
height1 = info1["height"]
weight1 = info1["weight"]
abilities1 = info1["abilities"]
ability1 = [abilities1["ability"]["name"] for abilities1 in info1["abilities"]]
moves1 = info1["moves"]
move1 = [moves1["move"]["name"] for moves1 in info1["moves"][:mvlimit]]

pname2 = info2["name"]
id2 = info2["id"]
t2 = info2["types"]
type2 = [t2["type"]["name"] for t2 in info2["types"]]
height2 = info2["height"]
weight2 = info2["weight"]
abilities2 = info2["abilities"]
ability2 = [abilities2["ability"]["name"] for abilities2 in info2["abilities"]]
moves2 = info2["moves"]
move2 = [moves2["move"]["name"] for moves2 in info2["moves"][:mvlimit]]

pname3 = info3["name"]
id3 = info3["id"]
t3 = info3["types"]
type3 = [t3["type"]["name"] for t3 in info3["types"]]
height3 = info3["height"]
weight3 = info3["weight"]
abilities3 = info3["abilities"]
ability3 = [abilities3["ability"]["name"] for abilities3 in info3["abilities"]]
moves3 = info3["moves"]
move3 = [moves3["move"]["name"] for moves3 in info3["moves"][:mvlimit]]

pname4 = info4["name"]
id4 = info4["id"]
t4 = info4["types"]
type4 = [t4["type"]["name"] for t4 in info4["types"]]
height4 = info4["height"]
weight4 = info4["weight"]
abilities4 = info4["abilities"]
ability4 = [abilities4["ability"]["name"] for abilities4 in info4["abilities"]]
moves4 = info4["moves"]
move4 = [moves4["move"]["name"] for moves4 in info4["moves"][:mvlimit]]

pname5 = info5["name"]
id5 = info5["id"]
t5 = info5["types"]
type5 = [t5["type"]["name"] for t5 in info5["types"]]
height5 = info5["height"]
weight5 = info5["weight"]
abilities5 = info5["abilities"]
ability5 = [abilities5["ability"]["name"] for abilities5 in info5["abilities"]]
moves5 = info5["moves"]
move5 = [moves5["move"]["name"] for moves5 in info5["moves"][:mvlimit]]

tries1 = 3
tries2 = 3
tries3 = 3
tries4 = 3
tries5 = 3

while True:
    print("=-" * 25)
    print("ID: ",id1)
    print("Type",type1)
    print("Height: ",height1)
    print("Weight: ",weight1)
    print("Abilities: ",ability1)
    print("Moves: ", move1)

    try:
        guest1 = input("Who's that Pokemon!? \n").lower()
        

        if not guest1.replace("-", "").isalpha():
            raise ValueError(guest1)

        if guest1 == pname1:
            print(f"That's right! It's {guest1}!" )
            score +=1
            break
        elif guest1 != pname1:
            
            tries1 -=1
            
            if tries1 == 0:
                print(f"Wrong! It's {pname1}!")
                print("No more tries left, procceding...")
                break
            print(f"Wrong! guess again! {tries1} tries left")
        
    except ValueError as a:
        print(f"There is no known Pokemon has a name that starts with '{a}'!")   
        
while True:
    print("=-" * 25)
    print("ID: ",id2) 
    print("Type",type2)
    print("Height: ",height2)
    print("Weight: ",weight2)
    print("Abilities: ",ability2)
    print("Moves: ", move2)

    try:
        guest2 = input("Who's that Pokemon!? \n").lower()
        
        if not guest2.replace("-", "").isalpha():
            raise ValueError(guest2)

        if guest2 == pname2:
            print(f"That's right! It's {guest2}!" )
            score +=1
            break
        elif guest2 != pname2:
            
            tries2 -=1
            
            if tries2 == 0:
                print(f"Wrong! It's {pname2}!")
                print("No more tries left, procceding...")
                break 
            print(f"Wrong! guess again! {tries2} tries left")

    except ValueError as b:
        print(f"There is no known Pokemon has a name that starts with '{b}'!")   

while True:
    print("=-" * 25)
    print("ID: ",id3)
    print("Type",type3)
    print("Height: ",height3)
    print("Weight: ",weight3)
    print("Abilities: ",ability3)
    print("Moves: ", move3)

    try:
        guest3 = input("Who's that Pokemon!? \n").lower()
        
        if not guest3.replace("-", "").isalpha():
            raise ValueError(guest3)
        
        if guest3 == pname3:
            print(f"That's right! It's {guest3}!" )
            score +=1
            break
        elif guest3 != pname3:
            
            tries3 -=1
            
            if tries3== 0:
                print(f"Wrong! It's {pname3}!")
                print("No more tries left, procceding...")
                break 
            print(f"Wrong! guess again! {tries3} tries left")

    except ValueError as c:
        print(f"There is no known Pokemon has a name that starts with '{c}'!")   

while True:
    print("=-" * 25)
    print("ID: ",id4)
    print("Type",type4)
    print("Height: ",height4)
    print("Weight: ",weight4)
    print("Abilities: ",ability4)
    print("Moves: ", move4)

    try:
        guest4 = input("Who's that Pokemon!? \n").lower()
        tries4 = 3
        if not guest4.replace("-", "").isalpha():
            raise ValueError(guest4)
        
        if guest4 == pname4:
            print(f"That's right! It's {guest4}!" )
            score +=1
            break
        elif guest4 != pname4:
            
            tries4 -=1
            
            if tries4 == 0:
                print(f"Wrong! It's {pname4}!")
                print("No more tries left, procceding...")
                break
            print(f"Wrong! guess again! {tries4} tries left")

    except ValueError as d:
        print(f"There is no known Pokemon has a name that starts with '{d}'!")   

while True:
    print("=-" * 25)
    print("ID: ",id5)
    print("Type",type5)
    print("Height: ",height5)
    print("Weight: ",weight5)
    print("Abilities: ",ability5)
    print("Moves: ", move5)

    try:
        guest5 = input("Who's that Pokemon!? \n").lower()
        tries5 = 3
        if not guest5.replace("-", "").isalpha():
            raise ValueError(guest5)
        
        if guest5 == pname5:
            print(f"That's right! It's {guest5}!" )
            score +=1
            break
        elif guest5 != pname5:
            
            tries5 -=1
            
            if tries5 == 0:
                print(f"Wrong! It's {pname5}!")
                print("No more tries left, procceding...")
                break
            print(f"Wrong! guess again! {tries5} tries left")

    except ValueError as e:
        print(f"There is no known Pokemon has a name that starts with '{e}'!")   

print("=-" * 25)
print(f"            You guessed {score} out of 5 Pokemons!")
print("\n                     GoodGame!")
print("=-" * 25)