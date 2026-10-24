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

id1 = info1["id"]
height1 = info1["height"]
weight1 = info1["weight"]

id2 = info2["id"]
height2 = info2["height"]
weight2 = info2["weight"]

id3 = info3["id"]
height3 = info3["height"]
weight3 = info3["weight"]

id4 = info4["id"]
height4 = info4["height"]
weight4 = info4["weight"]

id5 = info5["id"]
height5 = info5["height"]
weight5 = info5["weight"]


print("=-" * 25)
print("ID: ",id1)
print("height: ",height1)
print("weight: ",weight1)
guest1 = input("Who's that Pokemon!?")
if guest1 == "bulbasaur":{
    print("That's right! It's BULBASAUR" )
} 
else:{
    print("Wrong! It's BULBASAUR")
}
    
    

print("=-" * 25)
print("ID: ",id2)
print("height: ",height2)
print("weight: ",weight2)
guest2 = input("Who's that Pokemon!?")
if guest2 == "caterpie":{
    print("That's right! It's CATERPIE!" )
} 
else:{
    print("Wrong! It's CATERPIE!")
}

print("=-" * 25)
print("ID: ",id3)
print("height: ",height3)
print("weight: ",weight3)
guest3 = input("Who's that Pokemon!?")
if guest3 == "charmeleon":{
    print("That's right! It's CHARMELEON!" )
} 
else:{
    print("Wrong! It's CHARMELEON!")
}

print("=-" * 25)
print("ID: ",id4)
print("height: ",height4)
print("weight: ",weight4)
guest4 = input("Who's that Pokemon!?")
if guest4 == "mew":{
    print("That's right! It's MEW!" )
} 
else:{
    print("Wrong! It's MEW!")
}

print("=-" * 25)
print("ID: ",id5)
print("height: ",height5)
print("weight: ",weight5)
guest5 = input("Who's that Pokemon!?")
if guest5 == "mewtwo":{
    print("That's right! It's MEWTWO!" )
} 
else:{
    print("Wrong! It's MEWTWO!")
}