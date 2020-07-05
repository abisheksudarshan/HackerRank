if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for s in student_marks:
        if s==query_name:
            total=student_marks[s][0]+student_marks[s][1]+student_marks[s][2]
            print ('{0:.2f}'.format(total/3,3))
