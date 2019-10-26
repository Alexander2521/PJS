# range (a, b, c) => [a, a+c, a+2c, a+3c ... a+nc] so that a+nc < b < a+(n+1)c
# we want to make rangeCopy function which acts exactly same as range(a,b,c)

def rangeCopy (a, b, c) :
    returnList = []
    temp = a
    while (temp <= b) :
        returnList.append(temp)
        temp = temp + c
    return returnList


print( rangeCopy(1, 50, 7) )
