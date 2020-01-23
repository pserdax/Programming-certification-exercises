import operator
m,n,p=map(int,raw_input().split())

medie=0
d={}
for i in range(m):
    nume=raw_input()
    note=map(int,raw_input().split())
        
    if all ([int(x)>=5 for x in note]):
        medie=float(sum(note))/len(note)
    
        if medie >=8:
            d.update({nume:float(medie)})
            
sorted_d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)  #d items takes all values from d, operator.itemgetter second element from d which is medie, and reverse true means, order the by descending order... 

perfn=sorted_d[0][0] # [0]takes first item which is name: medie, [0] takes the first items first element 
perfm=sorted_d[0][1] # [0]takes first item which is name: medie, [1] takes the first items second element 
perfm=format(perfm,'.2f')
del sorted_d[0]

if p>len(sorted_d):
    print len(sorted_d)
else:
    print p

print perfn,perfm