#Python program to swap two elements in a list
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]
lst = [1, 2, 3, 4, 5]
a=lst[1]
lst[1]=lst[4]
lst[4]=a
print(lst)