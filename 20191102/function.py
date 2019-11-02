# input(param) : takes ( comments to be shown on the terminal - string1 ) as a parameter, returns ( user input - string2 ).
#               Work : shows string1 on the termnial, make user type something, and returns user input(string2).
# int() :  takes a string value (as a parameter), return an number value (Only integers)
        # Work :  changes string into number (only integer form)
# str() : opposite of int() OR float()
#
# printVal = 9
#
# def printTest ( a, b, c = 7 ):
#     print(a)
#     print(b)
#     print(c)
#     return a+b+c
#
# print ( printVal )
# print ( printTest(3, 5, 1) )
# print ( printTest( 6, 4 ))

# name = input ("Type your name : ")
# print (name)

# print(int("3") * 8)
# num = int("3")
# print (num + 8)

# start = 7
# num = input(" I will multiply your number by 7,8,9,10,11,12,13,14,15 : ")
#
# while(int(num) * start):
#     print( int(num) * 8)
#     start + 1
#     if(start > 15):
#         break

num = int(input(" I will multiply your number by 7,8,9,10,11,12,13,14,15 : "))

for i in range(7, 16):
    print (num * i)
