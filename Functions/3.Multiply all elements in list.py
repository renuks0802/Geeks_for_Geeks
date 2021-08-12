# Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def mul(lst):
    m=1
    s=0
    for i in lst:
        m=m*i
        s+=m
    print(m)

mul([8, 2, 3, -1, 7])