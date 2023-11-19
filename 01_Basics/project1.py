# Adding of two numbers

# Approach 1
'''
num1 = 5
num2 = 10

sum = num1 + num2

print("Approach 1 -The sum of the two number is: ", sum)

'''
# Approach 2 

'''
num1 = input("First number: ")
num2 = input("Second number: ")

sum = float(num1) + float(num2)

print("Approach 2 - The sum of {0} and {1} is {2}:" .format(num1,num2, sum)) 

'''

# Approach 3

def sum(num1, num2):
    return num1 + num2

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("Approach 3 - The sum of {0} and {1} is {2}:" .format(num1,num2, sum(num1,num2)))