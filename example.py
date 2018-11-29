list = []
n = input()
while n > 0:
    line = raw_input()
    print line
    line = line.split()
    print line
    if line[0] == "insert":
        list.insert(int(line[1]), int(line[2]))
    elif line[0] == "print":
        print list
    elif line[0] == "append":
        list.append(int(line[1]))
    print list
    n = n-1
