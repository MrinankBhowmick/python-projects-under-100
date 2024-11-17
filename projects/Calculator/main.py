"""imports the os and time modules from the Python Standard Library.
The os module provides a way of using operating system dependent functionality,
like reading or writing to the file system.
The time module provides various time-related functions, like getting the current
time or pausing the execution of the script."""

import os
import time


def addition():
    """This function asks the user to enter a series of numbers separated by spaces.
    It then adds all the numbers together and returns the result."""
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums)


def subtraction():
    """This function asks the user to enter two numbers.
    It then subtracts the second number from the first and returns the result."""
    n_1 = float(input("Enter first number: "))
    n_2 = float(input("Enter second number: "))

    return n_1 - n_2


def multiplication():
    """Function asks user to enter a series of numbers separated by spaces.
    Then multiply all the numbers together and returns the result."""

    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    result = 1
    for num in nums:
        result *= num
    return result


def division():
    """Function divide two numbers"""
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if n2 == 0:
        print("Invalid entry")
        return "Invalid entry"
    print(n1 / n2)

    return n1 / n2


def average():
    """This function takes space separated number series and then convert it to a list.
    Then calculates the average of that list of numbers."""

    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums) / len(nums)


def factorial(num):
    """
    Function to calculate the factorial of a number.

    Takes a number as an argument, calculates the factorial of the number,
    and returns the result.
    """
    answer = 1
    for i in range(num):
        answer *= i + 1
    return answer


def complex_arithmetic():
    """
    Function to execute complex arithmetic operations such as addition, subtraction, multiplication, and division.

    Asks the user to choose the operation and input the complex numbers as real and imaginary parts,
    performs the operation, and returns the result.
    """
    print("Enter '1' for complex addition")
    print("Enter '2' for complex subtraction")
    print("Enter '3' for complex multiplication")
    print("Enter '4' for complex division")
    choice = input("enter your choice")
    if choice == "1":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sum = 0
        imag_sum = 0
        for i in range(0, len(nums) - 1, 2):
            real_sum += nums[i]
        for i in range(2, len(nums) - 1, 2):
            imag_sum += nums[i]
        imag_sum += nums[-1]
        return f"{real_sum}+ i{imag_sum}"

    elif choice == "2":
        nums = list(map(int, input("Enter all numbers separated by space: ").split()))
        real_sub = nums[0]
        imag_sub = nums[1]
        for i in range(2, len(nums) - 1, 2):
            real_sub -= nums[i]
        for i in range(3, len(nums) - 1, 2):
            imag_sub -= nums[i]
        imag_sub -= nums[-1]
        return f"{real_sub}+ i{imag_sub}"

    elif choice == "3":
        nums = list(
            map(
                int,
                input(
                    "Enter all numbers separated by space maximum 4 elements: "
                ).split(),
            )
        )
        real = nums[0] * nums[2] - nums[1] * nums[3]
        imag = nums[0] * nums[3] + nums[2] * nums[1]
        return f"{real}+ i{imag}"

    elif choice == "4":
        nums = list(
            map(
                int,
                input(
                    "Enter all numbers separated by space maximum 4 elements: "
                ).split(),
            )
        )
        real = (nums[0] * nums[2] + nums[1] * nums[3]) / (nums[2] ** 2 + nums[3] ** 2)
        imag = (nums[1] * nums[2] - nums[0] * nums[3]) / (nums[2] ** 2 + nums[3] ** 2)
        return f"{real}+ i{imag}"


def binomial(num):
    """
    Function to calculate the binomial coefficient.

    Takes two numbers as arguments, calculates the binomial coefficient using the formula n!/(k!(n-k)!),
    and returns the result.
    """
    result = factorial(num[0]) / (factorial(num[1]) * factorial(num[0] - num[1]))
    return result


c = 0
while c != "-1":
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")
    print("Enter '6' for factorial")
    print("Enter '7' for complex arithmetic")
    print("ENter '8'  for binomial")
    print("Enter '-1' to exit.\n")

    c = input("Your choice is: ")
    if c == "1":
        res = addition()
    elif c == "2":
        res = subtraction()
    elif c == "3":
        res = multiplication()
    elif c == "4":
        res = division()
        if res == "Invalid entry":
            continue
    elif c == "5":
        res = average()
    elif c == "6":
        num = int(input("enter the number: "))
        if num < 0:
            print("Invalid entry")
            continue
        res = factorial(num)
    elif c == "7":
        os.system("cls||clear")
        res = complex_arithmetic()
    elif c == "8":
        num = list(map(int, input("Enter the number separated by space").split()))
        if num[0] < num[1]:
            print("Invalid entry")
            continue
        res = binomial(num)
    elif c == "-1":
        print("Thank you for using the calculator!")
        break
    else:
        print("Sorry, invalid option!")
    os.system("cls||clear")
    print(f"The answer is {res}")
    print("Waiting for 5 seconds before next prompt window")
    time.sleep(5)
    os.system("cls||clear")
