# Game : attacking game from COC
MAX_Cards = 10
Choice = []


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
        "DPS" : 4
    },
    {
        "name" : 'giant',
        "description" : "Tanker",
        "health" : 10,
        "symbol" : "B",
        "DPS" : 5,
        "Velocity" : 10
    },
    {
        "name" : "minion",
        "description" : "flying JJALJJali",
        "health" : 2,
        "symbol" : "C",
        "DPS" : 3
    }
]

for card in Troops :
    print(card["symbol"] + ' : ' + card["name"] + ' : ' + card["description"])

for cardIndex in range(MAX_Cards) :
    Choice.append( input('pick your troops ').upper()  )

print(Choice)
print(" <<< Prepare For Battle >>> ")

print(" Noob        |       Decent      |       Alex")
input("pick your level")

]
# 시간제한
# defensive base
# health bar (in percentage)
# Select Level (click interface )

# Health : 0 ~ 100 %
# Tower : distance. -> 1/10 Health
# charcater chooses Tower Randomly.
# Level Design Required (distances)

# enzymes
