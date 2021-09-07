# Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

# Example:

# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2

l=[2, 7, 5, 64, 14]
odd=0
even=0
for i in l:
    if i%2==0:
        even+=1
    else :
        odd+=1
print("Odd= "+ str(odd) + "Even= "+str(even))