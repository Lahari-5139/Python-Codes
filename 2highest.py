N = input()
students = []
for i in range(N):
    name = raw_input()
    marks = input()
    pair = []
    pair.append(name)
    pair.append(marks)
    students.append(pair)
print (students)
markslist = []
for i in range(N):
    markslist.append(students[i][1])
newml = []
for i in range(N):
    if markslist[i] not in newml:
        newml.append(markslist[i])
newml = sorted(newml)
newml = newml[1:]
dic ={}
for i in range(N):
    if students[i][1]== newml[0]:
        dic[students[i][0]]= newml[0]
k = (dic.keys())
k = sorted(k)
for i in k:
    print (i)
   