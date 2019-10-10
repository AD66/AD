n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
s=0
for i in range(len(l)):
    s=s+l[i]

print(s)
