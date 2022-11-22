#List Challenges
#1
#Define the function to accept one parameter for the list
#Get the length of the list
#Append the length of the list to the end of the list
#Return the modified list

def length_as_last(entry):
    entry.append(len(entry))
    print(entry)
    return entry

test_list = [1, "Hello", 3.4, "World"]
length_as_last(test_list)
print(test_list)

#2
#Define the function to accept one parameter for a list of numbers
#Add the las and second to last elements of our list together
#Append the calculated value to the end of the list
#Repeat steps 2 and 3 two more times
#Return the moified list

def modified_fibonacci(nums):
    for i in range(3):
        nums.append((nums[-2] + nums[-1]))
    return nums

begin_fibonacci = [1, 1, 2, 3, 5, 8]
print(begin_fibonacci)
modified_fibonacci(begin_fibonacci)
print(begin_fibonacci)

#3
#Define the function that accepts two parameters, both lists of numbers
#Check if the length of the first list is greater than or equal to the length of the second list
#If true, then return the last element from the first list, else return the last item from the second list

def last_of_longest(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

long_lst1 = [1, 2, 3, 4, 5, 6]
long_lst2 = [7, 8, 9, 10, 11]
print(int(last_of_longest(long_lst1, long_lst2)))

#4
#Define the function to accept 3 params, list of number, target, and a number for number of instances
#count the number of occurences of target in the list
#If the number of occurrences is greater an the param number of instances return true, otherwise false

def meets_frequency(nums, target, freq):
    acc_freq = nums.count(target)
    if acc_freq >= freq:
        return True
    else:
        return False

freq_list = [1, 2, 3, 1, 2, 3, 2, 3, 3]
freq_target = 3
freq = 3
print("The frequency is higher than expected: " + str(meets_frequency(freq_list, freq_target, freq)))

#5
#Define the function to accept two parameters, one for each list
#Combine the two lists together
#Sort the result
#Return the sorted combined list

def combination_sort(lst1, lst2):
    full_lst = lst1 + lst2
    full_lst.sort()
    return full_lst

unsort_lst = [1, 5, 3, 2]
unsort_lst2 = [4, 9, 6, 8, 7, 0]
full_lst = combination_sort(unsort_lst, unsort_lst2)
print(full_lst)

#6
#Defind the funciton to accept one parameter for our starting number
#Calculate the numbers between starting and 100 while incremening by 3
#store numbers in a list
#return list

def three_to_hundred(start_num):
    num = start_num
    lst_return = [start_num]
    while num <= 97:
        num += 3
        lst_return.append(num)
    return lst_return

start = int(input("Starting number: "))
lst_return = three_to_hundred(start)
print(lst_return)
print("There are " + str(len(lst_return) - 1) + " number(s), from " + str(start) + " to 100 (iterating by 3).")

#7
#Define the function to accept 3 params, list, starting index, ending index
#get all elements before starting index
#get all elemens after the ending index
#combind the two partial list into the result
#return the result
        