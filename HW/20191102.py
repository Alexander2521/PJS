start = 7
num = input(" I will multiply your number by 7,8,9,10,11,12,13,14,15 : ")

while(int(num) * start):
    print( int(num) * 8)
    start + 1
    if(start > 15):
        break
