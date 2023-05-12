x= 1
y=1
z = 2
n= 3
perm  = []
perm2 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(perm2)
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            # print(f" i : {i} j : {j} k : {k}")
            perm.append([i,j,k])
            
print(perm)

res = [i for i in perm2 if sum(i)!=n]
print(res)