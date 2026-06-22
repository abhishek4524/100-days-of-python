def average(a=5, b=8):
    print("The average is ", (a*b)/2)

#default argument
average()

#keyword argument
average(b= 10,a= 3)

#required arguments
average(a=5) #if a is not given

#Arbitrary arguments
def ave(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("Average is :", sum / len(numbers))
    return sum / len(numbers)

ave(56, 78, 1, 2)

#Keyword Arbitrary arguments
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname= "James")