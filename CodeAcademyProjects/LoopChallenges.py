#1
#Define the function to accept 1 param nums
#Initialize Counter at 0
#Loop through every numer in nums
#Within loop, if any numbers are divisible by 10, increment counter
#Return final counter value

def freq_div_ten(nums):
    div_by_ten = 0
    for i in range(len(nums)):
        if (nums[i] % 10) == 0:
            div_by_ten += 1
    return div_by_ten

print("There are " + str(freq_div_ten([10,20,30,11,15])) + " numbers divisible by ten in the list.")

#2
#Define the function to accept a list called names
#Create a new list of strings
#Loop through each name in names
#Within the loop, concatenate 'Hello, ' with the name and append this string to the new list
#Return the new list of strings

def greetings_list(names):
    greetings_lst = []
    for name in names:
        greetings_lst.append("Hello, " + name)
    return greetings_lst

greetings = greetings_list(["Cameron", "Lori", "Vernon"])
for greeting in greetings:
    print(greeting)

#3
#Define function to accept a single input param lst of nums
#Loop through every number in lst if there are still nums in lst and we haven't hit an odd yet
#Within the loop, if the first number is even, remove the first number of the list
#Once we hit an odd number or we run out of numers, return modified list

def odd_num_stop(nums):
    new_lst = []
    while len(nums) != 0:
        for num in nums:
            if (num % 2) == 0:
                nums.remove(num)
            else:
                new_lst = nums.copy()
                return new_lst
    return "This list has no odds"

    #Alternate way
    #while (len(nums) > 0 and nums[0] % 2 == 0):
    #    nums = nums[1:]
    #return nums

print("This list had no odds: " + odd_num_stop([2, 4, 6, 8, 10]))
print("This list had odd numers: " + str(odd_num_stop([2, 4, 6, 7, 8, 9, 10])))

#4
#Define the function header to accpet one input, lst of nums
#Creatae a new list which will hold vals to return
#Iterate through ever odd index until the end of the list
# within  the loop, et the elemet at the current odd index and append it to new list
#Return elements from odd indecies

def odds_only(full_lst):
    new_lst = []
    for i in range(len(full_lst)):
        if i % 2 != 0:
            new_lst.append(full_lst[i])
    return new_lst

    #Alternate
    #for i in range(1, len(full_lst), 2):
    #    new_lst.append(full_lst[i])

org_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odds_only(org_lst))

#5
#Define func to accept bases and powers
#create new list to contain answers
#create loop iterating through all bases
#within base loop, create another that iterates through all powers
#append the result of current base raised to the current power
#after iteration of both complete, return new list