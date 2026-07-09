# 2
num = 15

if num > 10:
    print("more than 10")
else:
    print("less than 10")


# 3
num = int(input("Enter a number: "))

if num == 15:
    print("equal to 15")
else:
    print("not equal to 15")


# 4
text = input("Enter a string: ")

if text == "group92":
    print("you are correct")
else:
    print("you are wrong")


# 5
for i in range(50, 101, 5):
    print(i)


# 6
for i in range(1):
    print("Toko Toko")


# 7
i = 20

while i <= 50:
    print(i)
    i += 1


# 8 (for)
for i in range(100):
    print(i)

# 8 (while)
i = 0
while i < 100:
    print(i)
    i += 1


# 9 (for)
for i in range(101):
    print(i)

# 9 (while)
i = 0
while i <= 100:
    print(i)
    i += 1


# 10 (for)
for i in range(10, 21):
    print(i)

# 10 (while)
i = 10
while i <= 20:
    print(i)
    i += 1


# 11 (for)
for i in range(100, 201, 5):
    print(i)

# 11 (while)
i = 100
while i <= 200:
    print(i)
    i += 5


# 12 (for)
for i in range(10, -1, -1):
    print(i)

# 12 (while)
i = 10
while i >= 0:
    print(i)
    i -= 1


# 13
num = float(input("Enter a number: "))

if num > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif num < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")


# 14
age = int(input("შეიყვანე ასაკი: "))

if age < 0:
    print("არასწორი ინფო")
elif age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")


# 15
num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
num3 = float(input("შეიყვანე მესამე რიცხვი: "))

print("უდიდესი რიცხვია:", max(num1, num2, num3))

# 16
day = int(input("შეიყვანე რიცხვი 1-დან 7-მდე: "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")


# 17
num = float(input("შეიყვანე რიცხვი: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2)


# 18
password = input("შეიყვანე პაროლი: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


# 19
num = int(input("შეიყვანე რიცხვი: "))
sum = 0

for i in range(1, num + 1):
    sum += i

print("ჯამი =", sum)


# 20
for ticket in range(1, 5001):
    if ticket == 2024:
        print("ჯეკპოტი! მომგებიანი ბილეთი ნაპოვნია")
        break


# 21
for i in range(1, 301):
    if i % 4 == 0 and i % 7 == 0:
        print(i)
        break


# 22
for i in range(1, 51):
    if i % 10 == 0:
        continue
    print(i)