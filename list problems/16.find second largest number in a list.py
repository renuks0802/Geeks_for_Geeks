# Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.
# Examples:

# Input: list1 = [10, 20, 4]
# Output: 10

l=[10, 20, 4,30,500]
lst=[]
max=0
for i in l:
    if max<i:
        max=i
        a=max
        l.remove(max)
for j in l:
    if max<j:
        max=j
        b=max

if a<b:
    print(a)
if b<a:
    print(b)


