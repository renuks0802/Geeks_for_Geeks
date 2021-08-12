#Write a Python function to find the Max of three numbers.

def max(n1,n2,n3):
    ''' to find the max of 3 numbers'''
    if (n1>n2) & (n1>n3):
        print(n1)
    elif(n2>n1) & (n2>n3):
        print(n2)
    elif(n3>n2) & (n3>n1):
        print(n3)
    else:
        print('All are eaual')

max(8,2,4)