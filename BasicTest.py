import random

print("Hello World!")

#Magic 8-ball project
name = input("What is your name? ")
question = input("Please enter a 'yes' or 'no' question you would like answered. ")
answer = ""

random_number = random.randint(1, 9)
if (random_number == 1):
    answer = "Yes - definitley"
elif (random_number == 2):
    answer = "It is decidedly so."
elif (random_number == 3):
    answer = "Without a doubt."
elif (random_number == 4):
    answer = "Reply hazy, try again."
elif (random_number == 5):
    answer = "Ask again later."
elif (random_number == 6):
    answer = "Better not tell you now."
elif (random_number == 7):
    answer = "My sources say no."
elif (random_number == 8):
    answer = "Outlook not so good"
elif (random_number == 9):
    answer = "Very doubtful."

print(name + " asks: " + question + "\nMagic 8-Ball's answer: " + answer)
