
# arr = [3,6,6,5,1,10,2]
# a1 = list(set(arr))
# print(a1)
# a2 = []

# [a2.append(i) for i in arr if i not in a2]
# print(a2)

# for i in range(len(arr)):
#     print(arr[i])
arr = map(int, input().split())
arr = list(set(list(arr)))
arr.sort(reverse=True)
print(arr[1])
    
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    arr.sort(reverse=True)

    if len(arr)>0 and len(arr)<2:
        print(arr[0])
    elif len(arr)>1:
        print(arr[1])