# print("hello World")
# print("values")
# a="3.0"
# print("Type of a :",type(a))
# #Assigning multiple values.
# b,c,d=1,2.3,"indai"
# print(b,c,d)
# #Lists: mutable and ordered collections
# first_list=[12,10,"14",15]
# print(first_list)
# #tuples:immutable and ordered collection
# Fir_tuple=(13,23.5,"India","12+13j")
# print(Fir_tuple)
# #range(start,stop,step)
# #Mapping data type-dict
# fir_dict={"neem":3,"rome":4,3:"Pune"}
# print(fir_dict[3])
# #set - set,frozenset - unorderd collection and mutable,unique items
# d={1,2,3,4,5.6,"neem",4}
# print(d)
# #frozsen set - unorderd collection and immutable
# f=({1,2.3,45})
# print(f)
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))