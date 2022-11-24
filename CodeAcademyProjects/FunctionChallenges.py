#1
#Set function with one param num
#Take the tenth power of the input
#return result

def tenth_pwr(num):
    return num ** 10

#2
#Sef func to accept on param
#Take squre root of input val
#return result

def sqr_root(num):
    return num ** 0.5

#3
#Def func to have two param, wins and losses
#Calc the numer of games using wins and losses
#get ratio of wins to losses
#Convert ratio to a percentage
#return percentage

def win_ratio(wins, losses):
    games = wins + losses
    wins = str((wins / games) * 100) + "%"
    losses = (losses / games) * 100
    return wins

print(win_ratio(10, 5))
    
#4
#Def function with input params num1, and num2
#Calc sum of two numbers
#Divide sum by number of inputs
#return answer

def average_calc(num1, num2):
    return (num1 + num2) / 2

#5
#Def func to accept 2 param
#Multiply the first input val by 2
#divide the second input val by 2
#Calc the remainder of the modified ifrst input value divided by the modified second input value (using modulus)
#return answer

def remainder(num1, num2):
    num1 = num1 * 2
    num2 = num2 / 2
    return num1 % num2

#6
#Def func for input num
#print num * 1
#print num * 2
#print num * 3
#return num * 3

def first_three_multiples(num):
    print(num, (num * 2), (num * 3))
    return num * 3

first_three_multiples(10)

#7
#Def func for total cost and percentage inputs
#Calc tip by mulitplying total and percentage, divide by 100
#return tip amount

def tip_calc(total, percentage):
    return (total * percentage) / 100

#8
#Def func for param first and last name
#concat , on last
#concat first  after last
#concat space 
#concat last 
#return final

def bond_func(fname, lname):
    return (lname + ", " + fname + " " + lname)

print(bond_func('Cameron', 'Thorp'))

#9
#Define func with name and age
#calc the age of dog in dog years
#concat name and age
#return final

def dog_years(name, age):
    age = age * 7
    return (name + ", you are " + str(age) + " years old in dog years.")

print(dog_years("Cameron", 23))

#10
#def func with input a, b, c, d
#print a + b
#print c - d
#print first times second result and save
#return result modulus a

def all_ops(a, b, c, d):
    b = a + b
    print(b)
    c = c - d
    print(c)
    d = b * c
    print(d)
    return d % a

print(all_ops(1, 2, 3, 4))