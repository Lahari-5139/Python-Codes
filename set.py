n = input()
hs =raw_input().split(" ")
hsnew = []
for i in range(n):
    k = int(hs[i])
    hsnew.append(k) 
j = set(hsnew)
s = sum(j)
avg = s/len(j)
print avg


