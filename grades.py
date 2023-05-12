# records = []
# scores = []
# # for _ in range(int(input())):
# #     name = input()
# #     score = float(input())
# #     records.append([score,name])
# #     scores.append(score)

# records = [['Harry', 36], ['Berry', 37], ['Tina', 37], ['Akriti', 41], ['Harsh', 39]]
# scores = [39,41,37,36,37]
# scores  = list(set(scores))
# scores.sort(reverse=False)
# s = scores[1]
# print(s)
# names = []
# for i in records :
#     print(i)
#     if s in i:
#         print(s)
#         names.append(i[0])
        

# names.sort(reverse=False)
# for n in names:
#     print(n)



if __name__ == '__main__':
    names = []
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    
    scores  = list(set(scores))
    scores.sort(reverse=False)
    s = scores[1]
    for i in records :
      if s in i:
        names.append(i[0])
    names.sort(reverse=False)
    for n in names:
        print(n)