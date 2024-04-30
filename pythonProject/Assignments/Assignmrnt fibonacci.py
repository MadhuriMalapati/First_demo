number = int(input("Enter your input:"))
first_term,second_term = 0,1
print(first_term,second_term , end =",")
while first_term+second_term <= number:
    next_term= first_term+second_term
    print(next_term , end=",")
    first_term=second_term
    second_term=next_term