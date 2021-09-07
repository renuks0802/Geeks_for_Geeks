# Given a list of numbers, the task is to write a Python program to find the largest number in given list.

# Examples:

# Input : list1 = [10, 20, 4]
# Output : 20

l=[10, 20, 4,100]
max=10
for i in l:
    if max<i:
        max=i

print(max)