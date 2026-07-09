# 1

name = input("შეიყვანე შენი სახელი: ")
print(name)


# 2

name = input("შეიყვანე სახელი: ")
surname = input("შეიყვანე გვარი: ")
age = input("შეიყვანე ასაკი: ")
city = input("შეიყვანე ქალაქი: ")
country = input("შეიყვანე ქვეყანა: ")

print(
    "ჩემი სახელია " + name +
    ", ჩემი გვარია " + surname +
    ", მე ვარ " + age +
    " წლის, ვცხოვრობ ქალაქ " + city +
    "-ში, ქვეყანაში " + country + "."
)


# 3

text = "Python"   # str
number = 25       # int
decimal = 3.14    # float

print(type(text))
print(type(number))
print(type(decimal))