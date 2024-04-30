# # Write a Python function to find the maximum of three numbers.
# #Algorithm:1.create a fnction maximum_3
# #2.assign greatest_number = n1
# #3.use if else conditon to check whtether n1 is lessthan or greater than both(n2 and n3)
# #4.return the value
# #5.Assign the retrned vale to a varibale
# #6.print the reslt.
# def maximum_3(n1,n2,n3):
#     greatest_number = n1
#     if n1 < n2:
#         greatest_number = n2
#     else:
#         greatest_number = n1
#     if n3 >  greatest_number:
#         greatest_number = n3
#     return  greatest_number
#
# result=maximum_3(10,5,12)
# print(result)
#-------------------------------------------
# Write a Python function to check if a given number is even or odd.
#1.crate a  variable for assigning the input create a function even_odd
#2.check the condition using if-else statement (number divisible by 0 is an even , not divisible by 0 is odd)
#3.retrun the value
#4.assign the returned value to the variable and print the result.
# n=int(input("Enter the number :"))
# def check_evenodd(n):
#     if n % 2 == 0:
#         print(f"The given number {n} is an even number")
#     else:
#         print(f"The given number {n} is an odd number")
# check_evenodd(n)
#-------------------------------------------------------------------
# Write a Python function to calculate the factorial of a given number.
#1.crate a  variable for assigning the input create a function factorial and assign a varialbe to take the prodct
#2.use for loop for itertaion and for every iteraion multiply the iertrar with the prouct
#3.return the value
#4.assign the returned value to the variable and print the result.
# n=int(input("Enter the number :"))
# def factorial(n):
#     product=1
#     for i in range (1,n+1):
#         product = product * i
#     return product
# result = factorial(n)
# print(result)
# from math import gcd
#
#
# # Write a Python function to find the greatest common divisor (GCD) of two numbers.
# def gcd_two(a,b):
#     return gcd_two(a,b)
# reslt=gcd(12,13)
# print(reslt)
# Write a Python program to demonstrate the use of lambda functions.
# x=lambda a ,b , c: a+b+c
# print(x(1,2,0))
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)

print(mytripler(11))


