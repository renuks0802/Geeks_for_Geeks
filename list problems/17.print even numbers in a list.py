# Given a list of numbers, write a Python program to print all even numbers in given list.

# Example:

# Input: list1 = [2, 7, 5, 64, 14]
# Output: [2, 64, 14]

l=[2, 7, 5, 64, 14]
lst=[]
for i in l:
    if i%2==0:
        lst.append(i)
print(lst)