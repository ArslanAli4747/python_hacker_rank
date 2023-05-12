
n = 29293
print("{number:a^10}".format(number=n/2))
print(f"{n/2:b>+20,.2f}")

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = student_marks[query_name]
    res = sum(res)/len(res)
    print(f"{res:.2f}")