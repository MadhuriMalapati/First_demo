# file_path=r"C:\Users\madhu\PycharmProjects\pythonProject\example.txt"
# with open(file_path,"r") as file:
#     contents=file.read()
#     print(contents)
# reading line by line
# file_path=r"C:\Users\madhu\PycharmProjects\pythonProject\example.txt"
# with open(file_path, 'r') as file:
#     for line in file:
#         print(line.strip())
# write into a file:
# file_path=r"C:\Users\madhu\PycharmProjects\pythonProject\example.txt"
# with open(file_path,"w") as file:
#     file.write("This is a pyhton courssse\n")
#     file.write("This is a file handling program")
#append data intoa file:
file_path=r"C:\Users\madhu\PycharmProjects\pythonProject\example.txt"
with open (file_path,"a") as file:
    file.write("\n I am new learner ")
