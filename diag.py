m=int(input("Number of rows"))
n=int(input("Number of columns"))

ar=[]
arr=[]
for i in range (m):
    print("Enter",i+1,"Row")
    for j in range(n):
        a=int(input())
        ar.append(a)
    arr.append(ar)
ar=[]

s=0
s1=0
for i in range(m):
    for j in range(n):
        if(arr[i][j]==[i]):
            s=s+arr[i][j]
        if(arr[j][i]==[j]):
            s1=s1+arr[j][i]
    print(s-s1)

