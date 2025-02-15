#To sort elements in order based on length
l=list(input("Enter List:").split())
l.sort(key=len)
print(l)


#To place odd numbers in even indexes
l=[0,1,2,3,4,5,6,7]
sum=0
for i in range(len(l)):
    if l[i]%2!=0 and i%2==0:
        sum+=l[i]
print(sum)


#To know which apartmants are having sunlight(Highest among all buildings
l=[1,2,5,3,4]
count=0
max=0
for i in l:
    if i>max:
        max=i
        count+=1
print(count)


#Print the list after deleting the duplicate elements without using set in it
l=[1,2,3,5,4,3,2,4,3]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)


#Print the elements in the list which has occured odd number of times
l=[1,2,3,5,4,3,2,4,3]
res=[]
for i in l:
    if l.count(i)%2!=0 and i not in res:
        res.append(i)
print(res)



#Sorting the given elements first in descending order and then odd elements in ascending order
l=[4,2,8,7,9,5,3,1,6]
res=[]
l.sort()
for i in l:
    if (i%2!=0):
        res.append(i)
    else:
        res.insert(0,i)
print(res)



#check if the list contains consecutive numbers and return true
l=[2,3,44,1,5,7,6]
flag=0
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        flag=1
        break
if flag==1:
    print(True)
else:
        print(False)


#To print the non duplicate elements
l=[5,2,2,1,3,4,3,5,4]
x=0
for i in l:
    x=x^i
print(x)



#Elections are conducted in a town of population N. all the people are voted and there is a rule that only people of age 18 or above can vote so the votes below age 18 are not considered so tell the candidate who is winner if it cannot be determined or if it is tie print -1
'''Sample Input
5
1 2 1 2 3 
17 21 20 19 18
sample output
2'''
n=int(input("Enter n:"))
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
c=[0]*max(vote)
for i in range(n):
    if age[i]>=18:
        c[vote[i]-1]+=1
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0])+1)

#To print 5 4 3 2 1 if the n is 5 using recursion
def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
x=int(input("Enter a number"))
fun(x)


#To print 1 2 3 4 5 if the n is 5 using recursion
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n,end=" ")
x=int(input("Enter a number"))
fun(x)


#To print 5 4 3 2 1 2 3 4 5 if the n is 5 using recursion
def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
    if n!=1:
        print(n, end=" ")
x=int(input("Enter a number"))
fun(x)


#To print 5 4 3 2 1 200 using recursion
def fun(n):
    if n==0:
        return 200
    print(n, end=" ")
    t=fun(n-1)
    return t
x=int(input("Enter a number:"))
print(fun(x))


#To print 1 2 3 4 5 4 3 2 1 if the n is 5 using recursion
def fun(n,m):
    if n==m:
        return
    print(n+1,end=" ")
    fun(n+1,m)
    #if n+1!=m:
    print(n+1,end=" ")
    return
x=int(input("Enter a number"))
fun(0,x)












