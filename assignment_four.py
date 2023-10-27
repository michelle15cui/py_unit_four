# name: Michelle Cui
# date: 10.27.2023
# purpose: Create a math facts review game
import random

max_num = int(input("what's your maximum number of this function?(it has to be between 5 and 20): "))
random.randint(1, int(max_num))
# This step is asking the user's maximum number and define that is required for this function.

if max_num < 5 or max_num > 20:
    print("this is not included.")
# This step can tell the user when the number is put is not between the interval between 5 and 20.

else:
    first = random.randint(1, max_num)
    second = random.randint(1, max_num)
# This step can define the first number and second number to let them all stay between 5 and 20.

    option = input("What calculation way you want to practice?(choose from + - *): ")
# This step is asking for the calculation way that the user want to practice.

    if option == "+":
        print("what is ", first, "+", second, "?")
        answer = input("Enter answer: ")
# This step asked the user to answer the question that's given by python.

        if int(answer) == first + second:
            print("You are right!")
# This step can tell the user if they made the right answer.

        else:
            print("Sorry, you are wrong, the right answer is", first + second)
# This step can tell the user if the answer is wrong and tell them the right answer.

    elif option == "-":
        print("what is ", first, "-", second, "?")
        answer = input("Enter answer: ")
        # This step asked the user to answer the question that's given by python.

        if int(answer) == first - second:
            print("You are right!")
        # This step can tell the user if they made the right answer.

        else:
            print("Sorry, you are wrong, the right answer is", first - second)
    # This step can tell the user if the answer is wrong and tell them the right answer.

    elif option == "*":
        print("what is ", first, "*", second, "?")
        answer = input("Enter answer: ")
        # This step asked the user to answer the question that's given by python.

        if int(answer) == first * second:
            print("You are right!")
        # This step can tell the user if they made the right answer.

        else:
            print("Sorry, you are wrong, the right answer is", first * second)
    # This step can tell the user if the answer is wrong and tell them the right answer.

    else:
        print("What is ", first, "+", second, "?", "(because you didn't type in + - * so the calculation is automatically add)")
        answer = input ("Enter answer: ")
# This step can make the function turn into a addition if the user entered a wrong symbol.

        if int(answer) == first + second:
            print("You are right!")
# This step can tell the user if they made the right answer.

        else:
            print("Sorry, you are wrong, the right answer is", first + second)
# This step can tell the user if they made the wrong answer, and it's also gave the user the right answer.
