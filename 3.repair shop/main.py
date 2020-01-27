stock = list(map(int, input().split()))
nr = int(input())
c=0
for i in range(nr):
    binary = list(map(int, input().split()))
    arr = list()    
    for x in range(len(binary)):
        if binary[x]==0:
            arr.append(x)
         
    a=any(stock[y]==0 for y in arr)
    
    if a==True:
        for y in range(len(stock)):
            
            stock[y]=stock[y]+binary[y]
    else:
        for y in arr:
            stock[y]  =stock[y]-1
            binary[y]=1
    b = all(y==1 for y in binary)
    
    if b==True:
        c=c+1

print(c)