# append() - ამატებს ელემენტს სიის ბოლოში
# insert() - ამატებს ელემენტს მითითებულ პოზიციაზე
# pop() - შლის ელემენტს სიიდან (ნაგულისხმევად ბოლო ელემენტს)


numbers = [10, 20, 30, 40, 50]
print("სიის სიგრძე:", len(numbers))


nums = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    nums.append(num)

print("რიცხვების სია:", nums)


colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()
print("განახლებული colors სია:", colors)


animals = ["dog", "cat", "elephant", "lion"]

animals.insert(1, "monkey")
print("განახლებული animals სია:", animals)


students = []

for i in range(3):
    name = input("შეიყვანე სტუდენტის სახელი: ")
    students.append(name)

students.insert(0, "Teacher")
students.pop()

print("სიის სიგრძე:", len(students))
print("საბოლოო სია:", students)