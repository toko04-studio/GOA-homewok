# 1

# >  (მეტია)
print(10 > 5)
print(20 > 15)
print(7 > 3)
print(100 > 50)
print(9 > 1)

# <  (ნაკლებია)
print(5 < 10)
print(15 < 20)
print(3 < 7)
print(50 < 100)
print(1 < 9)

# == (ტოლია)
print(5 == 5)
print(10 == 10)
print(7 == 7)
print(100 == 100)
print(0 == 0)

# != (არ უდრის)
print(5 != 10)
print(7 != 3)
print(20 != 15)
print(1 != 2)
print(100 != 99)

# >= (მეტია ან ტოლია)
print(10 >= 10)
print(15 >= 10)
print(20 >= 20)
print(30 >= 25)
print(50 >= 50)

# <= (ნაკლებია ან ტოლია)
print(10 <= 10)
print(5 <= 10)
print(20 <= 20)
print(15 <= 25)
print(50 <= 100)


# 2

# Logical Operators (ლოგიკური ოპერატორები) გამოიყენება
# რამდენიმე პირობის ერთმანეთთან დასაკავშირებლად.

# and - აბრუნებს True-ს მხოლოდ მაშინ,
# თუ ორივე პირობა True არის.

# or - აბრუნებს True-ს მაშინ,
# თუ ერთ-ერთი პირობა მაინც True არის.

# not - ცვლის შედეგს:
# True -> False
# False -> True


# 3

# and
print(True and True)
print(10 > 5 and 20 > 10)
print(7 == 7 and 3 < 5)

# or
print(True or False)
print(10 < 5 or 20 > 10)
print(7 != 8 or 2 > 10)

# not
print(not True)
print(not False)
print(not (10 > 5))


# 4

my_number = 50

user_number = int(input("შეიყვანე რიცხვი: "))

print(user_number > my_number)


# 5

my_name = "Toko"

user_name = input("შეიყვანე სახელი: ")

print(user_name == my_name)


# 6

age = int(input("შეიყვანე ასაკი: "))

print(age > 18)