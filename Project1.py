"""
Trying to make a program that can take a number and then a second number
and do whatever the input data tells it to do using functions

"""


def num1():
    num1.one = int(input("Enter a number less than 100: "))
    if num1.one > 100:
        print("That is not less than 100...")
        num1()
# using a function so we can call the first number


def num2():
    num2.two = int(input("Enter a second number less than 100: "))
    if num2.two > 100:
        print("That is not less than 100...")
        num2()
# using a function so we can call the second number


num1()
# calling function to initiate the program to get num1

num2()
# calling function to initiate the program to get num2


add = num1.one + num2.two
sub = num1.one - num2.two
div = num1.one / num2.two
mul = num1.one * num2.two
# defining the operations

fulfilled = 0
while fulfilled != 1:
    ans = input("Would you like to add, subtract, multiply, or divide these numbers?")
    if ans.lower() == "add":
        print(num1.one, "+", num2.two, "=", add)
        fulfilled += 1
    elif ans.lower() == "subtract":
        print(num1.one, "-", num2.two, "=", sub)
        fulfilled += 1
    elif ans.lower() == "multiply":
        print(num1.one, "*", num2.two, "=", mul)
        fulfilled += 1
    elif ans.lower() == "divide":
        print(num1.one, "/", num2.two, "=", div)
        fulfilled += 1
    else:
        print("Sorry that isn't a choice")
