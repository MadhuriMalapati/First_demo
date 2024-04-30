word1=input("Enter first word:")
new_word1=word1.upper()
print(new_word1)
word2=input("Enter the second word:")
new_word2=word2.upper()
print(new_word2)
count=0
count1=0
for char in new_word1:
    if char == "T" or char == "R" or char == "U" or char == "E":
        count += 1
print(count)
for i in new_word2:
    if i == "L" or i == "O" or i == "V" or i == "E":
        count1 += 1
print(count1)
print(str(count)+str(count1))






