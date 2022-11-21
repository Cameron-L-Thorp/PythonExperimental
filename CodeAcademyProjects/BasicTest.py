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

