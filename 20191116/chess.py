chessboard = [
[0,1,0,1,0,1,0,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0] ]

# print (chessboard) : WRONG!!!


print(" ㅡ  ㅡ  ㅡ  ㅡ  ㅡ  ㅡ  ㅡ  ㅡ ")
for lines in chessboard :
    print("|", end = " ")
    for points in lines :
        print(str(points) + " |", end = " ")
    print()
    print(" ㅡ  ㅡ  ㅡ  ㅡ  ㅡ  ㅡ  ㅡ  ㅡ ")
