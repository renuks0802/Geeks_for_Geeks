# Given starting and end points, write a Python program to print all even numbers in that given range.

# Example:

# Input: start = 4, end = 15
# Output: 4, 6, 8, 10, 12, 14


lst=[]
for i in range(4,16):
    if i%2==0:
        lst.append(i)
print(lst)