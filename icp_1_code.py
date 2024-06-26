# -*- coding: utf-8 -*-
"""700757217.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lvyHJw6zPdIluAMmx9ECvtzxNfTYSiJX

Write a python program for the following:

Input the string “Python” as a list of characters from console, delete at least 2 characters, reversethe resultant string and print it.
Sample input: •python
Sample output: •ntyp
"""

# Task 1: Manipulating Strings
input_string = input("Enter a string: ")  # Input the string
char_list = list(input_string)  # Convert the string to a list of characters

if len(char_list) >= 2:  # Ensure there are at least 2 characters to delete
    del char_list[:2]  # Delete the last two characters
    char_list.reverse()  # Reverse the list
    result = ''.join(char_list)  # Convert the list back to a string
    print("Modified and reversed string:", result)
else:
    print("String must have at least 2 characters to perform the operation.")

# Task 2: Arithmetic Operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check if num2 is not 0 to avoid division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

print("Arithmetic Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

"""Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’."""

def replace_python(sentence):
    replaced_sentence = sentence.replace("python", "pythons")
    return replaced_sentence

input_sentence = input("Enter a sentence: ")
modified_sentence = replace_python(input_sentence)
print("Modified sentence:", modified_sentence)

"""Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class."""

def calculate_class_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get input class score from the user
try:
    class_score = float(input("Enter the class score: "))
    if 0 <= class_score <= 100:
        letter_grade = calculate_class_grade(class_score)
        print("The letter grade for the score {:.2f} is: {}".format(class_score, letter_grade))
    else:
        print("Invalid score. Please enter a score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
