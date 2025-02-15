#To reduce the given number to 1 with min no.of steps by performing the following operations. We should print the min no.of steps
#1. If the number is even then divide it by 2
#2. If the number is odd then perform n-1 or n+1 // using Recursion
def fun(n):
    if n==1:
        return 0
    if n%2==0:
        return 1+fun(n/2)
    else:
        return 1+min(fun(n+1),fun(n-1))



n=int(input("Enter a number:"))
print(fun(n))
