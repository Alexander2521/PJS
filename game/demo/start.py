# Game : attacking game from COC

print("SUP")
print('ERC')
print("ELL")

# picking Cards.
print("Pick your Troops >> ")
# galaxy is better than iphone.
Troops = [
    {
        "name" : 'archer',
        'description' : 'JJALJJali',
        "health" : 1,
        "symbol" : 'A'
    },
    {
        "name" : 'giant',
        "description" : "Tanker",
        "health" : 10,
        "symbol" : "B"
    },
    {
        "name" : "minion",
        "description" : "flying JJALJJali",
        "health" : 2,
        "symbol" : "C"
    }
]

for card in Troops :
    print(card["symbol"] + ' : ' + card["name"])
