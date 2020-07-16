# Enter your code here. Read input from STDIN. Print output to STDOUT
flag=False
a=set(input().split())
n=int(input())
for i in range(n):
    s=set(input().split())
    if a.issuperset(s) and len(a)>len(s):
        flag=True
    else:
        flag=False
        break 
print(flag)
