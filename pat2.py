def triangle(n): 
    k = n 
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
      
        k = k - 1
     
        for j in range(0, i): 
            print("*",end="")  
        print("\r")  
n=int(input())
triangle(n) 
