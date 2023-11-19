# Find Maximim of two number in python

def maximum(num1, num2):

    if num1 >= num2:
        return num1
    else:
        return num2

num1 = input("First number: ")
num2 = input("Second number: ")

print("The Maximum Number between num1 and num2 is:", maximum(num1,num2))
