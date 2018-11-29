n = input()
names = []
out = []
for i in range(n):
    name = raw_input()
    if (name not in names):
        names.append(name)
        out.append("OK")   
    else:
        for j in range(n):
            s = name+str(j+1)
            if (s not in names):
                names.append(s)
                out.append(s)  
            else:
                for k in range(2,n):
                    s1 = name+str(j+k)
                    names.append(s1)
                    out.append(s1)
                    break
            break
for i in range(n):
    print out[i]

        
