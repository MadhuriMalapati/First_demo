# # Write a Python program to handle division by zero exception.
try:
    result=10/0
    print("result is",result)
except ZeroDivisionError as e:
    print("Error msg is:",e)
#when we do not know what exception to use we can do like this
# except Exception as e:
#     print("error msg is ", e)
# # Write a Python program to handle file not found exception.
# try:
#     file_path=" "
#     with open(file_path, "r") as file:
#         content =file.read()
#         print(content)
# # except FileNotFoundError as e:
# #     print("Eroor msg is",e)
# except Exception as e:
#     print("Error msg is ", e)
#
# # Write a Python program to handle IndexError exception.
# try:
#     list_num=[1,2,3,4,5,6]
#     print(list_num[4])
# # except IndexError as e:
# #     print("error msg is" , e)
# except Exception as e:
#     print("Error msg is ", e)
# # Write a Python program to handle KeyError exception.
# try:
#     dict={"name":"neelam","age":56,"place":"new delhi"}
#     print(dict.get(""))
# # except KeyError as e:
# #     print("error msg is",e)
# except Exception as e:
#     print("error msg is ",e)
#
#

# # Write a Python program to demonstrate the use of try-except-else-finally blocks.
try:
    if 4 % 3 == 0:
        print("remainder is zero")
except Exception as e:
    print("error msg is ",e)
else:
    print("remainder is not zero")
finally:
    print("Done the program")
