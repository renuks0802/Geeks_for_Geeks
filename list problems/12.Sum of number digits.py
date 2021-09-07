# The problem of finding the summation of digits of numbers is quite common. This can sometimes come in form of a list and we need to perform that. This has application in many domains such as school programming and web development. Let’s discuss certain ways in which this problem can be solved.
l=[12, 67, 98, 34]
lst=[]
for i in l:
    print(i)
    a=i%10    
    print(a)
    i=i-a
    b=i/10
    c=a+b
    lst.append(int(c))
print(lst)


    #print(i/10)