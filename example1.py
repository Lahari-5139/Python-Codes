list = []
n = input()
while n > 0:
    line = raw_input()
    line = line.split()
    if line[0] == "insert":
        list.insert(int(line[1]), int(line[2]))
    elif line[0] == "print":
        print list
    elif line[0] == "remove":
        list.remove(int(line[1]))
    elif line[0] == "append":
        list.append(int(line[1]))
    elif line[0] == "sort":
        list.sort()
    elif line[0] == "pop":
        list.pop()
    elif line[0] == "reverse":
        list.reverse()
    n = n-1
