# abstraction is when I hide
# the complex details for something
# alot more simple.

question1 = input("how old are you?")
question2 = input("where do you live?")
question3 = input("what school do you go to?")
print (question1 + question2 + question3)

def personInformation():
    question1 = input("how old are you?")
    question2 = input("where do you live?")
    question3 = input("what school do you go to")
    print(question1 + question2 +question3)

#call the function
personInformation()
personInformation()
personInformation()

# make a function that guesses how old you are?


q1 = int(input("what year is it now?"))
q2 = int(input("what year were you born?"))
answer = q1 - q2
result = print(f'you are {answer} years old')

# git add .
# git commit -m "abstraction"
# git push origin