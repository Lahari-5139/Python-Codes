n = input()
l = []
for i in range(n-1):
    a = input()
    l.append (a)
    
i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)

