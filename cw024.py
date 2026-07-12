
def greet(name):
    print("Hello World!")
    print("Hello", name)


def double(number):
    answer = number * number
    return answer


def checkOdd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"


def BMI(height, weight):
    answer = weight / (height * height)
    return answer
