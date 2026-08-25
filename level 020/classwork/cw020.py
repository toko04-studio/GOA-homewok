
# 1
name = input("შეიყვანე სახელი: ")
print(name.lower())

# 2
color = input("შეიყვანე საყვარელი ფერი: ")
print(color.upper())

# 3
city = input("შეიყვანე ქალაქი: ")
print(city.capitalize())

# 4
email = "student@university.ge"
print(email.find("@"))

# 5
word = "Programming"
print(word.find("r"))

# 6
sentence = "მე მიყვარს ვაშლი და მსხალი."
print(sentence.find("ბანანი"))

# 7
info = "Error 404: Page not found"
print(info.find("404"))

# 8
url = "https://www.google.com"
print(url.startswith("https://"))

# 9
phone = "+995555123456"
print(phone.startswith("+995"))

# 10
filename = "document.pdf"
print(filename.endswith(".pdf"))

# 11
text = input("შეიყვანე წინადადება: ")
print(text.endswith("?"))

# 12
word = "abracadabra"
print(word.count("a"))

# 13
data = "100110101011"
print(data.count("1"))

# 14
products = "პური,რძე,კვერცხი,ყველი"
products_list = products.split(",")
print(products_list)

# 15
text = "hello world"
print(len(text))

