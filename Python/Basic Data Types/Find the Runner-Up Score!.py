if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(list(arr))
    i=n-1
    cur_max=arr.pop()
    while i>=0:
        if arr[-1]<cur_max:
            print (arr[-1])
            break
        else:
            i-=1
            arr.pop()
