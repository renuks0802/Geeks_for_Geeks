# Python program to count positive and negative numbers in a list
# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:

# Input: list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
l=[2, -7, 5, -64, -14]
neg=pos=0
for i in l:
    if i>0:
        pos+=1
    else:
        neg+=1
print("pos= "+ str(pos) + "\tNeg = "+ str(neg)) 