#Python | Count occurrences of an element in a list
# Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
#          x = 10
# Output : 3 
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
n=10
c=0
for i in lst:
    if i==n:
        c+=1
print(c)