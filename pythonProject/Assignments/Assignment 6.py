#Write a Python program to find the sum of all even numbers from 1 to 50 using a for loop.

def sum_even():
    sum = 0
    for i in range(1,51):
        if i % 2 == 0:
            sum += i
    print(sum)
sum_even()