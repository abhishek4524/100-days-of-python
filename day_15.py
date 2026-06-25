# #Tuple in python
# tup = (1,3 ,4 ,75,6, "red")
# #It is immutable.
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[-1])
# print(tup[2])

# if 3 in tup:
#     print("Yes 3 is present in this tuple.")

# tup2 = tup[1:6]
# print(tup2)

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
#  print(countries)

# countries = ("Pakistan", "Afganistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

# res = len(countries2)
# print(res)

#Excercise : Koun banega crorepati


questions = [

    {
        "question": "1. What is the full form of HTTP?",
        "option1": "Hyper Text Transfer Protocol",
        "option2": "High Transfer Text Protocol",
        "option3": "Hyper Transfer Text Process",
        "option4": "Hyperlink Transfer Protocol",
        "answer": "Hyper Text Transfer Protocol"
    },

    {
        "question": "2. Which keyword is used to define a function in Python?",
        "option1": "func",
        "option2": "define",
        "option3": "def",
        "option4": "function",
        "answer": "def"
    },

    {
        "question": "3. Which data type is immutable in Python?",
        "option1": "List",
        "option2": "Dictionary",
        "option3": "Tuple",
        "option4": "Set",
        "answer": "Tuple"
    },

    {
        "question": "4. Which operator is used for exponentiation in Python?",
        "option1": "^",
        "option2": "**",
        "option3": "*",
        "option4": "//",
        "answer": "**"
    },

    {
        "question": "5. What is the output of print(type(10))?",
        "option1": "<class 'float'>",
        "option2": "<class 'str'>",
        "option3": "<class 'int'>",
        "option4": "<class 'list'>",
        "answer": "<class 'int'>"
    }

]

wining_amount = 0

print("Swagat hai aapka koun banega crorepati me :" )
for question in questions:
    print(question["question"])
    print(1, question["option1"])
    print(2, question["option2"])
    print(3, question["option3"])
    print(4, question["option4"])
    a = input("Enter answer of the question : ")
    if (a == question["answer"]):
        wining_amount+=10000

print("Aap ki jiti hui dhanrashi h : ", wining_amount)
    
    