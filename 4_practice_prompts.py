
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
variable1 = "clock"
variable2 = "boxes"
variable3 = "chairs"
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
fstring = f"There is a {variable1}, {variable2}, and {variable3} in the room."

# Familiarize yourself with the syntax of the print() function.
# Print your name.
print("Juana")
# Print today's date.
print("11-4-25")
# Print the name of your favorite movie.
print("Ice Age")
# Print your name and age on separate lines using a single print() function.
print("Juana")
print("15")
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
name = "Juana"
age = "15"
ten = "10"
fstring = f
In 0 yearts, {name} wil #be {age} + {ten}  years old.#############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

# print the length of the summary
# upper case the entire summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse

blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
print("Lenght: ", len(blue_beetle_summary))
print("uppercase: " , blue_beetle_summary.upper())
print("Lowercase: ", blue_beetle_summary.lower())
# # Replace all occurrences of 'old_word' with 'new_word'
# new_string_all = original_string.replace(old_word, new_word)
# print(f"After replacing all occurrences: {new_string_all}")

# # Replace a specific number of occurrences (e.g., only the first one)
# new_string_first = original_string.replace(old_word, new_word, 1)
# print(f"After replacing only the first occurrence: {new_string_first}")
old_word = "Blue"
new_word = "Red"

red_beetle = blue_beetle_summary.replace(old_word, new_word)
















##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.
name = (input("What is your name?"))

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
q1 = (input("What are you learning today?"))
print(f"Today you are learning{q1}")

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
q2 = (input("Where are you from?"))
print(f"You are from {q2}")

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.
q3 = (input("What is your name?"))
q4 = (input("What is your surname?"))
print (f"Your name is {q3} and your surname is {q4} ")

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information
q5 = (input("What is your full name?"))
q6 = (input("What is your favorite color?"))
print(f"Your full name is {q5} and your favorite color is {q6}")
 