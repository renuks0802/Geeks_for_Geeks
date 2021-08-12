#Different ways to clear a list in Python
a=[34,455,56,677,88,99,86]
b=[]
for i in a:
    if i!=0:
        a=b
print(a)

#or print(a[-1:0])