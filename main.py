import requests
import json

pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/1/") 
pokemon2 = requests.get("https://pokeapi.co/api/v2/pokemon/10/")
pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/5/")
pokemon4 = requests.get("https://pokeapi.co/api/v2/pokemon/151/")
pokemon5 = requests.get("https://pokeapi.co/api/v2/pokemon/150/")

info1 = pokemon1.json()
info2 = pokemon2.json()
info3 = pokemon3.json()
info4 = pokemon4.json()
info5 = pokemon5.json()

pname1 = info1["name"]
id1 = info1["id"]
height1 = info1["height"]
weight1 = info1["weight"]

pname2 = info2["name"]
id2 = info2["id"]
height2 = info2["height"]
weight2 = info2["weight"]

pname3 = info3["name"]
id3 = info3["id"]
height3 = info3["height"]
weight3 = info3["weight"]

pname4 = info4["name"]
id4 = info4["id"]
height4 = info4["height"]
weight4 = info4["weight"]

pname5 = info5["name"]
id5 = info5["id"]
height5 = info5["height"]
weight5 = info5["weight"]


print("=-" * 25)
print("ID: ",id1)
print("height: ",height1)
print("weight: ",weight1)

try:
    guest1 = input("Who's that Pokemon!? \n").lower()

    if not guest1.isalpha():
        raise ValueError(guest1)

    if guest1 == "bulbasaur":{
        print(f"That's right! It's {guest1}!" )
    } 
    else:{
        print(f"Wrong! It's {pname1}!")
    }
    
except ValueError as a:
    print(f"There is no known Pokemon has a name that starts with an {a}!")   
    

print("=-" * 25)
print("ID: ",id2)
print("height: ",height2)
print("weight: ",weight2)

try:
    guest2 = input("Who's that Pokemon!? \n").lower()
    
    if not guest2.isalpha():
        raise ValueError(guest2)

    if guest2.lower == "caterpie":{
        print(f"That's right! It's {guest2}!" )
    } 
    else:{
        print(f"Wrong! It's {pname2}!")
    }
    
except ValueError as b:
    print(f"There is no known Pokemon has a name that starts with an {b}!")   

print("=-" * 25)
print("ID: ",id3)
print("height: ",height3)
print("weight: ",weight3)

try:
    guest3 = input("Who's that Pokemon!? \n").lower()

    if not guest3.isalpha():
        raise ValueError(guest3)
    
    if guest3 == "charmeleon":{
        print(f"That's right! It's {guest3}!" )
    } 
    else:{
        print(f"Wrong! It's {pname3}!")
    }
    
except ValueError as c:
    print(f"There is no known Pokemon has a name that starts with {c}!")   

print("=-" * 25)
print("ID: ",id4)
print("height: ",height4)
print("weight: ",weight4)

try:
    guest4 = input("Who's that Pokemon!? \n").lower()

    if not guest4.isalpha():
        raise ValueError(guest4)
    
    if guest4 == "mew":{
        print(f"That's right! It's {guest4}!" )
    } 
    else:{
        print(f"Wrong! It's {pname4}!")
    }
    
except ValueError as d:
    print(f"There is no known Pokemon has a name that starts with {d}")   

print("=-" * 25)
print("ID: ",id5)
print("height: ",height5)
print("weight: ",weight5)

try:
    guest5 = input("Who's that Pokemon!? \n").lower()

    if not guest5.isalpha():
        raise ValueError(guest5)
    
    if guest5 == "mewtwo":{
        print(f"That's right! It's {guest5}!" )
    } 
    else:{
        print(f"Wrong! It's {pname5}!")
    }
    
except ValueError as e:
    print(f"There is no known Pokemon has a name that starts with {e}")   
print("=-" * 25)