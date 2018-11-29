string = raw_input()
n = raw_input()
n = n.split(" ")
l = list(string)
l[int(n[0])] = n[1]
lis = "".join(l)
print lis