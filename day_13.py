#List in python
marks = [30, 50,40, "Abhishek", True, 6, 7 ,9 , 20]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

# print(marks[-3]) #Negative index
# print(marks[len(marks)-3]) #Positive index
# print(marks[5-3]) #Positive index
# print(marks[2]) #Positive index

if 5 in marks:
    print("Yes")
else:
    print("NO")

#Same thing apply for string
if "bhi" in "Abhishek":
    print("YEs")

print(marks)
print(marks[1:])
print(marks[1:-1])
print(marks[1:6:2])


lst = [i for i in range(4)]
print(lst)

lst1 = [i*i for i in range(10) if i%2==0]
print(lst1)