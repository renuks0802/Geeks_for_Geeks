# Given a list of numbers, write a Python program to print all odd numbers in given list.

# Example:

# Input: list1 = [2, 7, 5, 64, 14]
# Output: [7, 5]

l=[2, 7, 5, 64, 14]
lst=[]
for i in l:
    if i%2==1:
        lst.append(i)
print(lst)