#Write a Python program to print the multiplication table of a given number using a for loop.
n=input("Enter your number:")
n=int(n)
def multi_table(n):
    for i in range(1,11):
        print(n,'*',i ,'=', n * i )
multi_table(n)

