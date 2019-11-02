# Q1
# using for / while loop, print 10000 prime numbers.

# lower = int(input("enter the low interval"))
# upper = int(input("enter the high interval"))
# for num in range(lower, upper +1):
#     if num>1:
#         for i in range(2, num) :
#             if(num%i)== 0:
#                 break
#             elif (i ==  num - 1 ):
#                 print(num)

# 79823

# primeNumList = [2]
#
# limit = int(input("enter the limit : "))
#
# for num in range(2, limit + 1) :
#     for i in primeNumList:
#         if (num % i) == 0 :
#             break
#         elif( i == primeNumList[ len(primeNumList) - 1 ] ) :
#             primeNumList.append(num)
#
# print (primeNumList)

# primeNumList = [2]
#
# count = int(input("enter the amount of prime numbers : "))
# num = 3
#
# while (count != len(primeNumList) ) :
#     for i in primeNumList:
#         if (num % i) == 0 :
#             break
#         elif( i == primeNumList[ len(primeNumList) - 1 ] ) :
#             primeNumList.append(num)
#     num = num + 1
#
# print (primeNumList)
