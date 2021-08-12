#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
n=int(input("Enter upto :"))
def fact():
    i=1
    f=1
    while i<=n:
        if i!=0:
            f=f*i
        i+=1
        
    print(f)
fact()