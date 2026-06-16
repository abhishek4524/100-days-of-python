print("This is a simple calculator program in python.")
input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")
attribute = input("Enter the operation you want to perform (+, -, *, /, //, **, %): ")

if attribute == "+" :
    result = float(input1) + float(input2)
    print("The result of addition is: ", result)
elif attribute == "-" :
    result = float(input1) - float(input2)
    print("The result of subtraction is: ", result)
elif attribute == "*" :
    result = float(input1) * float(input2)
    print("The result of multiplication is: ", result)
elif attribute == "/" :
    result = float(input1) / float(input2)
    print("The result of division is: ", result)
elif attribute == "//" :
    result = float(input1) // float(input2)
    print("The result of floar division is: ", result)
elif attribute == "**" :
    result = float(input1) ** float(input2)
    print("The result of exponestion is: ", result)
elif attribute == "%" :
    result = float(input1) % float(input2)
    print("The result of modulus is: ", result)
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")