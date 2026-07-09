
weather = input("შეიყვანე ამინდი: ")

if weather == "მზიანი":
    print("ვივარჯიშებ გარეთ")

elif weather == "მოღრუბლული":
    print("ვივარჯიშებ გარეთ ოღონდ მოგვიანებით")

else:
    print("საერთოდ არ ვივარჯიშებ დღეს")



for number in range(1, 1000):
    if number == 461:
        print("ვიპოვე", number)
        break



for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i)
        break