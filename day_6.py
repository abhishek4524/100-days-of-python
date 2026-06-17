# Strings are immutable, which means that they cannot be changed after they are created. However, you can create a new string by concatenating two or more strings together.
# When we apply any funtcion to a string , function creates a new copy of the string and applies the functoin to the new copy of the string. The original string remains unchanged.

name = "!!ABHishEk !!"
print(name)
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.lstrip("!"))
print(name.replace("Abhishek", "Kumar"))
print(name.split(" "))
print(name.capitalize())
print(len(name))
print(len(name.center(20)))
print(name.center(20))
print(name.count("!"))
print(name.endswith("!"))

str1 = "Welcome to the Console !!!!"
print(str1.endswith("to", 4, 10))

print(str1.find("to"))
print(str1.index("to")) 

print(str1.isalnum())
print(str1.isnumeric())
print(str1.isalpha())
print(str1.islower())
print(str1.isupper())

print(str1.isprintable())
str2 = "    "
print(str2.isspace())

print(str1.istitle())
print(str1.startswith("Wel"))
print(str1.swapcase())
print(str1.title())