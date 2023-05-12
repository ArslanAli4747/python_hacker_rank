def count_substring(string, sub_string):
    num = 0    
    i = 0
    index = 0
    # while i<len(string):
    #     index = string.find(sub_string,index)
    #     print("\nindex at : ",index)
    #     print("string : ",string)
    #     if index>-1:
    #         num+=1
    #         string = string[len(sub_string)-1:]
            
    #     i+=1
    while i < len(string):
        index = string.find(sub_string, i)
        if index >= 0:
            num += 1
            i = index + 1
        else:
            break 
        
       
    return num

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print("result : ",count)