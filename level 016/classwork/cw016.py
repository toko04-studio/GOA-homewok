# 1
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[3:])

# 2
text = "Hello, World!"

print(text[7:14])

# 3
colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "შავი"]

print(colors[:-2])

# 4
short_nums = [1, 2, 3, 4, 90, 8, 72, 31, 74]

sum_nums = 0

for num in short_nums:
    sum_nums += num

print(sum_nums)

number = [90, 81, 100, 23, 3, 98, 102, 90, 75]

# 5
get_highets = [90, 81, 100, 23, 3, 98, 102, 90, 75]

highest = get_highets[0]

for num in get_highets:
    if num > highest:
        highest = num

print(highest) 