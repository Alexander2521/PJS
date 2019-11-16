# grade = {
# "English" : 48,
# "Math" : 12,
# "Chinese" : 4,
# "Biology" : 6,
# "EastAsianStudies" : 7
# }

course = ["English", "Science", "Math", "History", "Chinese"]
grade = []

for indexes in course :
    grade.append( float( input("What is your " + indexes + " scores?"))  )

print(grade)

# print( 48 + 12 + 4 + 6 + 7)

def getSum(paramlisttt):
    sum = 0
    for grade in paramlisttt :
        sum = sum + grade
    return sum


def getMean(paramlist) :
    # sum = 0
    # for scores in paramlist :
    #     sum = sum + scores
    return getSum(paramlist) / len(paramlist)

print ( getMean(grade)  )
