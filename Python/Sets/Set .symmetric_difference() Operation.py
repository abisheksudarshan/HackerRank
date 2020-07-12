# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=list(input().split())
m=int(input())
s2=list(input().split())

s1=set(s1)
s2=set(s2)

print(len(s1.symmetric_difference(s2)))
