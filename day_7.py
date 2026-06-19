# a = int(input("Enter your age : "))
# print("Your age is : ", a )

# if a >= 18:
#     print("You can drive")
# else:
#     print("You cannot drive")

#Exercuse : Greeting 
import time 
timestamp = time.strftime("%H")
if timestamp < "12":
    print("Good Morning")
elif timestamp < "18":
    print("Good Afternoon")
elif timestamp < "21":
    print("Good Evening")
else:
    print("Good Night")