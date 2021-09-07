#Given a List. The task is to find the sum and average of the list. Average of the list is defined as the sum of the elements divided by the number of the elements.


# Input: [4, 5, 1, 2, 9, 7, 10, 8]
# Output:
# sum =  46
# average =  5.75

l=[4, 5, 1, 2, 9, 7, 10, 8]
sum=0
for i in l:
    sum+=i
print(sum)
print(sum/len(l))


