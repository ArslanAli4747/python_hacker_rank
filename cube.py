
t = int(input())

for i in range(t):
    n = int(input())
    sides = input().split()
    newsides = list(map(int,sides))
    left = 0 
    right = n - 1
    arr = []
    match =True
    while left <= right:
           
        if newsides[left] >= newsides[right]:
            if len(arr)>0:
                if arr[-1] < newsides[left]:
                    match = False
            arr.append(newsides[left])
            left += 1
        else:
            if len(arr)>0:
                if arr[-1]<newsides[right]:
                    match = False
            arr.append(newsides[right])
            right -= 1
        print(arr)
    if match:
        print("Yes")
    else:
        print("No")
           
            
            
    
    