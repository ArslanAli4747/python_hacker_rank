"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

"""

# ls = []
# n = int(input())

# for i in range(n):
#     command,*args = input().split()
#     match(command):
#         case "insert":
#             ls.insert(int(args[0]),int(args[1]))
#         case "print":
#             print(ls)
#         case "remove":
#             ls.remove(int(args[0]))
#         case "append":
#             ls.append(int(args[0]))
#         case "sort":
#             ls.sort()
#         case "pop":
#             ls.pop()
#         case "reverse":
#             ls.reverse()
        
        
        
if __name__ == '__main__':
    ls = []
    N = int(input())
    for i in range(N):
        command,*args = input().split()
        if command == "insert":
            ls.insert(int(args[0]),int(args[1]))
        if command == "print":
            print(ls)
        if command == "remove":
            ls.remove(int(args[0]))
        if command == "append":
            ls.append(int(args[0]))
        if command == "sort":
            ls.sort()
        if command ==  "pop":
            ls.pop()
        if command ==  "reverse":
            ls.reverse()