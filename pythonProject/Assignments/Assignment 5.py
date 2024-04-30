#Write a Python program to check if a given number is prime or not using a for loop.
# n=input("Enter your nbr:")
# n=int(n)
# def prime_num(n):
#     if n % 2 != 0:
#         print(f"The given number {n} is a prime number")
#     else:
#         print(f"The given number {n} is not a prime number")
# prime_num(n)
# factor=0
# for i in range(1,n+1):
#     if n % i == 0:
#         factor += 1
# if factor > 2:
#     print(f"The given number is not an prime number ")
# else:
#     print(f"The given number is a  prime number ")
#
def mystery(x):
    if x == 0:
        return 1
    return x * mystery(x - 1)

print(mystery(5))