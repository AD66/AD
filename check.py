m=int(input("total number of apples in list"))
n= int(input("total number of oranges in list"))
apples=[]
oranges=[]
for i in range(m):
    l=int(input())
    apples.append(l)
for i in range(n):
    k=int(input())
    oranges.append(k)

s=int(input("Starting point of sam's house"))
t=int(input("Ending point of sam's house"))
a=int(input("location of apple tree"))
b=int(input("Location of orange tree"))
print(apples)
print(oranges)
count=0
c=0
for i in range(len(apples)):
    p=apples[i]+a
    if(p>=s and p<=t):
        count+=1
        print(count)
    else:
        print(count)
for i in range(len(oranges)):
    q=oranges[i]+b
    if(q>=s and q<=t):
        c+=1
        print(c)
    else:
        print(c)
