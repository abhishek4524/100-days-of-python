x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case _:
        print("x is ", x)