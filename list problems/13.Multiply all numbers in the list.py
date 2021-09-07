# Given a list, print the value obtained after multiplying all numbers in a list. 
# Examples: 
 

# Input :  list1 = [1, 2, 3] 
# Output : 6 
# Explanation: 1*2*3=6 

# Input : list1 = [3, 2, 4] 
# Output : 24 

l=[3, 2, 4]
m=1
for i in l:
    m*=i
print(m)