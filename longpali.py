s=input("Enter string")
p=len(s)
m=""
for i in range(p):
    for j in range(1,p):
        if(j<=p and len(m)<=len(s[i:])):
            if(s[i:j]==s[i:j][::-1] and len(s[i:j])>len(m)):
                m=s[i:j]
        
        #print(s[i:])
        #print(s[i:j])
        #print(len(s[i:j]))
print(m)

