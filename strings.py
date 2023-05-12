n = 10
output = ""
for i in range(1, n+1):
    # calculate the number of digits in i
    num_digits = 1
   
    while i // (10 ** num_digits) > 0:
        num_digits += 1
    # print(num_digits) 
    
    # extract each digit of i and add to output
    for j in range(num_digits):
        print(j)
        divisor = 10 ** (num_digits - j - 1)
        print(divisor)
        digit = i // divisor
        print("digit : ",digit)
        i -= digit * divisor
        output += chr(48 + digit)
print(output)



n = int(input())
output = ''
for i in range(1,n+1):
    output=output+str(i)
print(output)

