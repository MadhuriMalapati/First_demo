#Write a Python program to find the factorial of a given number using a while loop.
# def factorial(n):
#     count=1
#     product=1
#     while count < (n+1):
#         product=product * count
#         count = count + 1
#     print(product)
# factorial(5)
n=input("Enter your number:")
n=int(n)
def factorial(n):
    count=1
    product=1
    while count < (n+1):
       product=product * count
       count = count + 1
    return product
result=factorial(n)
print(f"The factorial of a given number is {result}")
