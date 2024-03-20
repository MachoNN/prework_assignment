# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

#     def hello_name(user_name):
#         .....

print("hello_" + input("USERNAME?"))

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#     def first_odds()

odd_num = [x for x in range(1,100+1, 2)]
print(odd_num)
               
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#     def max_num_in_list(a_list):

num = [40, 20 ,50 ,10 ,30]
print(max(num))
               
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#     def is_leap_year(a_year):

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")
               
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#     def is_consecutive(a_list):
    
num1 = [2, 6, 1, 7, 9, 3]
sorted_list = sorted(num1)

range1 = list(range(min(num1), max(num1) +1))
if sorted_list == range1:
    print("num1 has consecutive numbers")
else:
    print("num1 has no consecutive numbers")