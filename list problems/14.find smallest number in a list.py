# Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
# Examples: 

# Input : list1 = [10, 20, 4]
# Output : 4

# Input : list2 = [20, 10, 20, 1, 100]
# Output : 1
l=[20, 10, 20, 1, 100]
min=20
for i in l:
    
    if min>i:
        min=i
print(min)
