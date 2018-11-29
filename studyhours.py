ds = raw_input().split(" ")
d = int(ds[0])
sumTime = int(ds[1])
time = []
for i in range(d):
    minmax = raw_input().split(" ")
    minTime = int(minmax[0])
    maxTime = int(minmax[1])
    nos = []
    for j in range(minTime,maxTime+1):
        nos.append(j)
    time.append(nos)

sum = 0
for i in range(d):
    for j in range(time[i][-1]-time[i][0]):
        for k in range(d):
            sum = sum+time[k][j]
        if (sum == sumTime):
            print "YES"
        else:
            print "NO"
        
        




