ddddnwh = raw_input().split(" ")
n = int(nwh[0])
w = int(nwh[1])
h = int(nwh[2])
widheis = []
for i in range(n):
    newwh = raw_input().split(" ")
    w1 = int(newwh[0])
    h1 = int(newwh[1])
    if (w1 <= w or h1<= h):
        print (0)
    elif (w1 > w and h1 > h):
        if newwh not in widheis:
            widheis.append(newwh)
order = []
if (len(widheis)>=2):
    for i in range(len(widheis)+1):
        if (widheis[i][0] > widheis[i+1][0]):
            order.append(i+1)
        else:
            order.append(1)
print (" ".join(order))
print (len(widheis))
print (widheis)




