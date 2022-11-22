#The following are the 'advanced' python function challenges
#1
#Define the function to accept 3 numbers as parameters
#See if the target number is within the range of the other two numbers
#If it is return true, if not return false

def within_range(low, high, target):
    #Inefficient, but I want to try it
    num_list = list(range(low, (high + 1)))
    for num in num_list:
        if num == target:
            return True
        else:
            continue
    return False

high_and_low = input("What is the range you would like to check [x:y]? ")
high_and_low = high_and_low.split(':')
low_num = int(high_and_low[0])
high_num = int(high_and_low[1])
range_target = int(input("Which number are you checking for in the range: "))
is_in_range = within_range(low_num, high_num, range_target)
if is_in_range:
    print(str(range_target) + " is within " + str(low_num) + " and " + str(high_num))
else:
    print("Target is not in the range of " + str(low_num) + " and " + str(high_num))

#2
#Define the function to accept two strings names
#Test if the strings are equal
#If they are return true, and if not, false

def same_name(my_name, your_name):
    if my_name.lower() == your_name.lower():
        return True
    else:
        return False

first_name = input("Enter someones' first name: ")
second_name = input("Enter your first name: ")
if same_name(first_name, second_name):
    print("Names are the same.")
else:
    print("Not the same names.")

#3
#Define the functions to accept a single parameter called num
#Use a combination of <, > and and to create a contradiction in an if statement
#If the condition is true, return True, otherwise return false. The truck is that because there is a contradiction should never be true

def contradiction(num):
    if num < num and num > num:
        return True
    else:
        return False

print(contradiction(1))

#4
#Define our function to accept a single number called rating
#If the rating is equal to or less than 5, return "Avoid at all costs!"
#If the rating was less than 9, return "This one was fun."
#If neigher of the if statement conditions were met, return "Outstanding!"

def movie_rating(rating):
    if rating < 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else:
        return "Outstanding"

rating = int(input("Rate this movie from 1-10"))
print(movie_rating(rating))

#5
#Define a function that has three input parameters, num1, num2, num3
#Test if num1 is greater than the other two numbers => return it
#Test if num 2 is greater than the other two numbers => return it
#Test if num3 is greater than the other two numbers => return it
#If there is a tie => "It's a tie!"

def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    elif num1 == num2 or num2 == num3 or num1 == num3:
        return "It's a tie!"

max1 = int(input("Enter the first number: "))
max2 = int(input("Enter the second number: "))
max3 = int(input("Enter the third number: "))
max = max_number(max1, max2, max3)
if type(max) == int:
    print("The maximum number is " + int(max))
elif type(max) == str:
    print(max)