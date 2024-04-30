# Write a Python program to print all even numbers from 1 to 100 using a for loop.
# for i in range(1,101):
#     if i % 2 == 0:
#         print("The even numbers are ", i)
# Write a Python program to find the sum of all numbers from 1 to 100 using a while loop.
sum=0
i=0
# while i <= 100:
#     sum += i
#     i += 1
# print("The sum of all natral numabers are ",sum)
# Write a Python program to print the Fibonacci sequence up to n terms using a for loop.
# n=int(input("enter the input:"))
# first_term,second_term=0,1
# print(first_term,second_term , end =",")
# for i in range(first_term+second_term,n+1):
#     next_term=first_term+second_term
#     print(next_term, end =",")
#     first_term=second_term
#     second_term=next_term
# Write a Python program to check if a given number is prime or not using a while loop.
# n=int(input("enter the input:"))
# factor=0
# for i in range(1,n+1):
#     if n % i == 0:
#         factor += 1
# if factor > 2:
#     print("The given number is not a prime number ")
# else:
#     print("The given number is  a prime number ")
# Write a Python program to print the multiplication table of a given number using a nested loop.
n=int(input("Enter the input:"))
product=1
for i in range(1,11):
    for j in range(1,i+1):
        product= n * j
    print(n , '*' , i ,'=',product)
