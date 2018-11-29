t = ("director",
     [
         (
             "dean",
             [
                 (
                     "prof1",
                     [

                     ]
                 ),
                 (
                     "prof2",
                     [

                     ]
                 )
             ]
         ),
         (
             "administrator",
             [
                 (
                     "admin",
                     [

                     ]
                 ),
                 (
                     "account",
                     [

                     ]
                 )
             ]
         )
     ]
 )

def find(value,t):
    v , subtrees = t
    if (v == value):
        return t
    else:
        for st in subtrees:
            result = find(value,st)
            if (result != None):
                return result
            return None
print (find("dean" , t))

def numofnodes(t):
    v , subtrees = t
    count = 0 
    for st in subtrees:
        count += numofnodes(st)
    return (1+count)
print numofnodes(t)

def addsubtree(v1,v2,t):
    node = find(v1,t)
    if (node != None):
        (_,st) = node
        st.append((v2,[]))
        return t
    return False
print addsubtree("dean","prof3",t) 

def parent(value,t):
    v, subtrees = t
    if (v==value):
        return None
    for st in subtrees:
        (v1,st1) = st
        if (v1==value):
            return t
    for st in subtrees:
        p = parent(value,st)
        if (p!=None):
            return p
        return None
print parent("prof1",t)   
