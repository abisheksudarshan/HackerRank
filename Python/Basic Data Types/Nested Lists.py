if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    second_lowest=sorted(list(set(score for name,score in students)))[1]
    print('\n'.join(sorted([s[0] for s in students if s[1]==second_lowest ])))
