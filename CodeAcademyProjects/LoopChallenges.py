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

def ret_exponents(bases, exponents):
    results = []
    for base in bases:
        for exponent in exponents:
            results.append(base ** exponent)
    return results

bases = [1, 2, 3, 4, 5]
exponents = [1, 2, 3]
results = ret_exponents(bases, exponents)
print(results)

#6
#Define a func to accept 2 lsts
#Create to vars to record sums
#Loop thru each list and add numbers of each
#Compare first and second, return list with greater sum

def greater_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in range(len(lst1)):
        sum1 += lst1[i]
    for i in range(len(lst2)):
        sum2 += lst2[i]
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

lst1 = [1, 3, 5, 6, 8] #23
lst2 = [20, 4]
greater_lst = greater_sum(lst1, lst2)
print(greater_lst)

#7
#Define the func to accept lst of nums
#Create var to keep track of sum
#Iterate through all elements
#add up the sum
#Still within the loop, check if the number is over 9000
#When it is over 9000 return the sum

def over_9000(nums):
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        if sum > 9000:
            return sum
        elif i == len(nums) - 1:
            return "This is not over 9000"
        else:
            continue
    
    

over = [7024, 1975, 43]
under = [8995, 1, 1, 1, 1]
over_result = over_9000(over)
under_result = over_9000(under)
print(over_result)
print(under_result)

#8
#Define func param with lst nums
#Set max balue to be first element in the list
#Loop thru lst, if current number greater, replace
#return maximum number

def manual_max(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
        else:
            continue
    return max

max_num_lst = [40, 14, 53, 10]
max_num_lst_neg = [-90, -109, -10, -40]
max1 = manual_max(max_num_lst)
max2 = manual_max(max_num_lst_neg)
print("Max for positives is " + str(max1) + ". Max for negatives is " + str(max2) + ".")

#9
#Def func to accept 2 lsts
#Create new list to store matching indecies
#loop thru each index to compare them
#if vals match, add index to new lst
#return list of indecies

def matching_indecies(lst1, lst2):
    ret_indecies = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            ret_indecies.append(i)
    return ret_indecies

matching1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matching2 = [1, 5, 3, 5, 5, 5, 7, 5, 9]
ret_indecies = matching_indecies(matching1, matching2)
print(ret_indecies)

#10
#Def func with two params for lsts
#Loop thru each index from beginning to end
#Within loop, compare element in first list at current index against element at second list's last index minust the current index. If they aren't the same, return false
#If the lists are mirrors, return true

def check_reversed(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] == lst2[(len(lst2) - 1) - i] and len(lst1) == len(lst2):
            continue
        else:
            return False
    return True

rev_lst1 = [1, 2, 3, 4, 5, 6]
rev_lst2 = [0, 6, 5, 4, 3, 2, 1]
rev_lst3 = [6, 5, 4, 3, 1, 1]
exp_true = check_reversed(rev_lst1, rev_lst2)
exp_false = check_reversed(rev_lst1, rev_lst3)
print(exp_true, exp_false)