# Factorial of a number

def factorial(num):

    if num == 0:
        return num
    elif num == 1 or num == 2:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact
        
num = int(input("Enter a number: "))

print("The factorial of", num, "is", factorial(num))