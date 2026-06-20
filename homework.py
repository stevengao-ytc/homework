# In class, we have made a simple program that asks the user a random addition maths question.
# The program generates a random number between 1 to 10
# and then generates a second number between 1 and 10
# it asks the user what's the sum of the 2 numbers, and prints "Correct!" if the user gets it right

# TODO: Your task is to improvise this program so that
# it keeps asking the user until the user gets it right
# make the whole process into a function, and call this function 5 times (to ask 5 different random addition maths questions)

# Current program:
import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
number_sum = number1 + number2
user_input = input("What's " + str(number1) + "+" + str(number2) + "?")


if (int(user_input) == number_sum):
    print("Correct!")
    
    
