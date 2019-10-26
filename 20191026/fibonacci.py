count = 100
start = 0

# 1 1 2 3 5 8 13

last1 = 1
last2 = 1


while(start < count):
    now = last1 + last2
    last1 = last2
    last2 = now
    print(now)
    start = start + 1

 # for numb in range(count):
 #     now = last1 + last2
 #     last1 = last2
 #     last2 = now
 #     # print(now)
 #     print(str(numb + 3) + "번째 : " + str(now))

 # last1 1   1   2
 # last2 1   2   3
 # now   2   3   5
