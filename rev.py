x=int(input())
temp=0

upper=2**31-1
lower=-2**31

p=abs(x)

while(p>0):
    rem=p%10
    temp=(temp*10)+rem
    p=p//10

if(x==abs(x) and temp>lower and temp<upper):
    print (temp)

elif(x!=abs(x) and temp>lower and temp<upper):
    print(-temp)

else:
    print(0)
