
n = int(input())
t = tuple(map(int,input().split()))

print(t)

res = sum(t)
print(hash(res))

my_tuple = (1, 2)
print(hash(my_tuple))