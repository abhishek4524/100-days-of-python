#Functions 

def calculateGMean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if (a > b):
        print(a , "is greater then", b)
    elif (a < b):
        print(a, "is less then", b)
    else:
        print(a , "is equal to", b)

def isLesser(a, b):
    pass

isGreater(5,9)
calculateGMean(5,9)
