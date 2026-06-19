#Loops in python 
name = "Abhishek"

#For loop in python

for i in name :
    print(i)

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for i in range(0,50):
    print(i + 1, end=" ")

for i in range(0, 10, 2):
    print(i)

#while loop in python

while i <= 10:
    i = int(input("Enter a number:"))
    print(i)
print("Done with the loop")

count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("Count is zero now")


