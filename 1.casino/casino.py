print('How many players: ')
n = int(input())
arr =  list()
for i in range(n):
    value = input().split()
    arr.append(value)

c =0
arr1 = list()

for i in arr:
    c = arr.count(i)
    arr1.append(c)
    if c>=3:
        i = ' '.join(i)
        print(i)
        break

check = all(i==1 or i==2 for i in arr1)

if check ==True:
    print('JOC OK')