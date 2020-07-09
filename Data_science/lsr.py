import matplotlib.pyplot as plt

icecream = [120, 350, 76, 420, 55, 768, 123, 320, 44]
constantIcecream = [245, 233, 265, 310, 221, 225, 210, 250, 278]
temp = [55, 74, 56, 70, 55, 71, 56, 75, 56]

def get_mean (list):
    sum = 0
    for i in list :
        sum += i
    return sum / len(list)

def get_sd (list) :
    mean = get_mean(list)
    sum = 0
    for i in list:
        sum += (i-mean)**2
    return (sum / (len(list) - 1) ) ** 0.5

def get_R (listA, listB) :
    sum = 0
    meanA = get_mean(listA)
    meanB = get_mean(listB)
    sdA = get_sd(listA)
    sdB = get_sd(listB)
    for index in range(len(listA)):
        sum += ( (listA[index] - meanA ) / sdA ) * ( (listB[index] - meanB ) / sdB )
    return sum / (len(listA) - 1)

def get_LSR (listA, listB) :
    R = get_R(listA, listB)
    b = R * (get_sd(listB) / get_sd(listA))
    a = get_mean(listB) - b * get_mean(listA)
    return [a, b]

def draw_line (coefficients, data):
    twoPoints = [0, 0]
    twoPoints[0] = data[0] * coefficients[1] + coefficients[0]
    twoPoints[1] = data[1] * coefficients[1] + coefficients[0]
    return twoPoints


print(get_sd(temp))
# print( get_mean(icecream) )
print( get_sd (icecream) )
#
# print( get_mean(constantIcecream) )
print( get_sd (constantIcecream) )
print(get_LSR(icecream, temp))
print(get_LSR(constantIcecream, temp))

print(get_R(icecream, temp))
print(get_R(constantIcecream, temp))

plt.xlabel('temperature')
plt.ylabel('icecream')
plt.plot(temp, icecream, 'bs', temp, constantIcecream, 'r^')
plt.plot([55, 75], draw_line(get_LSR(temp, icecream), [55, 75]))
plt.plot([55, 75], draw_line(get_LSR(temp, constantIcecream), [55, 75]))
plt.show()
