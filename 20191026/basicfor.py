# for numb in [1, 3, 5, 7, 8] :
#     print(numb)
#
# print('for loop finished!')

# for numb in range(2, 1000, 2):
#     print(numb)



# quiz : print all 28938 positive even numbers beginning from 2.

# count = 28938
#
# for numb in range(2, 57876, 2):
#      print(numb)


count = int(input("type the number"))

# for numb in range(2, count * 2 , 2):
#     print(numb)

for numb in range(count): # range(count) = [0, 1, 2, ... count]
    print (numb * 2 + 2)
