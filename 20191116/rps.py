
#
# for x in range(20):
#     print (  random.random()  )

# int(param) : when param is number string (e.g. "125", "30"), => makes it number,
import random
import math


def getRandomRPS() :
    return math.floor( random.random() * 3 ) + 1

def RPStoNumber(rps) :
    if (rps == "R"):
        return 1
    elif (rps == "P"):
        return 2
    else :
        return 3

R = 1
P = 2
S = 3
player = RPStoNumber (    input ("Lets play rock paper scissor. Choose R or P or S ")   )
print (" You chose", player)
print ("Alright Rock.. Paper... scissor... shoot")
Computer = getRandomRPS()



while player == Computer:
    print (" we tied, lets try again")
    player = RPStoNumber ( input ("Try again")   )
    continue

if (player) > (Computer):
    print ("you win")


if player < Computer:
    print("you are a loser :P")

# if player == "R" and Computer == "S" :
#     elif
