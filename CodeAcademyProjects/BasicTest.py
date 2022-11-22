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

#Sal's Shipping project
weight = float(input("Enter weight of package in lbs. "))
cost_ground = 0

if weight <= 2:
    cost_ground = 20 + (1.5 * weight)
elif weight <= 6:
    cost_ground = 20 + (3 * weight)
elif weight <= 10:
    cost_ground = 20 + (4 * weight)
elif weight > 10:
    cost_ground = 20 + (4.75 * weight)

cost_drone = 0
if weight <= 2:
    cost_drone = (4.5 * weight)
elif weight <= 6:
    cost_drone = (9 * weight)
elif weight <= 10:
    cost_drone = (12 * weight)
elif weight > 10:
    cost_drone = (14.25 * weight)

recommended_shipping = ""
shipping_price = 0

if (cost_ground >= 125) and (cost_drone >= 125):
    recommended_shipping = "Ground Shippint Premium"
    shipping_price = 125
elif (cost_ground > cost_drone):
    recommended_shipping = "Drone Shipping"
    shipping_price = cost_drone
elif (cost_ground <= cost_drone):
    recommended_shipping = "Ground Shipping"
    shipping_price = cost_ground

print("Ground: $" + str(cost_ground) + "\nDrone: $" + str(cost_drone) + "\nPremium Ground: $125")
print("Recommended shipping method: " + recommended_shipping + " - $" + str(shipping_price))

#Function Challenges
#1
#Defind the function to accept two input parameters called base and exponent
#Calculate the result of base to the power of exponent
#Use an if statement to test if the result is greater than 5000. If it is then return true, otherwise return false
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print("The result is larger than 5000: " + str(large_power(base, exponent)))

#2
#Define the function to accept five parameters, budget, food_bill, electricity_bill, internet_bill, and rent
#Calcualte the sum of the last four parameters
#Use if and else statements to test if the budget is less than the sum of the calculated sum from the previous step
#If the condition is true, return true, otherwise return false

def within_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    total_cost = food_bill + electricity_bill + internet_bill + rent
    if total_cost > budget:
        return False
    elif budget >= total_cost:
        return True

budget = int(input("What is your budget in dollars: "))
food_bill = 300
electricity_bill = 150
internet_bill = 80
rent = 1500
print("Result of calculation, determining if this is within your budget: " + str(within_budget(budget, food_bill, electricity_bill, internet_bill, rent)))

#3
#Define our function with two inputs, num1 and num2
#Multiply the second input by 2
#Compare the result of num2 with num1
#If num1 is greater return true, or if not, false

def more_than_double(num1, num2):
    if num1 > (num2 * 2):
        return True
    else:
        return False

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Is the first number more than double the second? " + str(more_than_double(num1, num2)))

#4
#Define the function header to accept one input, num
#Calcualte if the remainder of the input devided by 10
#If the input was 0 return True, if not return False

def div_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False

check_if_divisible_by_ten = int(input("Enter a number to devide by 10: "))
if check_if_divisible_by_ten:
    print("This number IS divisible by 10 :).")
else:
    print("This number IS NOT divisible by 10 :(.")

#5
#Define the function to accept two parameters, num1 and num2
#Add the two parameters together
#Test if the reuslt is not equal to 10
#If it is not, return true, otherwise false

def adds_to_ten(num1, num2):
    total = num1 + num2
    if total == 10:
        return True
    else:
        return False

num1_to_ten = int(input("Enter your first number."))
num2_to_ten = int(input("Enter your second number."))
result_of_adds_to_ten = adds_to_ten(num1_to_ten, num2_to_ten)
if result_of_adds_to_ten:
    print("The numbers add to ten!")
else:
    print("The numbers don't add to ten.")



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

first_name = name
second_name = input("Enter your firstName")
if same_name(first_name, second_name):
    print("Names are the same.")
else:
    print("Not the same names.")