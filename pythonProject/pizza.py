# customer_order=input("Enter your order:")
# bill=0
# pepper=input("Press Y for extra pepper:")
# extra_cheese=input("Press Y for extra cheese")
# if customer_order == "small_pizza":
#     if pepper.upper() == "Y" and extra_cheese.upper() == "Y":
#         bill = (bill+(15 * 64))+(2 * 64) +(1 * 64)
#     else:
#         bill = (bill + (15 * 64))
# elif customer_order == "medium_pizza":
#     if pepper == "Y" and extra_cheese == "Y":
#         bill = (bill+(20 * 64))+(3 * 64) +(1 * 64)
#     else:
#         bill = (bill + (20 * 64))
# elif customer_order == "large_pizza":
#     if pepper == "Y" and extra_cheese == "Y":
#         bill = (bill+(25 * 64))+(3 * 64) +(1 * 64)
#     else:
#         bill = (bill + (20 * 64))
# print(bill)
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0
if size == 'S':
    bill =+ 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")